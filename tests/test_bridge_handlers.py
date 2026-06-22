from remote_scripts.AbletonLiveBridge.commands.song import scan_song
from remote_scripts.AbletonLiveBridge.commands.arrangement import get_arrangement_clips
from remote_scripts.AbletonLiveBridge.commands.clips import get_clip_notes
from remote_scripts.AbletonLiveBridge.commands.devices import get_track_devices, get_device_parameters
from tests.fake_live.fake_objects import FakeSong


def test_scan_song():
    result = scan_song(FakeSong(), {})
    assert result["tempo"] == 120.0
    assert result["tracks"][0]["name"] == "Bass"


def test_get_arrangement_clips():
    result = get_arrangement_clips(FakeSong(), {})
    assert result["tracks"][0]["clips"][0]["name"] == "Clip"


def test_get_clip_notes():
    result = get_clip_notes(FakeSong(), {"clip_ref": "track:0/arrangement_clip:0"})
    assert result["notes"][0]["pitch"] == 36


def test_get_devices_and_params():
    song = FakeSong()
    devices = get_track_devices(song, {"track_ref": "track:0"})
    assert devices["devices"][0]["name"] == "Serum"
    params = get_device_parameters(song, {"device_ref": "track:0/device:0"})
    assert params["parameters"][0]["name"] == "Cutoff"
