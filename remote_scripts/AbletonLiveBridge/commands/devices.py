from __future__ import annotations

from ..serializers import (
    normalize_note_payload,
    safe_get,
    serialize_clip,
    serialize_device,
    serialize_device_tree,
    serialize_mixer_device,
    serialize_parameter,
    serialize_track,
)
from .resolvers import iter_track_refs, resolve_device, resolve_track
from .song import scan_song


def get_track_devices(song, params, app=None):
    track_ref = params["track_ref"]
    track, track_ref, _index, _kind = resolve_track(song, track_ref)
    devices = list(safe_get(track, "devices", []) or [])
    return {
        "track_ref": track_ref,
        "track_name": safe_get(track, "name"),
        "device_count": len(devices),
        "devices": [serialize_device(device, f"{track_ref}/device:{i}", i) for i, device in enumerate(devices)],
    }


def get_device_parameters(song, params, app=None):
    device_ref = params["device_ref"]
    device, device_ref, _track, track_ref, _device_index = resolve_device(song, device_ref)
    parameters = list(safe_get(device, "parameters", []) or [])
    return {
        "track_ref": track_ref,
        "device_ref": device_ref,
        "device": serialize_device(device, device_ref, _device_index),
        "parameter_count": len(parameters),
        "parameters": [serialize_parameter(param, f"{device_ref}/parameter:{i}", i) for i, param in enumerate(parameters)],
    }


def _as_bool(value, default=False):
    if value is None:
        return default
    return bool(value)


def _as_int(value, default):
    if value is None:
        return default
    try:
        return int(value)
    except Exception:
        return default


def _tree_options(params):
    return {
        "max_depth": _as_int(params.get("max_depth"), 8),
        "include_parameters": _as_bool(params.get("include_parameters"), True),
        "include_empty_drum_pads": _as_bool(params.get("include_empty_drum_pads"), False),
    }


def _device_trees_for_track(track, track_ref, params):
    options = _tree_options(params)
    devices = list(safe_get(track, "devices", []) or [])
    return [
        serialize_device_tree(
            device,
            "%s/device:%d" % (track_ref, device_index),
            device_index,
            max_depth=options["max_depth"],
            include_parameters=options["include_parameters"],
            include_empty_drum_pads=options["include_empty_drum_pads"],
        )
        for device_index, device in enumerate(devices)
    ]


def _walk_device_tree(tree):
    yield tree
    for collection_name in ("chains", "return_chains"):
        for chain in tree.get(collection_name, []):
            for device in chain.get("devices", []):
                for nested in _walk_device_tree(device):
                    yield nested
    for pad in tree.get("drum_pads", []):
        for chain in pad.get("chains", []):
            for device in chain.get("devices", []):
                for nested in _walk_device_tree(device):
                    yield nested


def _track_arrangement_clips(track, track_ref):
    clips = list(safe_get(track, "arrangement_clips", []) or [])
    return [
        serialize_clip(clip, "%s/arrangement_clip:%d" % (track_ref, clip_index))
        for clip_index, clip in enumerate(clips)
    ]


def _track_parameter_count(device_trees):
    return sum((device.get("parameter_count") or 0) for tree in device_trees for device in _walk_device_tree(tree))


def _plugin_notes(device):
    count = device.get("parameter_count") or 0
    if count == 0:
        return "Live exposes no DeviceParameter objects for this plugin."
    if device.get("exposure_status") == "minimal_or_preconfigured":
        return (
            "Live exposes %d DeviceParameter object(s); this may be a minimal or "
            "preconfigured parameter set, not hidden plugin internals."
        ) % count
    return "Live exposes %d DeviceParameter object(s); hidden plugin internals remain unavailable." % count


def inspect_device_tree(song, params, app=None):
    device_ref = params["device_ref"]
    options = _tree_options(params)
    device, device_ref, _track, track_ref, device_index = resolve_device(song, device_ref)
    tree = serialize_device_tree(
        device,
        device_ref,
        device_index,
        max_depth=options["max_depth"],
        include_parameters=options["include_parameters"],
        include_empty_drum_pads=options["include_empty_drum_pads"],
    )
    return {
        "track_ref": track_ref,
        "device_ref": device_ref,
        "device_tree": tree,
        "limitations": tree.get("limitations", []),
    }


