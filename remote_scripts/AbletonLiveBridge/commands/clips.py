from __future__ import annotations

from ..serializers import safe_get


def _resolve_arrangement_clip(song, clip_ref):
    # v0 resolver: track:N/arrangement_clip:M
    parts = clip_ref.split("/")
    track_index = int(parts[0].split(":", 1)[1])
    clip_index = int(parts[1].split(":", 1)[1])
    track = list(song.tracks)[track_index]
    return list(track.arrangement_clips)[clip_index]


def get_clip_notes(song, params):
    clip_ref = params["clip_ref"]
    clip = _resolve_arrangement_clip(song, clip_ref)
    if not safe_get(clip, "is_midi_clip"):
        raise RuntimeError("Clip is not a MIDI clip; note APIs are unavailable")
    if hasattr(clip, "get_all_notes_extended"):
        return {"clip_ref": clip_ref, "notes": clip.get_all_notes_extended()}
    # Fallback intentionally narrow; Codex should improve with real Live testing.
    raise RuntimeError("This Live version does not expose get_all_notes_extended in the bridge fallback yet")
