# LOM_INDEX_FOR_CODEX
Generated from the Firecrawl markdown export of Cycling '74 Live Object Model docs. This is a compact navigation/index file for Codex so it does not have to read every full LOM page for basic planning.
## Project focus
- Arrangement-first Ableton Live MCP server.
- Help an experienced producer understand the state of a Live set.
- Prioritize tracks, Arrangement clips, MIDI notes, audio/warp metadata, device chains, and exposed DeviceParameter values.
- Do not claim full arbitrary VST3 parameter access.
## Highest-value LOM APIs for this project
### Song
- Source: `song.md`
- Canonical paths:
  - `live_set`
- Target members:
  - `tracks`
  - `return_tracks`
  - `master_track`
  - `view`
  - `current_song_time`
  - `tempo`
  - `signature_numerator`
  - `signature_denominator`
  - `create_midi_track`
  - `create_audio_track`
  - `capture_midi`

### Track
- Source: `track.md`
- Canonical paths:
  - `live_set tracks N`
- Target members:
  - `arrangement_clips`
  - `clip_slots`
  - `devices`
  - `mixer_device`
  - `create_midi_clip`
  - `create_audio_clip`
  - `duplicate_clip_to_arrangement`
  - `delete_clip`
  - `delete_device`

### Clip
- Source: `clip.md`
- Canonical paths:
  - `live_set tracks N clip_slots M clip`
  - `live_set tracks N arrangement_clips M`
- Target members:
  - `is_arrangement_clip`
  - `is_audio_clip`
  - `is_midi_clip`
  - `start_time`
  - `end_time`
  - `length`
  - `loop_start`
  - `loop_end`
  - `get_all_notes_extended`
  - `get_notes_extended`
  - `add_new_notes`
  - `apply_note_modifications`
  - `warp_markers`
  - `add_warp_marker`
  - `move_warp_marker`
  - `remove_warp_marker`

### Device
- Source: `device.md`
- Canonical paths:
  - `live_set tracks N devices M`
  - `live_set tracks N devices M chains L devices K`
  - `live_set tracks N devices M return_chains L devices K`
- Target members:
  - `parameters`
  - `class_name`
  - `class_display_name`
  - `name`
  - `is_active`

### DeviceParameter
- Source: `deviceparameter.md`
- Canonical paths:
  - `live_set tracks N devices M parameters L`
- Target members:
  - `name`
  - `original_name`
  - `value`
  - `display_value`
  - `min`
  - `max`
  - `default_value`
  - `automation_state`
  - `is_enabled`
  - `is_quantized`
  - `value_items`

### PluginDevice
- Source: `plugindevice.md`
- Target members:
  - `presets`
  - `selected_preset_index`

### Song.View
- Source: `song_view.md`
- Canonical paths:
  - `live_set view`
- Target members:
  - `selected_track`
  - `selected_scene`
  - `selected_parameter`
  - `selected_device`
  - `selected_chain`
  - `highlighted_clip_slot`

### Application.View
- Source: `application_view.md`
- Canonical paths:
  - `live_app view`
- Target members:
  - `focused_document_view`
  - `show_view`
  - `focus_view`
  - `is_view_visible`
  - `zoom_view`
  - `scroll_view`

## Class index
### Application
- File: `application.md`
- Source URL: https://docs.cycling74.com/apiref/lom/application/
- Description: This class represents the Live application. It is reachable by the root path `live_app`.
- Canonical paths:
  - `live_app`
- Children (2): `view [Application.View](https://docs.cycling74.com/apiref/lom/application_view/ "Application.View")read-only`, `control_surfaces list of [ControlSurface](https://docs.cycling74.com/apiref/lom/controlsurface/ "ControlSurface")read-onlyobserve`
- Properties (5): `current_dialog_button_count intread-only`, `current_dialog_message symbolread-only`, `open_dialog_count intread-onlyobserve`, `average_process_usage floatread-onlyobserve`, `peak_process_usage floatread-onlyobserve`
- Functions (6): `get_bugfix_version`, `get_document`, `get_major_version`, `get_minor_version`, `get_version_string`, `press_current_dialog_button`

### Application.View
- File: `application_view.md`
- Source URL: https://docs.cycling74.com/apiref/lom/application_view/
- Description: This class represents the aspects of the Live application related to viewing the application.
- Canonical paths:
  - `live_app view`
- Properties (2): `browse_mode boolread-onlyobserve`, `focused_document_view unicoderead-onlyobserve`
- Functions (8): `available_main_views`, `focus_view`, `hide_view`, `is_view_visible`, `scroll_view`, `show_view`, `toggle_browse`, `zoom_view`

### Chain
- File: `chain.md`
- Source URL: https://docs.cycling74.com/apiref/lom/chain/
- Description: This class represents a group device chain in Live.
- Canonical paths:
  - `live_set tracks N devices M chains L`
  - `live_set tracks N devices M return_chains L`
  - `live_set tracks N devices M chains L devices K chains P ...`
  - `live_set tracks N devices M return_chains L devices K chains P ...`
