from __future__ import annotations

from ..errors import bad_request, object_not_found
from ..serializers import safe_get


def is_lom_null(obj):
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


def _parse_indexed_ref(ref, prefix):
    if not isinstance(ref, str):
        raise bad_request("Object reference must be a string", {"ref": ref})
    expected = prefix + ":"
    if not ref.startswith(expected):
        raise bad_request("Unexpected object reference type", {"ref": ref, "expected": prefix})
    value = ref[len(expected) :]
    try:
        index = int(value)
    except Exception:
        raise bad_request("Object reference index must be an integer", {"ref": ref})
    if index < 0:
        raise bad_request("Object reference index must be non-negative", {"ref": ref})
    return index


def _item_at(items, index, ref):
    items = list(items or [])
    if index >= len(items):
        raise object_not_found("Referenced object does not exist", {"ref": ref})
    return items[index]


def resolve_track(song, track_ref):
    if not track_ref:
        raise bad_request("track_ref is required")
    if track_ref == "master_track":
        track = safe_get(song, "master_track")
        if is_lom_null(track):
            raise object_not_found("Master track is not available", {"ref": track_ref})
        return track, "master_track", None, "master"
    if isinstance(track_ref, str) and track_ref.startswith("return_track:"):
        index = _parse_indexed_ref(track_ref, "return_track")
        track = _item_at(safe_get(song, "return_tracks", []), index, track_ref)
        return track, track_ref, index, "return"
    index = _parse_indexed_ref(track_ref, "track")
    track = _item_at(safe_get(song, "tracks", []), index, track_ref)
    return track, track_ref, index, None


def iter_track_refs(song, include_return_tracks=True, include_master=True):
    for index, track in enumerate(list(safe_get(song, "tracks", []) or [])):
        yield track, "track:%d" % index, index, None
    if include_return_tracks:
        for index, track in enumerate(list(safe_get(song, "return_tracks", []) or [])):
            yield track, "return_track:%d" % index, index, "return"
    if include_master:
        master_track = safe_get(song, "master_track")
        if not is_lom_null(master_track):
            yield master_track, "master_track", None, "master"


def find_track_ref(song, target):
    if is_lom_null(target):
        return None
    for track, track_ref, index, kind in iter_track_refs(song):
        if track is target:
            return track_ref, index, kind
    return None


def resolve_arrangement_clip(song, clip_ref):
    if not isinstance(clip_ref, str):
        raise bad_request("clip_ref is required and must be a string", {"clip_ref": clip_ref})
    parts = clip_ref.split("/")
    if len(parts) != 2:
        raise bad_request("Expected clip ref shaped like track:N/arrangement_clip:M", {"clip_ref": clip_ref})
    track, track_ref, _track_index, _kind = resolve_track(song, parts[0])
    clip_index = _parse_indexed_ref(parts[1], "arrangement_clip")
    clip = _item_at(safe_get(track, "arrangement_clips", []), clip_index, clip_ref)
    return clip, "%s/arrangement_clip:%d" % (track_ref, clip_index), track, track_ref, clip_index


def find_arrangement_clip_ref(song, target):
    if is_lom_null(target):
        return None
    for track, track_ref, _index, _kind in iter_track_refs(song, include_master=False):
        clips = list(safe_get(track, "arrangement_clips", []) or [])
        for clip_index, clip in enumerate(clips):
            if clip is target:
                return "%s/arrangement_clip:%d" % (track_ref, clip_index), track, track_ref, clip_index
    return None


def resolve_device(song, device_ref):
    if not isinstance(device_ref, str):
        raise bad_request("device_ref is required and must be a string", {"device_ref": device_ref})
    parts = device_ref.split("/")
    if len(parts) != 2:
        raise bad_request("Expected device ref shaped like track:N/device:M", {"device_ref": device_ref})
    track, track_ref, _track_index, _kind = resolve_track(song, parts[0])
    device_index = _parse_indexed_ref(parts[1], "device")
    device = _item_at(safe_get(track, "devices", []), device_index, device_ref)
    return device, "%s/device:%d" % (track_ref, device_index), track, track_ref, device_index


def find_device_ref(song, target, track=None, track_ref=None):
    if is_lom_null(target):
        return None
    candidates = [(track, track_ref)] if track is not None and track_ref else []
    candidates.extend((candidate, ref) for candidate, ref, _index, _kind in iter_track_refs(song))
    seen_refs = set()
    for candidate, candidate_ref in candidates:
        if candidate_ref in seen_refs:
            continue
        seen_refs.add(candidate_ref)
        for device_index, device in enumerate(list(safe_get(candidate, "devices", []) or [])):
            if device is target:
                return "%s/device:%d" % (candidate_ref, device_index), candidate, candidate_ref, device_index
    return None


def resolve_parameter(song, parameter_ref):
    if not isinstance(parameter_ref, str):
        raise bad_request("parameter_ref is required and must be a string", {"parameter_ref": parameter_ref})
    parts = parameter_ref.split("/")
    if len(parts) != 3:
        raise bad_request(
            "Expected parameter ref shaped like track:N/device:M/parameter:P",
            {"parameter_ref": parameter_ref},
        )
    device, device_ref, track, track_ref, device_index = resolve_device(song, "/".join(parts[:2]))
    parameter_index = _parse_indexed_ref(parts[2], "parameter")
    parameter = _item_at(safe_get(device, "parameters", []), parameter_index, parameter_ref)
    return (
        parameter,
        "%s/parameter:%d" % (device_ref, parameter_index),
        device,
        device_ref,
        track,
        track_ref,
        device_index,
        parameter_index,
    )


def find_parameter_ref(song, target):
    if is_lom_null(target):
        return None
    for track, track_ref, _track_index, _kind in iter_track_refs(song):
        for device_index, device in enumerate(list(safe_get(track, "devices", []) or [])):
            for parameter_index, parameter in enumerate(list(safe_get(device, "parameters", []) or [])):
                if parameter is target:
                    device_ref = "%s/device:%d" % (track_ref, device_index)
                    return "%s/parameter:%d" % (device_ref, parameter_index), device, device_ref, track, track_ref
    return None
