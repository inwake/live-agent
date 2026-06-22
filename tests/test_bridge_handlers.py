from remote_scripts.AbletonLiveBridge.commands.arrangement import get_arrangement_clips
from remote_scripts.AbletonLiveBridge.commands.clips import (
    get_audio_clip_warp_markers,
    get_clip_notes,
)
from remote_scripts.AbletonLiveBridge.commands.devices import get_track_devices, get_device_parameters
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


def test_get_audio_clip_warp_markers():
    result = get_audio_clip_warp_markers(FakeSong(), {"clip_ref": "track:1/arrangement_clip:0"})
    assert result["clip_ref"] == "track:1/arrangement_clip:0"
    assert result["markers"][1]["sample_time"] == 1.0
    assert result["markers"][1]["beat_time"] == 4.0


def test_get_devices_and_params():
    song = FakeSong()
    devices = get_track_devices(song, {"track_ref": "track:0"})
    assert devices["devices"][0]["name"] == "Serum"
    assert devices["devices"][0]["parameter_count"] == 1
    params = get_device_parameters(song, {"device_ref": "track:0/device:0"})
    assert params["parameters"][0]["name"] == "Cutoff"
    assert params["parameters"][0]["default_value"] == 0.25
    assert params["parameters"][0]["is_quantized"] is False


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
