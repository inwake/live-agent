from __future__ import annotations


class FakeApplication:
    def get_version_string(self):
        return "12.3.5"

    def get_major_version(self):
        return 12

    def get_minor_version(self):
        return 3

    def get_bugfix_version(self):
        return 5


class FakeParameter:
    def __init__(
        self,
        name,
        value=0.0,
        min=0.0,
        max=1.0,
        default_value=0.0,
        is_quantized=False,
        value_items=None,
    ):
        self.name = name
        self.original_name = name
        self.value = value
        self.display_value = str(value)
        self.min = min
        self.max = max
        self.default_value = default_value
        self.is_enabled = True
        self.is_quantized = is_quantized
        self.value_items = value_items or []
        self.automation_state = 0
        self.state = 0


class FakeDevice:
    def __init__(self, name, parameters=None, class_name="PluginDevice"):
        self.name = name
        self.class_name = class_name
        self.class_display_name = "Plugin"
        self.is_active = True
        self.can_have_chains = False
        self.can_have_drum_pads = False
        self.type = 1
        self.latency_in_samples = 0
        self.latency_in_ms = 0.0
        self.parameters = parameters or []


class FakeClip:
    def __init__(
        self,
        name="Clip",
        notes=None,
        ranged_notes=None,
        is_midi_clip=True,
        is_audio_clip=False,
        warp_markers=None,
    ):
        self.name = name
        self.is_midi_clip = is_midi_clip
        self.is_audio_clip = is_audio_clip
        self.is_arrangement_clip = True
        self.start_time = 0.0
        self.end_time = 4.0
        self.length = 4.0
        self.looping = False
        self.loop_start = 0.0
        self.loop_end = 4.0
        self.file_path = "C:/Samples/loop.wav" if is_audio_clip else ""
        self.sample_length = 192000 if is_audio_clip else 0
        self.sample_rate = 48000.0 if is_audio_clip else 0.0
        self.warping = is_audio_clip
        self.warp_mode = 2 if is_audio_clip else None
        self.gain = 1.0
        self._notes = notes or []
        self._ranged_notes = ranged_notes or []
        self._last_note_range = None
        self.warp_markers = warp_markers or []

    def get_all_notes_extended(self):
        return {"notes": self._notes}

    def get_notes_extended(self, from_pitch, pitch_span, from_time, time_span):
        self._last_note_range = {
            "from_pitch": from_pitch,
            "pitch_span": pitch_span,
            "from_time": from_time,
            "time_span": time_span,
        }
        return {"notes": self._ranged_notes}


class FakeTrackView:
    def __init__(self, selected_device=None):
        self.selected_device = selected_device


class FakeTrack:
    def __init__(
        self,
        name="Track",
        arrangement_clips=None,
        devices=None,
        has_midi_input=True,
        has_audio_input=False,
    ):
        self.name = name
        self.mute = False
        self.solo = False
        self.arm = False
        self.can_be_armed = True
        self.color = 16711680
        self.color_index = 3
        self.is_frozen = False
        self.has_midi_input = has_midi_input
        self.has_midi_output = has_midi_input
        self.has_audio_input = has_audio_input
        self.has_audio_output = has_audio_input or has_midi_input
        self.arrangement_clips = arrangement_clips or []
        self.devices = devices or []
        self.view = FakeTrackView(self.devices[0] if self.devices else None)


class FakeSongView:
    def __init__(self, selected_track=None, detail_clip=None, selected_parameter=None):
        self.selected_track = selected_track
        self.detail_clip = detail_clip
        self.selected_parameter = selected_parameter
        self.selected_chain = None
        self.highlighted_clip_slot = None


class FakeSong:
    def __init__(self):
        self.tempo = 120.0
        self.current_song_time = 0.0
        self.is_playing = False
        self.signature_numerator = 4
        self.signature_denominator = 4
        self.file_path = "C:/Live Sets/Test.als"
        self.name = "Test Set"
        self.loop = False
        self.loop_start = 0.0
        self.loop_length = 8.0
        cutoff = FakeParameter("Cutoff", 0.5, default_value=0.25)
        self.midi_clip = FakeClip(
            notes=[
                {
                    "note_id": 1,
                    "pitch": 36,
                    "start_time": 0.0,
                    "duration": 0.5,
                    "velocity": 100,
                    "mute": False,
                }
            ],
            ranged_notes=[
                {
                    "note_id": 2,
                    "pitch": 40,
                    "start_time": 1.0,
                    "duration": 0.25,
                    "velocity": 90,
                    "mute": False,
                }
            ],
        )
        self.audio_clip = FakeClip(
            "Audio Loop",
            is_midi_clip=False,
            is_audio_clip=True,
            warp_markers=[
                {"sample_time": 0.0, "beat_time": 0.0},
                {"sample_time": 1.0, "beat_time": 4.0},
            ],
        )
        self.device = FakeDevice("Serum", [cutoff])
        self.tracks = [
            FakeTrack("Bass", arrangement_clips=[self.midi_clip], devices=[self.device]),
            FakeTrack(
                "Vox",
                arrangement_clips=[self.audio_clip],
                devices=[],
                has_midi_input=False,
                has_audio_input=True,
            ),
        ]
        self.return_tracks = [FakeTrack("Reverb Return", has_midi_input=False, has_audio_input=True)]
        self.master_track = FakeTrack("Master", has_midi_input=False, has_audio_input=False)
        self.view = FakeSongView(
            selected_track=self.tracks[0],
            detail_clip=self.midi_clip,
            selected_parameter=cutoff,
        )
