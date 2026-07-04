from __future__ import annotations


PLUGIN_CLASS_NAMES = ("PluginDevice",)
MAX_FOR_LIVE_CLASS_PREFIXES = ("MxDevice", "Max")


def safe_get(obj, name, default=None):
    try:
        return getattr(obj, name)
    except Exception:
        return default


def safe_call(obj, name, default=None):
    try:
        fn = getattr(obj, name)
    except Exception:
        return default
    try:
        return fn()
    except Exception:
        return default


def safe_len(value):
    try:
        return len(list(value or []))
    except Exception:
        return None


def safe_list(value):
    if value is None:
        return None
    if isinstance(value, (str, bytes)):
        return [value]
    try:
        return list(value)
    except Exception:
        return None


def is_lom_nullish(obj):
    if obj is None:
        return True
    try:
        if int(obj) == 0:
            return True
    except Exception:
        pass
    try:
        return str(obj) == "id 0"
    except Exception:
        return False


def infer_track_kind(track, ref=None, kind=None):
    if kind:
        return kind
    if ref == "master_track":
        return "master"
    if isinstance(ref, str) and ref.startswith("return_track:"):
        return "return"
    has_midi_input = safe_get(track, "has_midi_input")
    has_audio_input = safe_get(track, "has_audio_input")
    if has_midi_input and not has_audio_input:
        return "midi"
    if has_audio_input and not has_midi_input:
        return "audio"
    if has_midi_input and has_audio_input:
        return "audio_midi"
    return None


def serialize_track(track, index, ref=None, kind=None):
    ref = ref or "track:%d" % index
    return {
        "ref": ref,
        "index": index,
        "name": safe_get(track, "name", f"Track {index}"),
        "kind": infer_track_kind(track, ref, kind),
        "mute": safe_get(track, "mute"),
        "solo": safe_get(track, "solo"),
        "arm": safe_get(track, "arm"),
        "can_be_armed": safe_get(track, "can_be_armed"),
        "is_frozen": safe_get(track, "is_frozen"),
        "color": safe_get(track, "color"),
        "color_index": safe_get(track, "color_index"),
        "has_audio_input": safe_get(track, "has_audio_input"),
        "has_audio_output": safe_get(track, "has_audio_output"),
        "has_midi_input": safe_get(track, "has_midi_input"),
        "has_midi_output": safe_get(track, "has_midi_output"),
        "arrangement_clip_count": safe_len(safe_get(track, "arrangement_clips", [])),
        "device_count": safe_len(safe_get(track, "devices", [])),
    }


def serialize_clip(clip, ref):
    return {
        "ref": ref,
        "name": safe_get(clip, "name"),
        "is_audio_clip": safe_get(clip, "is_audio_clip"),
        "is_midi_clip": safe_get(clip, "is_midi_clip"),
        "is_arrangement_clip": safe_get(clip, "is_arrangement_clip"),
        "start_time": safe_get(clip, "start_time"),
        "end_time": safe_get(clip, "end_time"),
        "length": safe_get(clip, "length"),
        "looping": safe_get(clip, "looping"),
        "loop_start": safe_get(clip, "loop_start"),
        "loop_end": safe_get(clip, "loop_end"),
        "start_marker": safe_get(clip, "start_marker"),
        "end_marker": safe_get(clip, "end_marker"),
        "file_path": safe_get(clip, "file_path"),
        "gain": safe_get(clip, "gain"),
        "warping": safe_get(clip, "warping"),
        "warp_mode": safe_get(clip, "warp_mode"),
        "sample_length": safe_get(clip, "sample_length"),
        "sample_rate": safe_get(clip, "sample_rate"),
    }


def serialize_device(device, ref, index):
    parameter_count = safe_len(safe_get(device, "parameters", []))
    device_kind = classify_device(device)
    return {
        "ref": ref,
        "index": index,
        "name": safe_get(device, "name"),
        "class_name": safe_get(device, "class_name"),
        "class_display_name": safe_get(device, "class_display_name"),
        "device_kind": device_kind,
        "is_plugin": device_kind == "plugin",
        "is_native": device_kind == "native",
        "is_active": safe_get(device, "is_active"),
        "type": safe_get(device, "type"),
        "can_have_chains": safe_get(device, "can_have_chains"),
        "can_have_drum_pads": safe_get(device, "can_have_drum_pads"),
        "latency_in_samples": safe_get(device, "latency_in_samples"),
        "latency_in_ms": safe_get(device, "latency_in_ms"),
        "parameter_count": parameter_count,
        "exposure_status": parameter_exposure_status(device, parameter_count),
    }


