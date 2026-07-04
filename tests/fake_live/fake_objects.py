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


class FakeSample:
    def __init__(self, file_path="C:/Samples/Kick.wav"):
        self.file_path = file_path
        self.length = 48000
        self.sample_rate = 48000
        self.slices = [0, 24000]
        self.start_marker = 0
        self.end_marker = 48000
        self.warp_markers = [
            {"sample_time": 0.0, "beat_time": 0.0},
            {"sample_time": 1.0, "beat_time": 1.0},
        ]
        self.warp_mode = 0
        self.warping = True
        self.slicing_style = 0
        self.slicing_beat_division = 0
        self.slicing_region_count = 0


class FakeChain:
    def __init__(self, name, devices=None, in_note=None, out_note=None, choke_group=None):
        self.name = name
        self.color = 255
        self.color_index = 1
        self.is_auto_colored = False
        self.has_audio_input = True
        self.has_audio_output = True
        self.has_midi_input = True
        self.has_midi_output = True
        self.mute = False
        self.muted_via_solo = False
        self.solo = False
        self.devices = devices or []
        self.mixer_device = None
        if in_note is not None:
            self.in_note = in_note
        if out_note is not None:
            self.out_note = out_note
        if choke_group is not None:
            self.choke_group = choke_group


class FakeDrumPad:
    def __init__(self, name, note, chains=None):
        self.name = name
        self.note = note
        self.mute = False
        self.solo = False
        self.chains = chains or []


class FakeDevice:
    def __init__(
        self,
        name,
        parameters=None,
        class_name="PluginDevice",
        class_display_name=None,
        can_have_chains=False,
        can_have_drum_pads=False,
        chains=None,
        return_chains=None,
        drum_pads=None,
        visible_drum_pads=None,
        sample=None,
    ):
        self.name = name
        self.class_name = class_name
        self.class_display_name = class_display_name or ("Plugin" if class_name == "PluginDevice" else name)
        self.is_active = True
        self.can_have_chains = can_have_chains
        self.can_have_drum_pads = can_have_drum_pads
        self.type = 1
        self.latency_in_samples = 0
        self.latency_in_ms = 0.0
        self.parameters = parameters or []
        self.chains = chains or []
        self.return_chains = return_chains or []
        self.drum_pads = drum_pads or []
        self.visible_drum_pads = visible_drum_pads or self.drum_pads[:16]
        if sample is not None:
            self.sample = sample


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
                    "probability": 0.75,
                    "velocity_deviation": 7,
                    "release_velocity": 64,
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
                    "probability": 1.0,
                    "velocity_deviation": 0,
                    "release_velocity": 48,
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
        resonance = FakeParameter("Resonance", 0.1, default_value=0.0)
        rack_macro = FakeParameter("Macro 1", 0.7, default_value=0.0)
        kick_sample = FakeSample("C:/Samples/Kick.wav")
        simpler = FakeDevice(
            "Kick Simpler",
            [FakeParameter("Volume", 0.8, default_value=0.75)],
            class_name="OriginalSimpler",
            class_display_name="Simpler",
            sample=kick_sample,
        )
        kick_chain = FakeChain(
            "Kick Chain",
            devices=[simpler],
            in_note=36,
            out_note=36,
            choke_group=1,
        )
        drum_pad = FakeDrumPad(
            "Kick",
            36,
            chains=[kick_chain],
        )
        empty_pad = FakeDrumPad("Closed Hat", 42)
        self.drum_rack = FakeDevice(
            "Drum Rack",
            [rack_macro],
            class_name="DrumGroupDevice",
            class_display_name="Drum Rack",
            can_have_chains=True,
            can_have_drum_pads=True,
            chains=[kick_chain],
            drum_pads=[drum_pad, empty_pad],
            visible_drum_pads=[drum_pad, empty_pad],
        )
        nested_filter = FakeDevice(
            "Auto Filter",
            [cutoff, resonance],
            class_name="AutoFilter",
            class_display_name="Auto Filter",
        )
        self.instrument_rack = FakeDevice(
            "Bass Rack",
            [rack_macro],
            class_name="InstrumentGroupDevice",
            class_display_name="Instrument Rack",
            can_have_chains=True,
            chains=[FakeChain("Bass Layer", devices=[nested_filter])],
            return_chains=[FakeChain("Rack Verb", devices=[FakeDevice("Echo", [FakeParameter("Dry/Wet", 0.2)], class_name="Echo")])],
        )
        self.device = FakeDevice("Serum", [cutoff, resonance])
        self.tracks = [
            FakeTrack("Bass", arrangement_clips=[self.midi_clip], devices=[self.device, self.instrument_rack, self.drum_rack]),
            FakeTrack(
                "Vox",
                arrangement_clips=[self.audio_clip],
                devices=[],
                has_midi_input=False,
                has_audio_input=True,
            ),
        ]
        self.return_tracks = [
            FakeTrack(
                "Reverb Return",
                devices=[
                    FakeDevice(
                        "Hybrid Reverb",
                        [FakeParameter("Decay", 0.4), FakeParameter("Dry/Wet", 0.25)],
                        class_name="HybridReverb",
                        class_display_name="Hybrid Reverb",
                    )
                ],
                has_midi_input=False,
                has_audio_input=True,
            )
        ]
        self.master_track = FakeTrack(
            "Master",
            devices=[
                FakeDevice(
                    "Limiter",
                    [FakeParameter("Ceiling", -0.3, min=-70.0, max=6.0), FakeParameter("Gain", 0.0, min=-35.0, max=35.0)],
                    class_name="Limiter",
                    class_display_name="Limiter",
                )
            ],
            has_midi_input=False,
            has_audio_input=False,
        )
        self.view = FakeSongView(
            selected_track=self.tracks[0],
            detail_clip=self.midi_clip,
            selected_parameter=cutoff,
        )
