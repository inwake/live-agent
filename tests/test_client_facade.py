from __future__ import annotations

from ableton_live_client.orm import LiveSet


class RecordingClient:
    def __init__(self):
        self.calls = []

    def call(self, command_type, **params):
        self.calls.append((command_type, params))
        return {"command_type": command_type, "params": params}


def test_live_set_facade_exposes_v01_read_commands():
    client = RecordingClient()
    live_set = LiveSet(client)

    assert live_set.scan()["command_type"] == "song.scan"
    assert live_set.arrangement_clips("track:0")["params"] == {"track_ref": "track:0"}
    assert live_set.clip("track:0/arrangement_clip:0")["command_type"] == "clip.get"
    assert live_set.clip_notes("track:0/arrangement_clip:0")["command_type"] == "clip.get_notes"
    assert (
        live_set.audio_clip_warp_markers("track:1/arrangement_clip:0")["command_type"]
        == "clip.get_warp_markers"
    )
    assert live_set.devices("track:0")["command_type"] == "track.get_devices"
    assert live_set.device_parameters("track:0/device:0")["command_type"] == "device.get_parameters"
    assert live_set.selected_context()["command_type"] == "selection.get_context"