def classify_device(device):
    class_name = safe_get(device, "class_name") or ""
    if class_name in PLUGIN_CLASS_NAMES or "Plugin" in class_name:
        return "plugin"
    for prefix in MAX_FOR_LIVE_CLASS_PREFIXES:
        if class_name.startswith(prefix):
            return "max_for_live"
    if class_name:
        return "native"
    return "unknown"


def parameter_exposure_status(device, parameter_count=None):
    if parameter_count is None:
        parameter_count = safe_len(safe_get(device, "parameters", []))
    device_kind = classify_device(device)
    if parameter_count is None:
        return "unknown"
    if device_kind == "plugin":
        if parameter_count == 0:
            return "none_exposed"
        if parameter_count <= 8:
            return "minimal_or_preconfigured"
        return "configured_or_exposed"
    if parameter_count == 0:
        return "no_exposed_parameters"
    return "live_exposed_parameters"


def serialize_parameter(param, ref, index):
    return {
        "ref": ref,
        "index": index,
        "name": safe_get(param, "name"),
        "original_name": safe_get(param, "original_name"),
        "value": safe_get(param, "value"),
        "display_value": safe_get(param, "display_value"),
        "min": safe_get(param, "min"),
        "max": safe_get(param, "max"),
        "default_value": safe_get(param, "default_value"),
        "is_enabled": safe_get(param, "is_enabled"),
        "is_quantized": safe_get(param, "is_quantized"),
        "automation_state": safe_get(param, "automation_state"),
        "state": safe_get(param, "state"),
        "value_items": safe_list(safe_get(param, "value_items")),
    }


def _basename(path):
    if not path:
        return None
    text = str(path).replace("\\", "/").rstrip("/")
    if not text:
        return None
    return text.rsplit("/", 1)[-1]


def serialize_sample(sample):
    if is_lom_nullish(sample):
        return None
    file_path = safe_get(sample, "file_path")
    raw_warp_markers = safe_get(sample, "warp_markers")
    return {
        "name": _basename(file_path),
        "file_path": file_path,
        "length": safe_get(sample, "length"),
        "sample_rate": safe_get(sample, "sample_rate"),
        "slices": safe_list(safe_get(sample, "slices")),
        "start_marker": safe_get(sample, "start_marker"),
        "end_marker": safe_get(sample, "end_marker"),
        "warp_markers": None if raw_warp_markers is None else normalize_warp_markers(raw_warp_markers),
        "warp_mode": safe_get(sample, "warp_mode"),
        "warping": safe_get(sample, "warping"),
        "slicing_style": safe_get(sample, "slicing_style"),
        "slicing_beat_division": safe_get(sample, "slicing_beat_division"),
        "slicing_region_count": safe_get(sample, "slicing_region_count"),
    }


def _parameter_children(obj, ref):
    children = []
    for name in (
        "volume",
        "panning",
        "left_split_stereo",
        "right_split_stereo",
        "track_activator",
        "crossfader",
        "cue_volume",
        "song_tempo",
        "chain_activator",
    ):
        param = safe_get(obj, name)
        if not is_lom_nullish(param):
            children.append(serialize_parameter(param, "%s/%s" % (ref, name), len(children)))
    sends = safe_list(safe_get(obj, "sends")) or []
    for send_index, param in enumerate(sends):
        if not is_lom_nullish(param):
            children.append(serialize_parameter(param, "%s/send:%d" % (ref, send_index), len(children)))
    return children


def serialize_mixer_device(mixer_device, ref):
    if is_lom_nullish(mixer_device):
        return None
    parameters = _parameter_children(mixer_device, ref)
    return {
        "ref": ref,
        "panning_mode": safe_get(mixer_device, "panning_mode"),
        "crossfade_assign": safe_get(mixer_device, "crossfade_assign"),
        "parameter_count": len(parameters),
        "parameters": parameters,
    }


def serialize_chain(
    chain,
    ref,
    index,
    depth=0,
    max_depth=8,
    include_parameters=True,
    include_empty_drum_pads=False,
    _seen=None,
):
    devices = list(safe_get(chain, "devices", []) or [])
    mixer = serialize_mixer_device(safe_get(chain, "mixer_device"), "%s/mixer_device" % ref)
    return {
        "ref": ref,
        "index": index,
        "name": safe_get(chain, "name"),
        "depth": depth,
        "color": safe_get(chain, "color"),
        "color_index": safe_get(chain, "color_index"),
        "is_auto_colored": safe_get(chain, "is_auto_colored"),
        "mute": safe_get(chain, "mute"),
        "muted_via_solo": safe_get(chain, "muted_via_solo"),
        "solo": safe_get(chain, "solo"),
        "has_audio_input": safe_get(chain, "has_audio_input"),
        "has_audio_output": safe_get(chain, "has_audio_output"),
        "has_midi_input": safe_get(chain, "has_midi_input"),
        "has_midi_output": safe_get(chain, "has_midi_output"),
        "in_note": safe_get(chain, "in_note"),
        "out_note": safe_get(chain, "out_note"),
        "choke_group": safe_get(chain, "choke_group"),
        "mixer_device": mixer,
        "device_count": len(devices),
        "devices": [
            serialize_device_tree(
                device,
                "%s/device:%d" % (ref, device_index),
                device_index,
                depth=depth,
                max_depth=max_depth,
                include_parameters=include_parameters,
                include_empty_drum_pads=include_empty_drum_pads,
                _seen=_seen,
            )
            for device_index, device in enumerate(devices)
        ],
    }


