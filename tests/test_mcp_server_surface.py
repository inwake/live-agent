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

    def inspect_capabilities(self):
        return {
            "set_summary": {
                "name": "Test Set",
                "tempo": 120.0,
                "signature": "4/4",
                "track_count": 1,
                "return_track_count": 1,
                "master_track_visible": True,
                "arrangement_clip_count": 1,
                "midi_clip_count": 1,
                "audio_clip_count": 0,
            },
            "return_tracks": [
                {"ref": "return_track:0", "name": "A-Reverb", "device_count": 1, "exposed_parameter_count": 2}
            ],
            "tracks": [
                {
                    "ref": "track:0",
                    "name": "Bass",
                    "kind": "midi",
                    "arrangement_clip_count": 1,
                    "device_count": 1,
                    "exposed_parameter_count": 2,
                }
            ],
            "parameter_exposure": {
                "plugin_devices": [
                    {
                        "track": "Bass",
                        "device": "Serum",
                        "class_name": "PluginDevice",
                        "exposed_parameter_count": 2,
                        "notes": "Live exposes 2 DeviceParameter object(s).",
                    }
                ],
                "native_devices": [
                    {
                        "track": "Bass",
                        "device": "Auto Filter",
                        "class_name": "AutoFilter",
                        "exposed_parameter_count": 2,
                        "example_parameters": ["Cutoff", "Resonance"],
                    }
                ],
            },
            "rack_depth": [
                {
                    "track": "Bass",
                    "rack": "Drum Rack",
                    "depth": 0,
                    "chains": 1,
                    "drum_pads": 16,
                    "nested_devices": 1,
                    "samples_found": 1,
                }
            ],
            "midi_note_visibility": [
                {
                    "clip": "Beat",
                    "note_count": 4,
                    "velocity_visible": True,
                    "probability_visible": True,
                    "velocity_deviation_visible": True,
                    "release_velocity_visible": True,
                }
            ],
            "limitations_observed": [
                {"code": "HIDDEN_PLUGIN_PARAMETERS_UNAVAILABLE", "message": "Only exposed parameters are visible."}
            ],
        }

    def inspect_track_detail(self, track_ref):
        return {"track": {"ref": track_ref}, "devices": []}

    def inspect_device_tree(self, device_ref):
        return {"device_ref": device_ref, "device_tree": {"ref": device_ref}}

    def inspect_clip_notes(self, clip_ref, **ranges):
        return {"clip_ref": clip_ref, "ranges": ranges, "field_visibility": {"velocity": True}}

    def inspect_parameter_exposure(self):
        return {"totals": {"exposed_parameter_count": 2}, "plugin_devices": [], "native_devices": []}


def test_mcp_tools_delegate_to_live_set(monkeypatch):
    monkeypatch.setattr(server, "live_set", FakeLiveSet())

    assert server.get_audio_clip_warp_markers("track:1/arrangement_clip:0")["markers"] == []
    assert server.get_selected_context()["selected_track"]["ref"] == "track:0"
    assert server.get_clip_notes("track:0/arrangement_clip:0", from_time=1.0)["ranges"][
        "from_time"
    ] == 1.0
    assert server.inspect_live_set_capabilities()["set_summary"]["name"] == "Test Set"
    assert server.inspect_track_detail("return_track:0")["track"]["ref"] == "return_track:0"
    assert server.inspect_device_tree("track:0/device:0")["device_ref"] == "track:0/device:0"
    assert server.inspect_clip_notes("track:0/arrangement_clip:0")["field_visibility"]["velocity"] is True
    assert server.inspect_parameter_exposure()["totals"]["exposed_parameter_count"] == 2
    report = server.generate_capability_report()
    assert "# Live Set Capability Report" in report["markdown"]
    assert "Hidden plugin parameters" in report["markdown"]


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
    assert server.set_capabilities_resource()["set_summary"]["name"] == "Test Set"
    assert server.track_detail_resource("track:0")["track"]["ref"] == "track:0"
    assert server.device_tree_resource("track:0/device:0")["device_tree"]["ref"] == "track:0/device:0"
    assert server.parameter_exposure_resource()["totals"]["exposed_parameter_count"] == 2
