from __future__ import annotations

from ..errors import BridgeCommandError
from ..protocol import err, ok
from .song import scan_song
from .arrangement import get_arrangement_clips
from .clips import get_audio_clip_warp_markers, get_clip, get_clip_notes
from .devices import get_track_devices, get_device_parameters
from .selection import get_selected_context


class CommandRegistry:
    def __init__(self, song_getter, app_getter=None):
        self.song_getter = song_getter
        self.app_getter = app_getter or (lambda: None)
        self.handlers = {
            "song.scan": scan_song,
            "arrangement.get_clips": get_arrangement_clips,
            "clip.get": get_clip,
            "clip.get_notes": get_clip_notes,
            "clip.get_warp_markers": get_audio_clip_warp_markers,
            "track.get_devices": get_track_devices,
            "device.get_parameters": get_device_parameters,
            "selection.get_context": get_selected_context,
        }

    def handle(self, request):
        request_id = request.get("id")
        command_type = request.get("type")
        handler = self.handlers.get(command_type)
        if not handler:
            return err(request_id, "UNKNOWN_COMMAND", "Unknown command", {"type": command_type})
        try:
            result = handler(self.song_getter(), request.get("params") or {}, app=self.app_getter())
            return ok(request_id, result)
        except BridgeCommandError as exc:
            return err(request_id, exc.code, exc.message, exc.details)
        except Exception as exc:
            return err(request_id, "LIVE_API_ERROR", str(exc), {"type": command_type})