def serialize_drum_pad(
    drum_pad,
    ref,
    index,
    depth=0,
    max_depth=8,
    include_parameters=True,
    include_empty_drum_pads=False,
    _seen=None,
):
    chains = list(safe_get(drum_pad, "chains", []) or [])
    return {
        "ref": ref,
        "index": index,
        "name": safe_get(drum_pad, "name"),
        "note": safe_get(drum_pad, "note"),
        "mute": safe_get(drum_pad, "mute"),
        "solo": safe_get(drum_pad, "solo"),
        "chain_count": len(chains),
        "chains": [
            serialize_chain(
                chain,
                "%s/chain:%d" % (ref, chain_index),
                chain_index,
                depth=depth + 1,
                max_depth=max_depth,
                include_parameters=include_parameters,
                include_empty_drum_pads=include_empty_drum_pads,
                _seen=_seen,
            )
            for chain_index, chain in enumerate(chains)
        ],
    }


def _tree_counts(tree):
    nested_device_count = 0
    sample_count = 1 if tree.get("sample") else 0
    exposed_parameter_count = tree.get("parameter_count") or 0
    for collection_name in ("chains", "return_chains"):
        for chain in tree.get(collection_name, []):
            for device in chain.get("devices", []):
                nested_device_count += 1
                counts = _tree_counts(device)
                nested_device_count += counts["nested_device_count"]
                sample_count += counts["sample_count"]
                exposed_parameter_count += counts["exposed_parameter_count"]
    for pad in tree.get("drum_pads", []):
        for chain in pad.get("chains", []):
            for device in chain.get("devices", []):
                nested_device_count += 1
                counts = _tree_counts(device)
                nested_device_count += counts["nested_device_count"]
                sample_count += counts["sample_count"]
                exposed_parameter_count += counts["exposed_parameter_count"]
    return {
        "nested_device_count": nested_device_count,
        "sample_count": sample_count,
        "exposed_parameter_count": exposed_parameter_count,
    }


def serialize_device_tree(
    device,
    ref,
    index,
    depth=0,
    max_depth=8,
    include_parameters=True,
    include_empty_drum_pads=False,
    _seen=None,
):
    _seen = _seen or set()
    data = serialize_device(device, ref, index)
    data["depth"] = depth
    data["limitations"] = []
    object_id = id(device)
    if object_id in _seen:
        data["limitations"].append(
            {
                "code": "DEVICE_TREE_CYCLE_DETECTED",
                "message": "Device tree recursion stopped because the same object was reached twice.",
            }
        )
        data["chains"] = []
        data["return_chains"] = []
        data["drum_pads"] = []
        return data
    _seen.add(object_id)

    parameters = list(safe_get(device, "parameters", []) or [])
    if include_parameters:
        data["parameters"] = [
            serialize_parameter(param, "%s/parameter:%d" % (ref, parameter_index), parameter_index)
            for parameter_index, param in enumerate(parameters)
        ]
    data["sample"] = serialize_sample(safe_get(device, "sample"))

    chains = list(safe_get(device, "chains", []) or [])
    return_chains = list(safe_get(device, "return_chains", []) or [])
    drum_pads = list(safe_get(device, "drum_pads", []) or [])
    visible_drum_pads = list(safe_get(device, "visible_drum_pads", []) or [])
    data["chain_count"] = len(chains)
    data["return_chain_count"] = len(return_chains)
    data["drum_pad_count"] = len(drum_pads)
    data["visible_drum_pad_count"] = len(visible_drum_pads)
    data["non_empty_drum_pad_count"] = len(
        [pad for pad in drum_pads if len(list(safe_get(pad, "chains", []) or [])) > 0]
    )

    if depth >= max_depth:
        data["chains"] = []
        data["return_chains"] = []
        data["drum_pads"] = []
        data["limitations"].append(
            {
                "code": "DEVICE_TREE_MAX_DEPTH_REACHED",
                "message": "Device tree recursion stopped at the configured max_depth.",
                "details": {"max_depth": max_depth},
            }
        )
    else:
        # Top-level Drum Rack chains are also reachable through DrumPad.chains.
        # Prefer the pad path for nested devices so counts and parameter totals
        # do not double-count the same Simpler/device objects.
        chain_items = [] if drum_pads and safe_get(device, "can_have_drum_pads") else chains
        data["chains"] = [
            serialize_chain(
                chain,
                "%s/chain:%d" % (ref, chain_index),
                chain_index,
                depth=depth + 1,
                max_depth=max_depth,
                include_parameters=include_parameters,
                include_empty_drum_pads=include_empty_drum_pads,
                _seen=_seen,
            )
            for chain_index, chain in enumerate(chain_items)
        ]
        data["return_chains"] = [
            serialize_chain(
                chain,
                "%s/return_chain:%d" % (ref, chain_index),
                chain_index,
                depth=depth + 1,
                max_depth=max_depth,
                include_parameters=include_parameters,
                include_empty_drum_pads=include_empty_drum_pads,
                _seen=_seen,
            )
            for chain_index, chain in enumerate(return_chains)
        ]
        filtered_drum_pads = []
        for pad_index, drum_pad in enumerate(drum_pads):
            pad_chains = list(safe_get(drum_pad, "chains", []) or [])
            if include_empty_drum_pads or pad_chains:
                filtered_drum_pads.append((pad_index, drum_pad))
        data["drum_pads"] = [
            serialize_drum_pad(
                drum_pad,
                "%s/drum_pad:%d" % (ref, pad_index),
                pad_index,
                depth=depth + 1,
                max_depth=max_depth,
                include_parameters=include_parameters,
                include_empty_drum_pads=include_empty_drum_pads,
                _seen=_seen,
            )
            for pad_index, drum_pad in filtered_drum_pads
        ]

    counts = _tree_counts(data)
    data["nested_device_count"] = counts["nested_device_count"]
    data["sample_count"] = counts["sample_count"]
    data["total_exposed_parameter_count"] = counts["exposed_parameter_count"]
    _seen.discard(object_id)
    return data


