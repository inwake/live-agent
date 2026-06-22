from __future__ import annotations


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
    return {
        "ref": ref,
        "index": index,
        "name": safe_get(device, "name"),
        "class_name": safe_get(device, "class_name"),
        "class_display_name": safe_get(device, "class_display_name"),
        "is_active": safe_get(device, "is_active"),
        "type": safe_get(device, "type"),
        "can_have_chains": safe_get(device, "can_have_chains"),
        "can_have_drum_pads": safe_get(device, "can_have_drum_pads"),
        "latency_in_samples": safe_get(device, "latency_in_samples"),
        "latency_in_ms": safe_get(device, "latency_in_ms"),
        "parameter_count": safe_len(safe_get(device, "parameters", [])),
    }


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


def normalize_note_payload(payload):
    if payload is None:
        return []
    if isinstance(payload, dict):
        notes = payload.get("notes", [])
        return list(notes or [])
    if isinstance(payload, (list, tuple)):
        return list(payload)
    return []


def _marker_from_dict(marker):
    if "sample_time" in marker and "beat_time" in marker:
        return {"sample_time": marker.get("sample_time"), "beat_time": marker.get("beat_time")}
    return dict(marker)


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
    if isinstance(payload, (list, tuple)):
        markers = []
        for marker in payload:
            if isinstance(marker, dict):
                markers.append(_marker_from_dict(marker))
            elif isinstance(marker, (list, tuple)) and len(marker) == 2:
                markers.append({"sample_time": marker[0], "beat_time": marker[1]})
        return markers
    return []
