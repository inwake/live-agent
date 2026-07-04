from __future__ import annotations

from ..errors import unsupported_operation
from ..serializers import (
    normalize_note_payload,
    normalize_warp_markers,
    safe_get,
    serialize_clip,
)
from .resolvers import resolve_arrangement_clip


def _clip_type(clip):
    if safe_get(clip, "is_midi_clip"):
        return "midi"
    if safe_get(clip, "is_audio_clip"):
        return "audio"
    return "unknown"


def _has_note_range(params):
    return any(params.get(name) is not None for name in ("from_time", "time_span", "from_pitch", "pitch_span"))


def _note_range(clip, params):
    from_pitch = params.get("from_pitch")
    pitch_span = params.get("pitch_span")
    from_time = params.get("from_time")
    time_span = params.get("time_span")
    if from_pitch is None:
        from_pitch = 0
    if pitch_span is None:
        pitch_span = 128 - int(from_pitch)
    if from_time is None:
        from_time = 0.0
    if time_span is None:
        time_span = safe_get(clip, "length", 0.0) or 0.0
    return {
        "from_pitch": int(from_pitch),
        "pitch_span": int(pitch_span),
        "from_time": float(from_time),
        "time_span": float(time_span),
    }


def get_clip(song, params, app=None):
    clip_ref = params["clip_ref"]
    clip, clip_ref, _track, _track_ref, _clip_index = resolve_arrangement_clip(song, clip_ref)
    return {"clip": serialize_clip(clip, clip_ref)}


def get_clip_notes(song, params, app=None):
    clip_ref = params["clip_ref"]
    clip, clip_ref, _track, _track_ref, _clip_index = resolve_arrangement_clip(song, clip_ref)
    if not safe_get(clip, "is_midi_clip"):
        raise unsupported_operation(
            "Clip is not a MIDI clip; note APIs are unavailable",
            {"clip_ref": clip_ref, "clip_type": _clip_type(clip)},
        )
    note_range = None
    if _has_note_range(params):
        if not hasattr(clip, "get_notes_extended"):
            raise unsupported_operation(
                "This Live version does not expose get_notes_extended",
                {"clip_ref": clip_ref},
            )
        note_range = _note_range(clip, params)
        payload = clip.get_notes_extended(
            note_range["from_pitch"],
            note_range["pitch_span"],
            note_range["from_time"],
            note_range["time_span"],
        )
    elif hasattr(clip, "get_all_notes_extended"):
        payload = clip.get_all_notes_extended()
    else:
        raise unsupported_operation(
            "This Live version does not expose get_all_notes_extended",
            {"clip_ref": clip_ref},
        )
    notes = normalize_note_payload(payload)
    return {
        "clip_ref": clip_ref,
        "clip": serialize_clip(clip, clip_ref),
        "range": note_range,
        "notes": notes,
        "note_count": len(notes),
    }


def _note_field_visibility(notes):
    fields = ("velocity", "mute", "probability", "velocity_deviation", "release_velocity")
    return {field: any(field in note for note in notes) for field in fields}


def inspect_clip_notes(song, params, app=None):
    result = get_clip_notes(song, params, app=app)
    notes = result["notes"]
    field_visibility = _note_field_visibility(notes)
    result["field_visibility"] = field_visibility
    result["missing_fields"] = [
        field for field, visible in field_visibility.items() if not visible
    ]
    result["limitations"] = []
    if result["missing_fields"]:
        result["limitations"].append(
            {
                "code": "MIDI_NOTE_FIELDS_NOT_OBSERVED",
                "message": "Some extended MIDI note fields were not present in the returned notes.",
                "details": {"fields": result["missing_fields"]},
            }
        )
    return result


def get_audio_clip_warp_markers(song, params, app=None):
    clip_ref = params["clip_ref"]
    clip, clip_ref, _track, _track_ref, _clip_index = resolve_arrangement_clip(song, clip_ref)
    if not safe_get(clip, "is_audio_clip"):
        raise unsupported_operation(
            "Warp markers are only available for audio clips.",
            {"clip_ref": clip_ref, "clip_type": _clip_type(clip)},
        )
    raw_markers = safe_get(clip, "warp_markers")
    if raw_markers is None:
        raise unsupported_operation(
            "This Live version did not expose warp markers for the audio clip.",
            {"clip_ref": clip_ref, "clip_type": _clip_type(clip)},
        )
    markers = normalize_warp_markers(raw_markers)
    return {
        "clip_ref": clip_ref,
        "clip": serialize_clip(clip, clip_ref),
        "markers": markers,
        "marker_count": len(markers),
        "raw_marker_type": type(raw_markers).__name__,
    }
