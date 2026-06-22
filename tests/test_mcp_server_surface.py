from __future__ import annotations

from ableton_mcp_server import server


class FakeLiveSet:
    def scan(self):
        return {
            "application": {"version": "12.3.5"},
            "tempo": 120.0,
            "current_song_time": 8.0,
            "is_playing": False,
            "tracks": [{"ref": "track:0", "name": "Bass"}],
        }

    def arrangement_clips(self, track_ref=None):
        return {"track_ref": track_ref, "tracks": [{"track_ref": track_ref, "clips": []}]}

    def clip(self, clip_ref):
        return {"clip": {"ref": clip_ref}}

    def clip_notes(self, clip_ref, **ranges):
        return {"clip_ref": clip_ref, "ranges": ranges}

    def audio_clip_warp_markers(self, clip_ref):
        return {"clip_ref": clip_ref, "markers": []}

    def devices(self, track_ref):
        return {"track_ref": track_ref, "devices": []}

    def device_parameters(self, device_ref):
        return {"device_ref": device_ref, "parameters": []}

    def selected_context(self):
        return {"selected_track": {"ref": "track:0"}}


def test_mcp_tools_delegate_to_live_set(monkeypatch):
    monkeypatch.setattr(server, "live_set", FakeLiveSet())

    assert server.get_audio_clip_warp_markers("track:1/arrangement_clip:0")["markers"] == []
    assert server.get_selected_context()["selected_track"]["ref"] == "track:0"
    assert server.get_clip_notes("track:0/arrangement_clip:0", from_time=1.0)["ranges"][
        "from_time"
    ] == 1.0


def test_mcp_resources_delegate_to_live_set(monkeypatch):
    monkeypatch.setattr(server, "live_set", FakeLiveSet())

    assert server.live_version_resource()["version"] == "12.3.5"
    assert server.set_summary_resource()["tracks"][0]["name"] == "Bass"
    assert server.set_transport_resource()["tempo"] == 120.0
    assert server.tracks_resource()["tracks"][0]["ref"] == "track:0"
    assert server.track_resource("track:0")["ref"] == "track:0"
    assert server.track_arrangement_resource("track:0")["track_ref"] == "track:0"
    assert server.track_devices_resource("track:0")["track_ref"] == "track:0"
    assert server.clip_resource("track:0/arrangement_clip:0")["clip"]["ref"] == "track:0/arrangement_clip:0"
    assert (
        server.clip_notes_resource("track:0/arrangement_clip:0")["clip_ref"]
        == "track:0/arrangement_clip:0"
    )
    assert server.clip_warp_resource("track:1/arrangement_clip:0")["markers"] == []
    assert server.selection_resource()["selected_track"]["ref"] == "track:0"
