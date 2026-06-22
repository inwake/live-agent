from __future__ import annotations

from ..serializers import safe_get, serialize_clip
from .resolvers import resolve_track


def _track_arrangement_payload(track, track_ref):
    clips = list(safe_get(track, "arrangement_clips", []) or [])
    return {
            "track_ref": track_ref,
            "track_name": safe_get(track, "name"),
            "clip_count": len(clips),
            "clips": [
                serialize_clip(clip, "%s/arrangement_clip:%d" % (track_ref, clip_index))
                for clip_index, clip in enumerate(clips)
            ],
        }


def get_arrangement_clips(song, params, app=None):
    target_ref = params.get("track_ref")
    result = []
    if target_ref:
        track, track_ref, _index, _kind = resolve_track(song, target_ref)
        result.append(_track_arrangement_payload(track, track_ref))
        return {"tracks": result}
    tracks = list(safe_get(song, "tracks", []) or [])
    for track_index, track in enumerate(tracks):
        result.append(_track_arrangement_payload(track, "track:%d" % track_index))
    return {"tracks": result}