- Children (2): `devices [Device](https://docs.cycling74.com/apiref/lom/device/ "Device")read-onlyobserve`, `mixer_device [ChainMixerDevice](https://docs.cycling74.com/apiref/lom/chainmixerdevice/ "ChainMixerDevice")read-only`
- Properties (11): `color intobserve`, `color_index longobserve`, `is_auto_colored boolobserve`, `has_audio_input boolread-only`, `has_audio_output boolread-only`, `has_midi_input boolread-only`, `has_midi_output boolread-only`, `mute boolobserve`, `muted_via_solo boolread-onlyobserve`, `name unicodeobserve`, `solo boolobserve`
- Functions (2): `delete_device`, `insert_device`

### ChainMixerDevice
- File: `chainmixerdevice.md`
- Source URL: https://docs.cycling74.com/apiref/lom/chainmixerdevice/
- Description: This class represents a chain's mixer device in Live.
- Canonical paths:
  - `live_set tracks N devices M chains L mixer_device`
  - `live_set tracks N devices M return_chains L mixer_device`
- Children (4): `sends list of [DeviceParameter](https://docs.cycling74.com/apiref/lom/deviceparameter/ "DeviceParameter")read-onlyobserve`, `chain_activator [DeviceParameter](https://docs.cycling74.com/apiref/lom/deviceparameter/ "DeviceParameter")read-only`, `panning [DeviceParameter](https://docs.cycling74.com/apiref/lom/deviceparameter/ "DeviceParameter")read-only`, `volume [DeviceParameter](https://docs.cycling74.com/apiref/lom/deviceparameter/ "DeviceParameter")read-only`

### Clip
- File: `clip.md`
- Source URL: https://docs.cycling74.com/apiref/lom/clip/
- Description: This class represents a clip in Live. It can be either an audio clip or a MIDI clip in the Arrangement or Session View, depending on the track / slot it lives in.
- Canonical paths:
  - `live_set tracks N clip_slots M clip`
  - `live_set tracks N arrangement_clips M`
- Children (1): `view [Clip.View](https://docs.cycling74.com/apiref/lom/clip_view/ "Clip.View")read-only`
- Properties (48): `available_warp_modes listread-only`, `color intobserve`, `color_index intobserve`, `end_marker floatobserve`, `end_time floatread-onlyobserve`, `gain floatobserve`, `gain_display_string symbolread-only`, `file_path symbolread-only`, `groove [Groove](https://docs.cycling74.com/apiref/lom/groove/ "Groove")observe`, `has_envelopes boolread-onlyobserve`, `has_groove boolread-only`, `is_session_clip boolread-only`, `is_arrangement_clip boolread-only`, `is_take_lane_clip boolread-only`, `is_audio_clip boolread-only`, `is_midi_clip boolread-only`, `is_overdubbing boolread-onlyobserve`, `is_playing bool`, `is_recording boolread-onlyobserve`, `is_triggered boolread-only`, `launch_mode intobserve`, `launch_quantization intobserve`, `legato boolobserve`, `length floatread-only`, `loop_end floatobserve`, `loop_jump bangobserve`, `loop_start floatobserve`, `looping boolobserve`, `muted boolobserve`, `name symbolobserve`, `notes bangobserve`, `warp_markers dict/bangread-onlyobserve`, `pitch_coarse intobserve`, `pitch_fine floatobserve`, `playing_position floatread-onlyobserve`, `playing_status bangobserve`, `position floatread-onlyobserve`, `ram_mode boolobserve`, `sample_length intread-only`, `sample_rate floatread-only` ...
- Functions (28): `add_new_notes`, `add_warp_marker`, `apply_note_modifications`, `clear_all_envelopes`, `clear_envelope`, `crop`, `deselect_all_notes`, `duplicate_loop`, `duplicate_notes_by_id`, `duplicate_region`, `fire`, `get_all_notes_extended`, `get_notes_by_id`, `get_notes_extended`, `get_selected_notes_extended`, `move_playing_pos`, `move_warp_marker`, `quantize`, `quantize_pitch`, `remove_notes_by_id`, `remove_notes_extended`, `remove_warp_marker`, `scrub`, `select_all_notes`, `select_notes_by_id`, `set_fire_button_state`, `stop`, `stop_scrub`

### Clip.View
- File: `clip_view.md`
- Source URL: https://docs.cycling74.com/apiref/lom/clip_view/
- Description: Representing the view aspects of a Clip.
- Canonical paths:
  - `live_set tracks N clip_slots M clip view`
- Properties (2): `grid_is_triplet bool`, `grid_quantization int`
- Functions (4): `hide_envelope`, `select_envelope_parameter`, `show_envelope`, `show_loop`

### ClipSlot
- File: `clipslot.md`
- Source URL: https://docs.cycling74.com/apiref/lom/clipslot/
- Description: This class represents an entry in Live's Session View matrix.
- Canonical paths:
  - `live_set tracks N clip_slots M`
- Children (1): `clip [Clip](https://docs.cycling74.com/apiref/lom/clip/ "Clip")read-only`
- Properties (11): `color longread-onlyobserve`, `color_index longread-onlyobserve`, `controls_other_clips boolread-onlyobserve`, `has_clip boolread-onlyobserve`, `has_stop_button boolobserve`, `is_group_slot boolread-only`, `is_playing boolread-only`, `is_recording boolread-only`, `is_triggered boolread-onlyobserve`, `playing_status intread-onlyobserve`, `will_record_on_start boolread-only`
- Functions (7): `create_audio_clip`, `create_clip`, `delete_clip`, `duplicate_clip_to`, `fire`, `set_fire_button_state`, `stop`