def inspect_track_detail(song, params, app=None):
    track_ref = params["track_ref"]
    track, track_ref, index, kind = resolve_track(song, track_ref)
    devices = _device_trees_for_track(track, track_ref, params)
    arrangement_clips = _track_arrangement_clips(track, track_ref)
    mixer_device = serialize_mixer_device(safe_get(track, "mixer_device"), "%s/mixer_device" % track_ref)
    exposed_parameter_count = _track_parameter_count(devices)
    return {
        "track": serialize_track(track, index, ref=track_ref, kind=kind),
        "track_ref": track_ref,
        "arrangement_clip_count": len(arrangement_clips),
        "arrangement_clips": arrangement_clips,
        "device_count": len(devices),
        "devices": devices,
        "mixer_device": mixer_device,
        "mixer_exposed_parameter_count": 0 if mixer_device is None else mixer_device["parameter_count"],
        "exposed_parameter_count": exposed_parameter_count,
    }


def _parameter_examples(device, limit=5):
    return [param.get("name") for param in device.get("parameters", [])[:limit] if param.get("name")]


def _exposure_entry(track, track_ref, device):
    return {
        "track": safe_get(track, "name"),
        "track_ref": track_ref,
        "device": device.get("name"),
        "device_ref": device.get("ref"),
        "class_name": device.get("class_name"),
        "class_display_name": device.get("class_display_name"),
        "device_kind": device.get("device_kind"),
        "exposed_parameter_count": device.get("parameter_count") or 0,
        "exposure_status": device.get("exposure_status"),
        "example_parameters": _parameter_examples(device),
    }


def inspect_parameter_exposure(song, params, app=None):
    tracks = []
    return_tracks = []
    master_track = None
    plugin_devices = []
    native_devices = []
    other_devices = []
    totals = {
        "device_count": 0,
        "plugin_device_count": 0,
        "native_device_count": 0,
        "max_for_live_device_count": 0,
        "unknown_device_count": 0,
        "exposed_parameter_count": 0,
    }

    for track, track_ref, index, kind in iter_track_refs(song):
        device_trees = _device_trees_for_track(track, track_ref, params)
        devices = [device for tree in device_trees for device in _walk_device_tree(tree)]
        exposed_parameter_count = sum((device.get("parameter_count") or 0) for device in devices)
        summary = {
            "track_ref": track_ref,
            "name": safe_get(track, "name"),
            "kind": kind or serialize_track(track, index, ref=track_ref).get("kind"),
            "device_count": len(devices),
            "top_level_device_count": len(device_trees),
            "exposed_parameter_count": exposed_parameter_count,
        }
        if kind == "return":
            return_tracks.append(summary)
        elif kind == "master":
            master_track = summary
        else:
            tracks.append(summary)

        for device in devices:
            totals["device_count"] += 1
            totals["exposed_parameter_count"] += device.get("parameter_count") or 0
            entry = _exposure_entry(track, track_ref, device)
            device_kind = device.get("device_kind") or "unknown"
            if device_kind == "plugin":
                totals["plugin_device_count"] += 1
                entry["notes"] = _plugin_notes(device)
                plugin_devices.append(entry)
            elif device_kind == "native":
                totals["native_device_count"] += 1
                native_devices.append(entry)
            elif device_kind == "max_for_live":
                totals["max_for_live_device_count"] += 1
                other_devices.append(entry)
            else:
                totals["unknown_device_count"] += 1
                other_devices.append(entry)

    return {
        "totals": totals,
        "tracks": tracks,
        "return_tracks": return_tracks,
        "master_track": master_track,
        "plugin_devices": plugin_devices,
        "native_devices": native_devices,
        "other_devices": other_devices,
        "limitations": [_hidden_plugin_parameter_limitation()],
    }


def _hidden_plugin_parameter_limitation():
    return {
        "code": "HIDDEN_PLUGIN_PARAMETERS_UNAVAILABLE",
        "message": "Only parameters exposed to Live as DeviceParameter objects are visible.",
    }


def _standard_limitations():
    return [
        _hidden_plugin_parameter_limitation(),
        {
            "code": "RENDERED_WAVEFORMS_UNAVAILABLE",
            "message": "Rendered waveform image data is not exposed through the Live Object Model.",
        },
        {
            "code": "PLUGIN_GUI_UNAVAILABLE",
            "message": "Plugin GUI contents and private plugin internals are not exposed through this bridge.",
        },
        {
            "code": "SAMPLER_WAVEFORM_DISPLAY_UNAVAILABLE",
            "message": "Sampler waveform displays are not exposed; only documented Simpler/Sample properties are read.",
        },
    ]


