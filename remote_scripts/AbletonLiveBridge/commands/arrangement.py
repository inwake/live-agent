from __future__ import annotations

from ..serializers import safe_get, serialize_clip


def get_arrangement_clips(song, params):
    target_ref = params.get("track_ref")
    tracks = list(safe_get(song, "tracks", []) or [])
    result = []
    for track_index, track in enumerate(tracks):
        track_ref = f"track:{track_index}"
        if target_ref and target_ref != track_ref:
            continue
        clips = list(safe_get(track, "arrangement_clips", []) or [])
        result.append({
            "track_ref": track_ref,
            "track_name": safe_get(track, "name"),
            "clips": [serialize_clip(clip, f"{track_ref}/arrangement_clip:{clip_index}") for clip_index, clip in enumerate(clips)],
        })
    return {"tracks": result}