### CompressorDevice
- File: `compressordevice.md`
- Source URL: https://docs.cycling74.com/apiref/lom/compressordevice/
- Description: This class represents a Compressor device in Live.
- Properties (4): `available_input_routing_channels dictread-onlyobserve`, `available_input_routing_types dictread-onlyobserve`, `input_routing_channel dictobserve`, `input_routing_type dictobserve`

### ControlSurface
- File: `controlsurface.md`
- Source URL: https://docs.cycling74.com/apiref/lom/controlsurface/
- Description: A ControlSurface can be reached either directly by the root path `control_surfaces N` or by getting a list of active control surface IDs, via calling _get control_surfaces_ on an Application object.
- Canonical paths:
  - `control_surfaces N`
- Properties (1): `pad_layout symbolread-onlyobserve`
- Functions (9): `get_control`, `get_control_names`, `grab_control`, `grab_midi`, `register_midi_control`, `release_control`, `release_midi`, `send_midi`, `send_receive_sysex`

### CuePoint
- File: `cuepoint.md`
- Source URL: https://docs.cycling74.com/apiref/lom/cuepoint/
- Description: Represents a locator in the Arrangement View.
- Canonical paths:
  - `live_set cue_points N`
- Properties (2): `name symbolobserve`, `time floatread-onlyobserve`
- Functions (1): `jump`

### Device
- File: `device.md`
- Source URL: https://docs.cycling74.com/apiref/lom/device/
- Description: This class represents a MIDI or audio device in Live.
- Canonical paths:
  - `live_set tracks N devices M`
  - `live_set tracks N devices M chains L devices K`
  - `live_set tracks N devices M return_chains L devices K`
- Children (2): `parameters list of [DeviceParameter](https://docs.cycling74.com/apiref/lom/deviceparameter/ "DeviceParameter")read-onlyobserve`, `view [Device.View](https://docs.cycling74.com/apiref/lom/device_view/ "Device.View")read-only`
- Properties (11): `can_have_chains boolread-only`, `can_have_drum_pads boolread-only`, `class_display_name symbolread-only`, `class_name symbolread-only`, `is_active boolread-onlyobserve`, `name symbolobserve`, `type intread-only`, `latency_in_samples intread-onlyobserve`, `latency_in_ms floatread-onlyobserve`, `can_compare_ab boolread-only`, `is_using_compare_preset_b boolobserve`
- Functions (2): `store_chosen_bank`, `save_preset_to_compare_ab_slot`

### Device.View
- File: `device_view.md`
- Source URL: https://docs.cycling74.com/apiref/lom/device_view/
- Description: Representing the view aspects of a Device.
- Canonical paths:
  - `live_set tracks N devices M view`
  - `live_set tracks N devices M chains L devices K view`
  - `live_set tracks N devices M return_chains L devices K view`
- Properties (1): `is_collapsed boolobserve`

### DeviceIO
- File: `deviceio.md`
- Source URL: https://docs.cycling74.com/apiref/lom/deviceio/
- Description: This class represents an input or output bus of a Live device.
- Properties (5): `available_routing_channels dictionaryread-onlyobserve`, `available_routing_types dictionaryread-onlyobserve`, `default_external_routing_channel_is_none bool`, `routing_channel dictionaryobserve`, `routing_type dictionaryobserve`