_NOTE_FIELDS = (
    "note_id",
    "pitch",
    "start_time",
    "duration",
    "velocity",
    "mute",
    "probability",
    "velocity_deviation",
    "release_velocity",
)


def _note_to_dict(note):
    if isinstance(note, dict):
        return dict(note)
    data = {}
    for field in _NOTE_FIELDS:
        if hasattr(note, field):
            data[field] = getattr(note, field)
    return data


def normalize_note_payload(payload):
    # Real Live returns a MidiNoteVector of MidiNote objects, which is
    # neither dict nor list/tuple. Iterate anything iterable and
    # serialize note objects by attribute.
    if payload is None:
        return []
    if isinstance(payload, dict):
        notes = payload.get("notes", [])
        return [_note_to_dict(note) for note in (notes or [])]
    try:
        return [_note_to_dict(note) for note in payload]
    except TypeError:
        return []


def _marker_from_dict(marker):
    if "sample_time" in marker and "beat_time" in marker:
        return {"sample_time": marker.get("sample_time"), "beat_time": marker.get("beat_time")}
    return dict(marker)


def _marker_to_dict(marker):
    if isinstance(marker, dict):
        return _marker_from_dict(marker)
    if isinstance(marker, (list, tuple)) and len(marker) == 2:
        return {"sample_time": marker[0], "beat_time": marker[1]}
    if hasattr(marker, "sample_time") and hasattr(marker, "beat_time"):
        return {"sample_time": marker.sample_time, "beat_time": marker.beat_time}
    return None


def normalize_warp_markers(payload):
    if payload is None:
        return []
    if isinstance(payload, dict):
        if "warp_markers" in payload:
            return normalize_warp_markers(payload.get("warp_markers"))
        if "sample_time" in payload and "beat_time" in payload:
            sample_time = payload.get("sample_time")
            beat_time = payload.get("beat_time")
            if isinstance(sample_time, (list, tuple)) and isinstance(beat_time, (list, tuple)):
                return [
                    {"sample_time": sample, "beat_time": beat}
                    for sample, beat in zip(sample_time, beat_time)
                ]
            return [{"sample_time": sample_time, "beat_time": beat_time}]
        markers = []
        for sample_time, beat_time in payload.items():
            markers.append({"sample_time": sample_time, "beat_time": beat_time})
        return markers
    # Real Live returns a WarpMarkerVector of WarpMarker objects, which is
    # neither dict nor list/tuple. Iterate anything iterable and accept
    # dicts, 2-sequences, or attribute objects.
    try:
        markers = []
        for marker in payload:
            data = _marker_to_dict(marker)
            if data is not None:
                markers.append(data)
        return markers
    except TypeError:
        return []
