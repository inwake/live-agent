from remote_scripts.AbletonLiveBridge.commands.arrangement import get_arrangement_clips
from remote_scripts.AbletonLiveBridge.commands.clips import (
    get_audio_clip_warp_markers,
    get_clip_notes,
    inspect_clip_notes,
)
from remote_scripts.AbletonLiveBridge.commands.devices import (
    get_device_parameters,
    get_track_devices,
    inspect_device_tree,
    inspect_live_set_capabilities,
    inspect_parameter_exposure,
    inspect_track_detail,
)
from remote_scripts.AbletonLiveBridge.commands.registry import CommandRegistry
from remote_scripts.AbletonLiveBridge.commands.selection import get_selected_context
from remote_scripts.AbletonLiveBridge.commands.song import scan_song
from tests.fake_live.fake_objects import FakeApplication, FakeSong


def test_scan_song():
    result = scan_song(FakeSong(), {}, app=FakeApplication())
    assert result["tempo"] == 120.0
    assert result["application"]["version"] == "12.3.5"
    assert result["tracks"][0]["name"] == "Bass"
    assert result["tracks"][0]["kind"] == "midi"
    assert result["tracks"][1]["kind"] == "audio"
    assert result["return_tracks"][0]["ref"] == "return_track:0"
    assert result["master_track"]["ref"] == "master_track"


def test_get_arrangement_clips():
    result = get_arrangement_clips(FakeSong(), {})
    assert result["tracks"][0]["clips"][0]["name"] == "Clip"
    assert result["tracks"][1]["clips"][0]["file_path"] == "C:/Samples/loop.wav"


def test_get_arrangement_clips_filters_track():
    result = get_arrangement_clips(FakeSong(), {"track_ref": "track:1"})
    assert len(result["tracks"]) == 1
    assert result["tracks"][0]["track_ref"] == "track:1"
    assert result["tracks"][0]["clips"][0]["is_audio_clip"] is True


def test_get_clip_notes():
    result = get_clip_notes(FakeSong(), {"clip_ref": "track:0/arrangement_clip:0"})
    assert result["notes"][0]["pitch"] == 36
    assert result["notes"][0]["probability"] == 0.75
    assert result["notes"][0]["velocity_deviation"] == 7
    assert result["notes"][0]["release_velocity"] == 64
    assert result["note_count"] == 1


def test_get_clip_notes_with_range():
    song = FakeSong()
    result = get_clip_notes(
        song,
        {
            "clip_ref": "track:0/arrangement_clip:0",
            "from_time": 1.0,
            "time_span": 1.0,
            "from_pitch": 36,
            "pitch_span": 12,
        },
    )
    assert result["notes"][0]["pitch"] == 40
    assert result["range"]["from_time"] == 1.0
    assert song.midi_clip._last_note_range == {
        "from_pitch": 36,
        "pitch_span": 12,
        "from_time": 1.0,
        "time_span": 1.0,
    }


def test_inspect_clip_notes_reports_extended_field_visibility():
    result = inspect_clip_notes(FakeSong(), {"clip_ref": "track:0/arrangement_clip:0"})
    assert result["note_count"] == 1
    assert result["field_visibility"] == {
        "velocity": True,
        "mute": True,
        "probability": True,
        "velocity_deviation": True,
        "release_velocity": True,
    }


def test_get_audio_clip_warp_markers():
    result = get_audio_clip_warp_markers(FakeSong(), {"clip_ref": "track:1/arrangement_clip:0"})
    assert result["clip_ref"] == "track:1/arrangement_clip:0"
    assert result["markers"][1]["sample_time"] == 1.0
    assert result["markers"][1]["beat_time"] == 4.0


def test_get_devices_and_params():
    song = FakeSong()
    devices = get_track_devices(song, {"track_ref": "track:0"})
    assert devices["devices"][0]["name"] == "Serum"
    assert devices["devices"][0]["parameter_count"] == 2
    params = get_device_parameters(song, {"device_ref": "track:0/device:0"})
    assert params["parameters"][0]["name"] == "Cutoff"
    assert params["parameters"][0]["default_value"] == 0.25
    assert params["parameters"][0]["is_quantized"] is False


def test_inspect_device_tree_recurses_into_racks_drum_pads_and_samples():
    result = inspect_device_tree(FakeSong(), {"device_ref": "track:0/device:2"})
    tree = result["device_tree"]
    assert tree["class_display_name"] == "Drum Rack"
    assert tree["chain_count"] == 1
    assert tree["chains"] == []
    assert tree["drum_pad_count"] == 2
    assert tree["non_empty_drum_pad_count"] == 1
    assert tree["nested_device_count"] == 1
    assert tree["sample_count"] == 1
    pad = tree["drum_pads"][0]
    assert pad["name"] == "Kick"
    assert pad["note"] == 36
    chain = pad["chains"][0]
    assert chain["in_note"] == 36
    simpler = chain["devices"][0]
    assert simpler["class_display_name"] == "Simpler"
    assert simpler["sample"]["file_path"] == "C:/Samples/Kick.wav"
    assert simpler["sample"]["sample_rate"] == 48000


