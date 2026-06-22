from __future__ import annotations


def safe_get(obj, name, default=None):
    try:
        return getattr(obj, name)
    except Exception:
        return default


def serialize_track(track, index):
    return {
        "ref": f"track:{index}",
        "index": index,
        "name": safe_get(track, "name", f"Track {index}"),
        "mute": safe_get(track, "mute"),
        "solo": safe_get(track, "solo"),
        "arm": safe_get(track, "arm"),
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
    }


def serialize_device(device, ref, index):
    return {
        "ref": ref,
        "index": index,
        "name": safe_get(device, "name"),
        "class_name": safe_get(device, "class_name"),
        "class_display_name": safe_get(device, "class_display_name"),
        "is_active": safe_get(device, "is_active"),
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
        "is_enabled": safe_get(param, "is_enabled"),
        "automation_state": safe_get(param, "automation_state"),
    }
