from __future__ import annotations

from ..protocol import err, ok
from .song import scan_song
from .arrangement import get_arrangement_clips
from .clips import get_clip_notes
from .devices import get_track_devices, get_device_parameters


class CommandRegistry:
    def __init__(self, song_getter):
        self.song_getter = song_getter
        self.handlers = {
            "song.scan": scan_song,
            "arrangement.get_clips": get_arrangement_clips,
            "clip.get_notes": get_clip_notes,
            "track.get_devices": get_track_devices,
            "device.get_parameters": get_device_parameters,
        }

    def handle(self, request):
        request_id = request.get("id")
        command_type = request.get("type")
        handler = self.handlers.get(command_type)
        if not handler:
            return err(request_id, "UNKNOWN_COMMAND", "Unknown command", {"type": command_type})
        try:
            result = handler(self.song_getter(), request.get("params") or {})
            return ok(request_id, result)
        except Exception as exc:
            return err(request_id, "LIVE_API_ERROR", str(exc), {"type": command_type})