def test_inspect_device_tree_resolves_nested_device_refs():
    result = inspect_device_tree(
        FakeSong(),
        {"device_ref": "track:0/device:1/chain:0/device:0"},
    )
    assert result["device_tree"]["name"] == "Auto Filter"
    assert result["device_tree"]["parameter_count"] == 2


def test_inspect_track_detail_supports_return_and_master_tracks():
    song = FakeSong()
    return_detail = inspect_track_detail(song, {"track_ref": "return_track:0"})
    assert return_detail["track"]["kind"] == "return"
    assert return_detail["device_count"] == 1
    assert return_detail["exposed_parameter_count"] == 2
    master_detail = inspect_track_detail(song, {"track_ref": "master_track"})
    assert master_detail["track"]["kind"] == "master"
    assert master_detail["devices"][0]["name"] == "Limiter"
    assert master_detail["exposed_parameter_count"] == 2


def test_inspect_parameter_exposure_counts_plugins_native_devices_and_tracks():
    result = inspect_parameter_exposure(FakeSong(), {})
    assert result["totals"]["plugin_device_count"] == 1
    assert result["totals"]["native_device_count"] >= 5
    assert result["totals"]["exposed_parameter_count"] >= 12
    assert result["tracks"][0]["track_ref"] == "track:0"
    assert result["tracks"][0]["exposed_parameter_count"] >= 8
    plugin = result["plugin_devices"][0]
    assert plugin["device"] == "Serum"
    assert plugin["exposure_status"] == "minimal_or_preconfigured"
    native_names = {entry["device"] for entry in result["native_devices"]}
    assert "Auto Filter" in native_names
    assert "Limiter" in native_names


def test_inspect_live_set_capabilities_summarizes_read_only_visibility():
    result = inspect_live_set_capabilities(FakeSong(), {}, app=FakeApplication())
    assert result["set_summary"]["return_track_count"] == 1
    assert result["set_summary"]["master_track_visible"] is True
    assert result["set_summary"]["midi_clip_count"] == 1
    assert result["set_summary"]["audio_clip_count"] == 1
    assert result["parameter_exposure"]["totals"]["plugin_device_count"] == 1
    drum_rack = next(rack for rack in result["rack_depth"] if rack["rack"] == "Drum Rack")
    assert drum_rack["drum_pads"] == 2
    assert result["midi_note_visibility"][0]["velocity_visible"] is True
    assert result["midi_note_visibility"][0]["probability_visible"] is True
    limitation_codes = {item["code"] for item in result["limitations_observed"]}
    assert "HIDDEN_PLUGIN_PARAMETERS_UNAVAILABLE" in limitation_codes
    assert "RENDERED_WAVEFORMS_UNAVAILABLE" in limitation_codes


def test_get_selected_context():
    result = get_selected_context(FakeSong(), {})
    assert result["selected_track"]["ref"] == "track:0"
    assert result["detail_clip"]["ref"] == "track:0/arrangement_clip:0"
    assert result["selected_device"]["ref"] == "track:0/device:0"
    assert result["selected_parameter"]["ref"] == "track:0/device:0/parameter:0"


def test_registry_returns_typed_unsupported_error():
    registry = CommandRegistry(song_getter=FakeSong)
    response = registry.handle(
        {
            "id": "req_1",
            "type": "clip.get_notes",
            "params": {"clip_ref": "track:1/arrangement_clip:0"},
        }
    )
    assert response["ok"] is False
    assert response["error"]["code"] == "UNSUPPORTED_LOM_OPERATION"
    assert response["error"]["details"]["clip_type"] == "audio"


def test_registry_returns_typed_not_found_error():
    registry = CommandRegistry(song_getter=FakeSong)
    response = registry.handle(
        {"id": "req_1", "type": "track.get_devices", "params": {"track_ref": "track:99"}}
    )
    assert response["ok"] is False
    assert response["error"]["code"] == "OBJECT_NOT_FOUND"


def test_registry_scan_includes_application_metadata():
    registry = CommandRegistry(song_getter=FakeSong, app_getter=FakeApplication)
    response = registry.handle({"id": "req_1", "type": "song.scan", "params": {}})
    assert response["ok"] is True
    assert response["result"]["application"]["version"] == "12.3.5"


def test_registry_exposes_capability_inspection_commands():
    registry = CommandRegistry(song_getter=FakeSong, app_getter=FakeApplication)
    response = registry.handle({"id": "req_1", "type": "set.inspect_capabilities", "params": {}})
    assert response["ok"] is True
    assert response["result"]["set_summary"]["name"] == "Test Set"
    response = registry.handle(
        {
            "id": "req_2",
            "type": "device.inspect_tree",
            "params": {"device_ref": "track:0/device:2"},
        }
    )
    assert response["ok"] is True
    assert response["result"]["device_tree"]["class_display_name"] == "Drum Rack"
