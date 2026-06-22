from __future__ import annotations


class FakeParameter:
    def __init__(self, name, value=0.0, min=0.0, max=1.0):
        self.name = name
        self.original_name = name
        self.value = value
        self.display_value = str(value)
        self.min = min
        self.max = max
        self.is_enabled = True
        self.automation_state = 0


class FakeDevice:
    def __init__(self, name, parameters=None):
        self.name = name
        self.class_name = "PluginDevice"
        self.class_display_name = "Plugin"
        self.is_active = True
        self.parameters = parameters or []


class FakeClip:
    def __init__(self, name="Clip", notes=None):
        self.name = name
        self.is_midi_clip = True
        self.is_audio_clip = False
        self.is_arrangement_clip = True
        self.start_time = 0.0
        self.end_time = 4.0
        self.length = 4.0
        self.looping = False
        self.loop_start = 0.0
        self.loop_end = 4.0
        self._notes = notes or []

    def get_all_notes_extended(self):
        return self._notes


class FakeTrack:
    def __init__(self, name="Track", arrangement_clips=None, devices=None):
        self.name = name
        self.mute = False
        self.solo = False
        self.arm = False
        self.arrangement_clips = arrangement_clips or []
        self.devices = devices or []


class FakeSong:
    def __init__(self):
        self.tempo = 120.0
        self.current_song_time = 0.0
        self.is_playing = False
        self.signature_numerator = 4
        self.signature_denominator = 4
        self.tracks = [
            FakeTrack(
                "Bass",
                arrangement_clips=[FakeClip(notes=[{"pitch": 36, "start_time": 0.0, "duration": 0.5, "velocity": 100, "mute": False}])],
                devices=[FakeDevice("Serum", [FakeParameter("Cutoff", 0.5)])],
            )
        ]
        self.return_tracks = []
