from __future__ import annotations

from ..serializers import safe_call, safe_get, serialize_track


def _application_metadata(app):
    if app is None:
        return {}
    return {
        "version": safe_call(app, "get_version_string"),
        "major_version": safe_call(app, "get_major_version"),
        "minor_version": safe_call(app, "get_minor_version"),
        "bugfix_version": safe_call(app, "get_bugfix_version"),
    }


def scan_song(song, params, app=None):
    tracks = list(safe_get(song, "tracks", []) or [])
    return_tracks = list(safe_get(song, "return_tracks", []) or [])
    master_track = safe_get(song, "master_track")
    return {
        "application": _application_metadata(app),
        "name": safe_get(song, "name"),
        "file_path": safe_get(song, "file_path"),
        "tempo": safe_get(song, "tempo"),
        "current_song_time": safe_get(song, "current_song_time"),
        "is_playing": safe_get(song, "is_playing"),
        "loop": safe_get(song, "loop"),
        "loop_start": safe_get(song, "loop_start"),
        "loop_length": safe_get(song, "loop_length"),
        "signature_numerator": safe_get(song, "signature_numerator"),
        "signature_denominator": safe_get(song, "signature_denominator"),
        "track_count": len(tracks),
        "return_track_count": len(return_tracks),
        "tracks": [serialize_track(track, i, ref="track:%d" % i) for i, track in enumerate(tracks)],
        "return_tracks": [
            serialize_track(track, i, ref="return_track:%d" % i, kind="return")
            for i, track in enumerate(return_tracks)
        ],
        "master_track": serialize_track(master_track, None, ref="master_track", kind="master")
        if master_track is not None
        else None,
    }
