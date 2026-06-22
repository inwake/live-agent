from __future__ import annotations

from ..serializers import serialize_track, safe_get


def scan_song(song, params):
    tracks = list(safe_get(song, "tracks", []) or [])
    return_tracks = list(safe_get(song, "return_tracks", []) or [])
    return {
        "tempo": safe_get(song, "tempo"),
        "current_song_time": safe_get(song, "current_song_time"),
        "is_playing": safe_get(song, "is_playing"),
        "signature_numerator": safe_get(song, "signature_numerator"),
        "signature_denominator": safe_get(song, "signature_denominator"),
        "tracks": [serialize_track(track, i) for i, track in enumerate(tracks)],
        "return_tracks": [serialize_track(track, i) for i, track in enumerate(return_tracks)],
    }