### DeviceParameter
- File: `deviceparameter.md`
- Source URL: https://docs.cycling74.com/apiref/lom/deviceparameter/
- Description: This class represents an (automatable) parameter within a MIDI or audio device. To modify a device parameter, set its `value` property or send its object ID to [live.remote~](https://docs.cycling74.com/reference/live.remote~ "live.remote~").
- Canonical paths:
  - `live_set tracks N devices M parameters L`
- Properties (12): `automation_state intread-onlyobserve`, `default_value floatread-only`, `is_enabled boolread-only`, `is_quantized boolread-only`, `max floatread-only`, `min floatread-only`, `name symbolread-only`, `original_name symbolread-only`, `state intread-onlyobserve`, `value floatobserve`, `display_value floatobserve`, `value_items StringVectorread-only`
- Functions (3): `re_enable_automation`, `str_for_value`, `__str__`

### DriftDevice
- File: `driftdevice.md`
- Source URL: https://docs.cycling74.com/apiref/lom/driftdevice/
- Description: This class represents an instance of a Drift device in Live.
- Properties (29): `mod_matrix_filter_source_1_index intobserve`, `mod_matrix_filter_source_1_list StringVectorread-only`, `mod_matrix_filter_source_2_index intobserve`, `mod_matrix_filter_source_2_list StringVectorread-only`, `mod_matrix_lfo_source_index intobserve`, `mod_matrix_lfo_source_list StringVectorread-only`, `mod_matrix_pitch_source_1_index intobserve`, `mod_matrix_pitch_source_1_list StringVectorread-only`, `mod_matrix_pitch_source_2_index intobserve`, `mod_matrix_pitch_source_2_list StringVectorread-only`, `mod_matrix_shape_source_index intobserve`, `mod_matrix_shape_source_list StringVectorread-only`, `mod_matrix_source_1_index intobserve`, `mod_matrix_source_1_list StringVectorread-only`, `mod_matrix_source_2_index intobserve`, `mod_matrix_source_2_list StringVectorread-only`, `mod_matrix_source_3_index intobserve`, `mod_matrix_source_3_list StringVectorread-only`, `mod_matrix_target_1_index intobserve`, `mod_matrix_target_1_list StringVectorread-only`, `mod_matrix_target_2_index intobserve`, `mod_matrix_target_2_list StringVectorread-only`, `mod_matrix_target_3_index intobserve`, `mod_matrix_target_3_list StringVectorread-only`, `pitch_bend_range intobserve`, `voice_count_index intobserve`, `voice_count_list StringVectorread-only`, `voice_mode_index intobserve`, `voice_mode_list StringVectorread-only`

### DrumCellDevice
- File: `drumcelldevice.md`
- Source URL: https://docs.cycling74.com/apiref/lom/drumcelldevice/
- Description: This class represents an instance of a Drum Sampler device in Live.
- Properties (1): `gain floatobserve`

### DrumChain
- File: `drumchain.md`
- Source URL: https://docs.cycling74.com/apiref/lom/drumchain/
- Description: This class represents a Drum Rack device chain in Live.
- Properties (3): `in_note intobserve`, `out_note intobserve`, `choke_group intobserve`

### DrumPad
- File: `drumpad.md`
- Source URL: https://docs.cycling74.com/apiref/lom/drumpad/
- Description: This class represents a Drum Rack pad in Live.
- Canonical paths:
  - `live_set tracks N devices M drum_pads L`
- Children (1): `chains [Chain](https://docs.cycling74.com/apiref/lom/chain/ "Chain")read-onlyobserve`
- Properties (4): `mute boolobserve`, `name symbolread-onlyobserve`, `note intread-only`, `solo boolobserve`
- Functions (1): `delete_all_chains`

### Eq8Device
- File: `eq8device.md`
- Source URL: https://docs.cycling74.com/apiref/lom/eq8device/
- Description: This class represents an instance of an EQ Eight device in Live.
- Properties (3): `edit_mode boolobserve`, `global_mode intobserve`, `oversample boolobserve`

### Eq8Device.View
- File: `eq8device_view.md`
- Source URL: https://docs.cycling74.com/apiref/lom/eq8device_view/
- Description: Represents the view aspects of an Eq8Device.
- Properties (1): `selected_band intobserve`

### Groove
- File: `groove.md`
- Source URL: https://docs.cycling74.com/apiref/lom/groove/
- Description: This class represents a groove in Live.
- Canonical paths:
  - `live_set groove_pool grooves N`
  - `live_set tracks N clip_slots M clip groove`
- Children (6): `base int`, `name symbolobserve`, `quantization_amount floatobserve`, `random_amount floatobserve`, `timing_amount floatobserve`, `velocity_amount floatobserve`

### GroovePool
- File: `groovepool.md`
- Source URL: https://docs.cycling74.com/apiref/lom/groovepool/
- Description: This class represents the groove pool in Live. It provides access to the current set's list of grooves.
- Canonical paths:
  - `live_set groove_pool`
- Children (1): `grooves list of [Groove](https://docs.cycling74.com/apiref/lom/groove/ "Groove")read-onlyobserve`

### HybridReverbDevice
- File: `hybridreverbdevice.md`
- Source URL: https://docs.cycling74.com/apiref/lom/hybridreverbdevice/
- Description: This class represents an instance of a Hybrid Reverb device in Live.
- Properties (8): `ir_attack_time floatobserve`, `ir_category_index intobserve`, `ir_category_list StringVectorread-only`, `ir_decay_time floatobserve`, `ir_file_index intobserve`, `ir_file_list StringVectorread-onlyobserve`, `ir_size_factor floatobserve`, `ir_time_shaping_on boolobserve`

### LooperDevice
- File: `looperdevice.md`
- Source URL: https://docs.cycling74.com/apiref/lom/looperdevice/
- Description: This class represents an instance of a Looper device in Live.
- Properties (5): `loop_length floatread-onlyobserve`, `overdub_after_record boolobserve`, `record_length_index intobserve`, `record_length_list StringVectorread-only`, `tempo floatread-onlyobserve`
- Functions (11): `clear`, `double_speed`, `half_speed`, `double_length`, `half_length`, `record`, `overdub`, `play`, `stop`, `undo`, `export_to_clip_slot`

### MaxDevice
- File: `maxdevice.md`
- Source URL: https://docs.cycling74.com/apiref/lom/maxdevice/
- Description: This class represents a Max for Live device in Live.
- Properties (4): `audio_inputs list of [DeviceIO](https://docs.cycling74.com/apiref/lom/deviceio/ "DeviceIO")read-onlyobserve`, `audio_outputs list of [DeviceIO](https://docs.cycling74.com/apiref/lom/deviceio/ "DeviceIO")read-onlyobserve`, `midi_inputs list of [DeviceIO](https://docs.cycling74.com/apiref/lom/deviceio/ "DeviceIO")read-onlyobserve`, `midi_outputs list of [DeviceIO](https://docs.cycling74.com/apiref/lom/deviceio/ "DeviceIO")read-onlyobserve`
- Functions (3): `get_bank_count`, `get_bank_name`, `get_bank_parameters`

### MeldDevice
- File: `melddevice.md`
- Source URL: https://docs.cycling74.com/apiref/lom/melddevice/
- Description: This class represents an instance of a Meld device in Live.
- Properties (4): `selected_engine intobserve`, `unison_voices intobserve`, `mono_poly intobserve`, `poly_voices intobserve`

### MixerDevice
- File: `mixerdevice.md`
- Source URL: https://docs.cycling74.com/apiref/lom/mixerdevice/
- Description: This class represents a mixer device in Live. It provides access to volume, panning and other [DeviceParameter](https://docs.cycling74.com/apiref/lom/mixerdevice/#DeviceParameter) objects. See [DeviceParameter](https://docs.cycling74.com/apiref/lom/mixerdevice/#DeviceParameter) to learn how to modify them.
- Canonical paths:
  - `live_set tracks N mixer_device`
- Children (9): `sends list of [DeviceParameter](https://docs.cycling74.com/apiref/lom/deviceparameter/ "DeviceParameter")read-onlyobserve`, `cue_volume [DeviceParameter](https://docs.cycling74.com/apiref/lom/deviceparameter/ "DeviceParameter")read-only`, `crossfader [DeviceParameter](https://docs.cycling74.com/apiref/lom/deviceparameter/ "DeviceParameter")read-only`, `left_split_stereo [DeviceParameter](https://docs.cycling74.com/apiref/lom/deviceparameter/ "DeviceParameter")read-only`, `panning [DeviceParameter](https://docs.cycling74.com/apiref/lom/deviceparameter/ "DeviceParameter")read-only`, `right_split_stereo [DeviceParameter](https://docs.cycling74.com/apiref/lom/deviceparameter/ "DeviceParameter")read-only`, `song_tempo [DeviceParameter](https://docs.cycling74.com/apiref/lom/deviceparameter/ "DeviceParameter")read-only`, `track_activator [DeviceParameter](https://docs.cycling74.com/apiref/lom/deviceparameter/ "DeviceParameter")read-only`, `volume [DeviceParameter](https://docs.cycling74.com/apiref/lom/deviceparameter/ "DeviceParameter")read-only`
- Properties (2): `crossfade_assign intobserve`, `panning_mode intobserve`

### PluginDevice
- File: `plugindevice.md`
- Source URL: https://docs.cycling74.com/apiref/lom/plugindevice/
- Description: This class represents a plug-in device.
- Properties (2): `presets StringVectorread-onlyobserve`, `selected_preset_index intobserve`

### RackDevice
- File: `rackdevice.md`
- Source URL: https://docs.cycling74.com/apiref/lom/rackdevice/
- Description: This class represents a Live Rack Device.
- Children (5): `chain_selector [DeviceParameter](https://docs.cycling74.com/apiref/lom/deviceparameter/ "DeviceParameter")read-only`, `chains list of [Chain](https://docs.cycling74.com/apiref/lom/chain/ "Chain")read-onlyobserve`, `drum_pads list of [DrumPad](https://docs.cycling74.com/apiref/lom/drumpad/ "DrumPad")read-onlyobserve`, `return_chains list of [Chain](https://docs.cycling74.com/apiref/lom/chain/ "Chain")read-onlyobserve`, `visible_drum_pads list of [DrumPad](https://docs.cycling74.com/apiref/lom/drumpad/ "DrumPad")read-onlyobserve`
- Properties (7): `can_show_chains boolread-only`, `has_drum_pads boolread-onlyobserve`, `has_macro_mappings boolread-onlyobserve`, `is_showing_chains boolobserve`, `variation_count intread-onlyobserve`, `selected_variation_index int`, `visible_macro_count intread-onlyobserve`
- Functions (9): `copy_pad`, `add_macro`, `insert_chain`, `remove_macro`, `randomize_macros`, `store_variation`, `recall_selected_variation`, `recall_last_used_variation`, `delete_selected_variation`

### RackDevice.View
- File: `rackdevice_view.md`
- Source URL: https://docs.cycling74.com/apiref/lom/rackdevice_view/
- Description: Represents the view aspects of a Rack Device.
- Children (2): `selected_drum_pad [DrumPad](https://docs.cycling74.com/apiref/lom/drumpad/ "DrumPad")observe`, `selected_chain [Chain](https://docs.cycling74.com/apiref/lom/chain/ "Chain")observe`
- Properties (2): `drum_pads_scroll_position intobserve`, `is_showing_chain_devices boolobserve`

### RoarDevice
- File: `roardevice.md`
- Source URL: https://docs.cycling74.com/apiref/lom/roardevice/
- Description: This class represents an instance of a Roar device in Live.
- Properties (3): `routing_mode_index intobserve`, `routing_mode_list StringVectorread-only`, `env_listen boolobserve`

### Sample
- File: `sample.md`
- Source URL: https://docs.cycling74.com/apiref/lom/sample/
- Description: This class represents a sample file loaded into Simpler.
- Canonical paths:
  - `live_set tracks N devices N sample`
- Properties (22): `beats_granulation_resolution intobserve`, `beats_transient_envelope floatobserve`, `beats_transient_loop_mode intobserve`, `complex_pro_envelope floatobserve`, `complex_pro_formants floatobserve`, `end_marker intobserve`, `file_path unicoderead-onlyobserve`, `gain floatobserve`, `length intread-only`, `sample_rate intread-only`, `slices list of intread-onlyobserve`, `slicing_sensitivity floatobserve`, `start_marker intobserve`, `texture_flux floatobserve`, `texture_grain_size floatobserve`, `tones_grain_size floatobserve`, `warp_markers dict/bangread-onlyobserve`, `warp_mode intobserve`, `warping boolobserve`, `slicing_style intobserve`, `slicing_beat_division intobserve`, `slicing_region_count intobserve`
- Functions (6): `gain_display_string`, `insert_slice`, `move_slice`, `remove_slice`, `clear_slices`, `reset_slices`

### Scene
- File: `scene.md`
- Source URL: https://docs.cycling74.com/apiref/lom/scene/
- Description: This class represents a series of clip slots in Live's Session View matrix.
- Canonical paths:
  - `live_set scenes N`
- Children (1): `clip_slots list of [ClipSlot](https://docs.cycling74.com/apiref/lom/clipslot/ "ClipSlot")read-onlyobserve`
- Properties (10): `color intobserve`, `color_index longobserve`, `is_empty boolread-only`, `is_triggered boolread-onlyobserve`, `name symbolobserve`, `tempo floatobserve`, `tempo_enabled boolobserve`, `time_signature_numerator intobserve`, `time_signature_denominator intobserve`, `time_signature_enabled boolobserve`
- Functions (3): `fire`, `fire_as_selected`, `set_fire_button_state`

### ShifterDevice
- File: `shifterdevice.md`
- Source URL: https://docs.cycling74.com/apiref/lom/shifterdevice/
- Description: This class represents an instance of the Shifter audio effect.
- Properties (2): `pitch_bend_range intobserve`, `pitch_mode_index intobserve`

### SimplerDevice
- File: `simplerdevice.md`
- Source URL: https://docs.cycling74.com/apiref/lom/simplerdevice/
- Description: This class represents an instance of Simpler.
- Children (1): `sample [Sample](https://docs.cycling74.com/apiref/lom/sample/ "Sample")read-onlyobserve`
- Properties (11): `can_warp_as boolread-onlyobserve`, `can_warp_double boolread-onlyobserve`, `can_warp_half boolread-onlyobserve`, `multi_sample_mode boolread-onlyobserve`, `pad_slicing boolobserve`, `playback_mode intobserve`, `playing_position floatread-onlyobserve`, `playing_position_enabled boolread-onlyobserve`, `retrigger boolobserve`, `slicing_playback_mode intobserve`, `voices intobserve`
- Functions (6): `crop`, `guess_playback_length`, `reverse`, `warp_as`, `warp_double`, `warp_half`

### SimplerDevice.View
- File: `simplerdevice_view.md`
- Source URL: https://docs.cycling74.com/apiref/lom/simplerdevice_view/
- Description: Represents the view aspects of a SimplerDevice.
- Properties (1): `selected_slice intobserve`

### Song
- File: `song.md`
- Source URL: https://docs.cycling74.com/apiref/lom/song/
- Description: This class represents a Live Set. The current Live Set is reachable by the root path `live_set`.
- Canonical paths:
  - `live_set`
- Children (9): `cue_points list of [CuePoint](https://docs.cycling74.com/apiref/lom/cuepoint/ "CuePoint")read-onlyobserve`, `return_tracks list of [Track](https://docs.cycling74.com/apiref/lom/track/ "Track")read-onlyobserve`, `scenes list of [Scene](https://docs.cycling74.com/apiref/lom/scene/ "Scene")read-onlyobserve`, `tracks list of [Track](https://docs.cycling74.com/apiref/lom/track/ "Track")read-onlyobserve`, `visible_tracks list of [Track](https://docs.cycling74.com/apiref/lom/track/ "Track")read-onlyobserve`, `master_track [Track](https://docs.cycling74.com/apiref/lom/track/ "Track")read-only`, `view [Song.View](https://docs.cycling74.com/apiref/lom/song_view/ "Song.View")read-only`, `groove_pool [GroovePool](https://docs.cycling74.com/apiref/lom/groovepool/ "GroovePool")read-only`, `tuning_system [TuningSystem](https://docs.cycling74.com/apiref/lom/tuningsystem/ "TuningSystem")read-onlyobserve`
- Properties (48): `appointed_device [Device](https://docs.cycling74.com/apiref/lom/device/ "Device")read-onlyobserve`, `arrangement_overdub boolobserve`, `back_to_arranger boolobserve`, `can_capture_midi boolread-onlyobserve`, `can_jump_to_next_cue boolread-onlyobserve`, `can_jump_to_prev_cue boolread-onlyobserve`, `can_redo boolread-only`, `can_undo boolread-only`, `clip_trigger_quantization intobserve`, `count_in_duration intread-onlyobserve`, `current_song_time floatobserve`, `exclusive_arm boolread-only`, `exclusive_solo boolread-only`, `file_path symbolread-only`, `groove_amount floatobserve`, `is_ableton_link_enabled boolobserve`, `is_ableton_link_start_stop_sync_enabled boolobserve`, `is_counting_in boolread-onlyobserve`, `is_playing boolobserve`, `last_event_time floatread-only`, `loop boolobserve`, `loop_length floatobserve`, `loop_start floatobserve`, `metronome boolobserve`, `midi_recording_quantization intobserve`, `name symbolread-only`, `nudge_down boolobserve`, `nudge_up boolobserve`, `tempo_follower_enabled boolobserve`, `overdub boolobserve`, `punch_in boolobserve`, `punch_out boolobserve`, `re_enable_automation_enabled boolread-onlyobserve`, `record_mode boolobserve`, `root_note intobserve`, `scale_intervals listread-onlyobserve`, `scale_mode boolobserve`, `scale_name unicodeobserve`, `select_on_launch boolread-only`, `session_automation_record boolobserve` ...
- Functions (34): `capture_and_insert_scene`, `capture_midi`, `continue_playing`, `create_audio_track`, `create_midi_track`, `create_return_track`, `create_scene`, `delete_scene`, `delete_track`, `delete_return_track`, `duplicate_scene`, `duplicate_track`, `find_device_position`, `force_link_beat_time`, `get_beats_loop_length`, `get_beats_loop_start`, `get_current_beats_song_time`, `get_current_smpte_song_time`, `is_cue_point_selected`, `jump_by`, `jump_to_next_cue`, `jump_to_prev_cue`, `move_device`, `play_selection`, `re_enable_automation`, `redo`, `scrub_by`, `set_or_delete_cue`, `start_playing`, `stop_all_clips`, `stop_playing`, `tap_tempo`, `trigger_session_record`, `undo`

### Song.View
- File: `song_view.md`
- Source URL: https://docs.cycling74.com/apiref/lom/song_view/
- Description: This class represents the view aspects of a Live document: the Session and Arrangement Views.
- Canonical paths:
  - `live_set view`
- Children (6): `detail_clip [Clip](https://docs.cycling74.com/apiref/lom/clip/ "Clip")observe`, `highlighted_clip_slot [ClipSlot](https://docs.cycling74.com/apiref/lom/clipslot/ "ClipSlot")`, `selected_chain [Chain](https://docs.cycling74.com/apiref/lom/chain/ "Chain")observe`, `selected_parameter [DeviceParameter](https://docs.cycling74.com/apiref/lom/deviceparameter/ "DeviceParameter")read-onlyobserve`, `selected_scene [Scene](https://docs.cycling74.com/apiref/lom/scene/ "Scene")observe`, `selected_track [Track](https://docs.cycling74.com/apiref/lom/track/ "Track")observe`
- Properties (2): `draw_mode boolobserve`, `follow_song boolobserve`
- Functions (1): `select_device`

### SpectralResonatorDevice
- File: `spectralresonatordevice.md`
- Source URL: https://docs.cycling74.com/apiref/lom/spectralresonatordevice/
- Description: This class represents an instance of a Spectral Resonator device in Live.
- Properties (7): `frequency_dial_mode intobserve`, `midi_gate intobserve`, `mod_mode intobserve`, `mono_poly intobserve`, `pitch_mode intobserve`, `pitch_bend_range intobserve`, `polyphony intobserve`

### TakeLane
- File: `takelane.md`
- Source URL: https://docs.cycling74.com/apiref/lom/takelane/
- Description: This class represents a take lane in Live. Tracks in Live can have take lanes in Arrangement View, which are used for comping. If take lanes exist for a track, they can be shown by right-clicking on a track and choosing Show Take Lanes.
- Canonical paths:
  - `live_set tracks N take_lanes M`
- Children (1): `arrangement_clips list of [Clip](https://docs.cycling74.com/apiref/lom/clip/ "Clip")read-onlyobserve`
- Properties (1): `name symbolobserve`
- Functions (2): `create_audio_clip`, `create_midi_clip`

### this_device
- File: `this_device.md`
- Source URL: https://docs.cycling74.com/apiref/lom/this_device/
- Description: This root path represents the device containing the [live.path](https://docs.cycling74.com/reference/live.path "live.path") object to which the `goto this_device` message is sent. The class of this object is `Device`.
- Canonical paths:
  - `live_set tracks N devices M`

### Track
- File: `track.md`
- Source URL: https://docs.cycling74.com/apiref/lom/track/
- Description: This class represents a track in Live. It can either be an audio track, a MIDI track, a return track or the master track. The master track and at least one Audio or MIDI track will be always present. Return tracks are optional.
- Canonical paths:
  - `live_set tracks N`
- Children (7): `take_lanes list of [TakeLane](https://docs.cycling74.com/apiref/lom/takelane/ "TakeLane")read-onlyobserve`, `clip_slots list of [ClipSlot](https://docs.cycling74.com/apiref/lom/clipslot/ "ClipSlot")read-onlyobserve`, `arrangement_clips list of [Clip](https://docs.cycling74.com/apiref/lom/clip/ "Clip")read-onlyobserve`, `devices list of [Device](https://docs.cycling74.com/apiref/lom/device/ "Device")read-onlyobserve`, `group_track [Track](https://docs.cycling74.com/apiref/lom/track/ "Track")read-only`, `mixer_device [MixerDevice](https://docs.cycling74.com/apiref/lom/mixerdevice/ "MixerDevice")read-only`, `view [Track.View](https://docs.cycling74.com/apiref/lom/track_view/ "Track.View")read-only`
- Properties (40): `arm boolobserve`, `available_input_routing_channels dictionaryread-onlyobserve`, `available_input_routing_types dictionaryread-onlyobserve`, `available_output_routing_channels dictionaryread-onlyobserve`, `available_output_routing_types dictionaryread-onlyobserve`, `back_to_arranger boolobserve`, `can_be_armed boolread-only`, `can_be_frozen boolread-only`, `can_show_chains boolread-only`, `color intobserve`, `color_index longobserve`, `fired_slot_index intread-onlyobserve`, `fold_state int`, `has_audio_input boolread-only`, `has_audio_output boolread-only`, `has_midi_input boolread-only`, `has_midi_output boolread-only`, `implicit_arm boolobserve`, `input_meter_left floatread-onlyobserve`, `input_meter_level floatread-onlyobserve`, `input_meter_right floatread-onlyobserve`, `input_routing_channel dictionaryobserve`, `input_routing_type dictionaryobserve`, `is_foldable boolread-only`, `is_frozen boolread-onlyobserve`, `is_grouped boolread-only`, `is_part_of_selection boolread-only`, `is_showing_chains boolobserve`, `is_visible boolread-only`, `mute boolobserve`, `muted_via_solo boolread-onlyobserve`, `name symbolobserve`, `output_meter_left floatread-onlyobserve`, `output_meter_level floatread-onlyobserve`, `output_meter_right floatread-onlyobserve`, `performance_impact floatread-onlyobserve`, `output_routing_channel dictionaryobserve`, `output_routing_type dictionaryobserve`, `playing_slot_index intread-onlyobserve`, `solo boolobserve`
- Functions (10): `create_audio_clip`, `create_midi_clip`, `create_take_lane`, `delete_clip`, `delete_device`, `duplicate_clip_slot`, `duplicate_clip_to_arrangement`, `insert_device`, `jump_in_running_session_clip`, `stop_all_clips`

### Track.View
- File: `track_view.md`
- Source URL: https://docs.cycling74.com/apiref/lom/track_view/
- Description: Representing the view aspects of a track.
- Canonical paths:
  - `live_set tracks N view`
- Children (1): `selected_device [Device](https://docs.cycling74.com/apiref/lom/device/ "Device")read-onlyobserve`
- Properties (2): `device_insert_mode intobserve`, `is_collapsed boolobserve`
- Functions (1): `select_instrument`

### TuningSystem
- File: `tuningsystem.md`
- Source URL: https://docs.cycling74.com/apiref/lom/tuningsystem/
- Description: This class represents a tuning system in Live.
- Canonical paths:
  - `live_set tuning_system`
- Properties (6): `name symbolobserve`, `pseudo_octave_in_cents floatread-only`, `lowest_note dictionaryobserve`, `highest_note dictionaryobserve`, `reference_pitch dictionaryobserve`, `note_tunings dictionaryobserve`

### WavetableDevice
- File: `wavetabledevice.md`
- Source URL: https://docs.cycling74.com/apiref/lom/wavetabledevice/
- Description: This class represents a Wavetable instrument.
- Properties (15): `filter_routing intobserve`, `mono_poly intobserve`, `oscillator_1_effect_mode intobserve`, `oscillator_2_effect_mode intobserve`, `oscillator_1_wavetable_category observe`, `oscillator_2_wavetable_category observe`, `oscillator_1_wavetable_index observe`, `oscillator_2_wavetable_index observe`, `oscillator_1_wavetables StringVectorread-onlyobserve`, `oscillator_2_wavetables StringVectorread-onlyobserve`, `oscillator_wavetable_categories StringVectorread-only`, `poly_voices intobserve`, `unison_mode intobserve`, `unison_voice_count intobserve`, `visible_modulation_target_names StringVectorread-onlyobserve`
- Functions (5): `add_parameter_to_modulation_matrix`, `get_modulation_target_parameter_name`, `get_modulation_value`, `is_parameter_modulatable`, `set_modulation_value`

## Notes for implementation
- Treat `Track.arrangement_clips` and `Track.create_midi_clip(start_time, length)` as the core Arrangement-first path.
- Prefer extended note APIs on `Clip` where available.
- Treat `Device.parameters` / `DeviceParameter.value` as the supported parameter-control boundary.
- Use explicit unsupported-operation errors for MIDI-only, audio-only, frozen-track, or plugin-internal cases.
- Do not expose arbitrary Python eval to MCP by default.