def _clip_note_visibility(clip, clip_ref):
    try:
        payload = clip.get_all_notes_extended()
        notes = normalize_note_payload(payload)
    except Exception as exc:
        return {
            "clip": safe_get(clip, "name") or clip_ref,
            "clip_ref": clip_ref,
            "note_count": 0,
            "velocity_visible": False,
            "probability_visible": False,
            "velocity_deviation_visible": False,
            "release_velocity_visible": False,
            "limitation": {
                "code": "MIDI_NOTES_UNAVAILABLE",
                "message": str(exc),
            },
        }
    return {
        "clip": safe_get(clip, "name") or clip_ref,
        "clip_ref": clip_ref,
        "note_count": len(notes),
        "velocity_visible": any("velocity" in note for note in notes),
        "probability_visible": any("probability" in note for note in notes),
        "velocity_deviation_visible": any("velocity_deviation" in note for note in notes),
        "release_velocity_visible": any("release_velocity" in note for note in notes),
    }


def _rack_summaries(track, device_trees):
    summaries = []
    for tree in device_trees:
        for device in _walk_device_tree(tree):
            chain_count = (device.get("chain_count") or 0) + (device.get("return_chain_count") or 0)
            drum_pads = device.get("drum_pad_count") or 0
            if chain_count or drum_pads:
                summaries.append(
                    {
                        "track": safe_get(track, "name"),
                        "track_ref": device.get("ref", "").split("/device:", 1)[0],
                        "rack": device.get("name"),
                        "device_ref": device.get("ref"),
                        "class_name": device.get("class_name"),
                        "depth": device.get("depth") or 0,
                        "chains": chain_count,
                        "drum_pads": drum_pads,
                        "nested_devices": device.get("nested_device_count") or 0,
                        "samples_found": device.get("sample_count") or 0,
                    }
                )
    return summaries


def inspect_live_set_capabilities(song, params, app=None):
    summary = scan_song(song, params, app=app)
    parameter_exposure = inspect_parameter_exposure(song, params, app=app)
    arrangement_clip_count = 0
    midi_clip_count = 0
    audio_clip_count = 0
    midi_note_visibility = []
    rack_depth = []
    track_rows = []
    return_track_rows = []

    for track, track_ref, index, kind in iter_track_refs(song):
        clips = _track_arrangement_clips(track, track_ref)
        device_trees = _device_trees_for_track(track, track_ref, params)
        exposed_parameter_count = _track_parameter_count(device_trees)
        arrangement_clip_count += len(clips)
        midi_clip_count += len([clip for clip in clips if clip.get("is_midi_clip")])
        audio_clip_count += len([clip for clip in clips if clip.get("is_audio_clip")])
        for clip_index, clip in enumerate(list(safe_get(track, "arrangement_clips", []) or [])):
            if safe_get(clip, "is_midi_clip"):
                midi_note_visibility.append(
                    _clip_note_visibility(clip, "%s/arrangement_clip:%d" % (track_ref, clip_index))
                )
        rack_depth.extend(_rack_summaries(track, device_trees))
        row = {
            "ref": track_ref,
            "name": safe_get(track, "name"),
            "kind": kind or serialize_track(track, index, ref=track_ref).get("kind"),
            "arrangement_clip_count": len(clips),
            "device_count": len(device_trees),
            "exposed_parameter_count": exposed_parameter_count,
        }
        if kind == "return":
            return_track_rows.append(row)
        elif kind != "master":
            track_rows.append(row)

    return {
        "application": summary.get("application", {}),
        "set_summary": {
            "name": summary.get("name"),
            "tempo": summary.get("tempo"),
            "signature": "%s/%s"
            % (summary.get("signature_numerator"), summary.get("signature_denominator")),
            "track_count": summary.get("track_count"),
            "return_track_count": summary.get("return_track_count"),
            "master_track_visible": summary.get("master_track") is not None,
            "arrangement_clip_count": arrangement_clip_count,
            "midi_clip_count": midi_clip_count,
            "audio_clip_count": audio_clip_count,
        },
        "tracks": track_rows,
        "return_tracks": return_track_rows,
        "master_track": parameter_exposure.get("master_track"),
        "parameter_exposure": parameter_exposure,
        "rack_depth": rack_depth,
        "midi_note_visibility": midi_note_visibility,
        "limitations_observed": _standard_limitations(),
    }
