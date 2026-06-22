---
source_url: "https://docs.cycling74.com/apiref/lom/track/"
fetched_at: "2026-06-21T21:08:27.1876504-04:00"
---
# Track

This class represents a track in Live. It can either be an audio track, a MIDI track, a return track or the master track. The master track and at least one Audio or MIDI track will be always present. Return tracks are optional.

Not all properties are supported by all types of tracks. The properties are marked accordingly.

## Canonical Path

```clike
live_set tracks N
```

## Children

### take_lanes list of [TakeLane](https://docs.cycling74.com/apiref/lom/takelane/ "TakeLane")read-onlyobserve

The list of this track's take lanes

### clip_slots list of [ClipSlot](https://docs.cycling74.com/apiref/lom/clipslot/ "ClipSlot")read-onlyobserve

### arrangement_clips list of [Clip](https://docs.cycling74.com/apiref/lom/clip/ "Clip")read-onlyobserve

The list of this track's Arrangement View clip IDs

_Available since Live 11.0._

### devices list of [Device](https://docs.cycling74.com/apiref/lom/device/ "Device")read-onlyobserve

Includes mixer device.

### group_track [Track](https://docs.cycling74.com/apiref/lom/track/ "Track")read-only

The Group Track, if the Track is grouped. If it is not, _id 0_ is returned.

### mixer_device [MixerDevice](https://docs.cycling74.com/apiref/lom/mixerdevice/ "MixerDevice")read-only

### view [Track.View](https://docs.cycling74.com/apiref/lom/track_view/ "Track.View")read-only

## Properties

### arm boolobserve

1 = track is armed for recording. [not in return/master tracks]

### available_input_routing_channels dictionaryread-onlyobserve

The list of available source channels for the track's input routing. It's represented as a _dictionary_ with the following key:

`available_input_routing_channels` [list]

The list contains _dictionaries_ as described in _input_routing_channel_.

Only available on MIDI and audio tracks.

### available_input_routing_types dictionaryread-onlyobserve

The list of available source types for the track's input routing. It's represented as a _dictionary_ with the following key:

`available_input_routing_types` [list]

The list contains _dictionaries_ as described in _input_routing_type_.

Only available on MIDI and audio tracks.

### available_output_routing_channels dictionaryread-onlyobserve

The list of available target channels for the track's output routing. It's represented as a _dictionary_ with the following key:

`available_output_routing_channels` [list]

The list contains _dictionaries_ as described in _output_routing_channel_.

Not available on the master track.

### available_output_routing_types dictionaryread-onlyobserve

The list of available target types for the track's output routing. It's represented as a _dictionary_ with the following key:

`available_output_routing_types` [list]

The list contains _dictionaries_ as described in _output_routing_type_.

Not available on the master track.

### back_to_arranger boolobserve

Get/set/observe the current state of the Single Track Back to Arrangement button (1 = highlighted). This button is used to indicate that the current state of the playback differs from what is stored in the Arrangement.

Setting this property to 0 will make Live go back to playing the track's arrangement content. For group tracks, this means that all of the tracks that belong to the group and any subgroups will go back to playing the arrangement.

### can_be_armed boolread-only

0 for return and master tracks.

### can_be_frozen boolread-only

1 = the track can be frozen, 0 = otherwise.

### can_show_chains boolread-only

1 = the track contains an Instrument Rack device that can show chains in Session View.

### color intobserve

The RGB value of the track's color in the form `0x00rrggbb` or (2^16 * red) + (2^8) * green + blue, where red, green and blue are values from 0 (dark) to 255 (light).

When setting the RGB value, the nearest color from the track color chooser is taken.

### color_index longobserve

The color index of the track.

### fired_slot_index intread-onlyobserve

Reflects the blinking clip slot.

-1 = no slot fired, -2 = Clip Stop Button fired

First clip slot has index 0.

[not in return/master tracks]

### fold_state int

0 = tracks within the Group Track are visible, 1 = Group Track is folded and the tracks within the Group Track are hidden

[only available if `is_foldable` = 1]

### has_audio_input boolread-only

1 for audio tracks.

### has_audio_output boolread-only

1 for audio tracks and MIDI tracks with instruments.

### has_midi_input boolread-only

1 for MIDI tracks.

### has_midi_output boolread-only

1 for MIDI tracks with no instruments and no audio effects.

### implicit_arm boolobserve

A second arm state, only used by Push so far.

### input_meter_left floatread-onlyobserve

Smoothed momentary peak value of left channel input meter, 0.0 to 1.0. For tracks with audio output only. This value corresponds to the meters shown in Live. Please take into account that the left/right audio meters put a significant load onto the GUI part of Live.

### input_meter_level floatread-onlyobserve

Hold peak value of input meters of audio and MIDI tracks, 0.0 ... 1.0. For audio tracks it is the maximum of the left and right channels. The hold time is 1 second.

### input_meter_right floatread-onlyobserve

Smoothed momentary peak value of right channel input meter, 0.0 to 1.0. For tracks with audio output only. This value corresponds to the meters shown in Live.

### input_routing_channel dictionaryobserve

The currently selected source channel for the track's input routing. It's represented as a _dictionary_ with the following keys:

`display_name` [symbol]

`identifier` [symbol]

Can be set to all values found in the track's _available_input_routing_channels_.

Only available on MIDI and audio tracks.

### input_routing_type dictionaryobserve

The currently selected source type for the track's input routing. It's represented as a _dictionary_ with the following keys:

`display_name` [symbol]

`identifier` [symbol]

Can be set to all values found in the track's _available_input_routing_types_.

Only available on MIDI and audio tracks.

### is_foldable boolread-only

1 = track can be (un)folded to hide or reveal the contained tracks. This is currently the case for Group Tracks. Instrument and Drum Racks return 0 although they can be opened/closed. This will be fixed in a later release.

### is_frozen boolread-onlyobserve

1 = the track is currently frozen.

### is_grouped boolread-only

1 = the track is contained within a Group Track.

### is_part_of_selection boolread-only

### is_showing_chains boolobserve

Get or set whether a track with an Instrument Rack device is currently showing its chains in Session View.

### is_visible boolread-only

0 = track is hidden in a folded Group Track.

### mute boolobserve

[not in master track]

### muted_via_solo boolread-onlyobserve

1 = the track or chain is muted due to Solo being active on at least one other track.

### name symbolobserve

As shown in track header.

### output_meter_left floatread-onlyobserve

Smoothed momentary peak value of left channel output meter, 0.0 to 1.0. For tracks with audio output only. This value corresponds to the meters shown in Live. Please take into account that the left/right audio meters add a significant load to Live GUI resource usage.

### output_meter_level floatread-onlyobserve

Hold peak value of output meters of audio and MIDI tracks, 0.0 to 1.0. For audio tracks, it is the maximum of the left and right channels. The hold time is 1 second.

### output_meter_right floatread-onlyobserve

Smoothed momentary peak value of right channel output meter, 0.0 to 1.0. For tracks with audio output only. This value corresponds to the meters shown in Live.

### performance_impact floatread-onlyobserve

Reports the performance impact of this track.

### output_routing_channel dictionaryobserve

The currently selected target channel for the track's output routing. It's represented as a _dictionary_ with the following keys:

`display_name` [symbol]

`identifier` [symbol]

Can be set to all values found in the track's _available_output_routing_channels_.

Not available on the master track.

### output_routing_type dictionaryobserve

The currently selected target type for the track's output routing. It's represented as a _dictionary_ with the following keys:

`display_name` [symbol]

`identifier` [symbol]

Can be set to all values found in the track's _available_output_routing_types_.

Not available on the master track.

### playing_slot_index intread-onlyobserve

First slot has index 0, -2 = Clip Stop slot fired in Session View, -1 = Arrangement recording with no Session clip playing. [not in return/master tracks]

### solo boolobserve

Remark: when setting this property, the exclusive Solo logic is bypassed, so you have to unsolo the other tracks yourself. [not in master track]

## Functions

### create_audio_clip

Parameters:

`file_path` [symbol]

`position` [float]

Given an absolute path to a valid audio file in a supported format, creates an audio clip that references the file at the specified position in the arrangement view. Prints an error if the track is not an audio track, if the track is frozen, or if the track is being recorded into. The position must be within the range [0., 1576800].

See the `ClipSlot.create_audio_clip` function if you need to create audio clips in session view instead.

### create_midi_clip

Parameters:

`start_time` [float]

`length` [float]

Creates an empty MIDI clip and inserts it into the arrangement at the specified time. Throws an error when called on a non-MIDI track or a frozen track, when the specified time is outside the [0., 1576800.] range, or when the track is currently being recorded into.

See the `ClipSlot.create_clip` function if you need to create audio clips in session view instead.

### create_take_lane

Creates a take lane for this track.

### delete_clip

Parameter: `clip`

Delete the given clip.

### delete_device

Parameter: `index`

Delete the device at the given index.

### duplicate_clip_slot

Parameter: `index`

Works like 'Duplicate' in a clip's context menu.

### duplicate_clip_to_arrangement

Parameters: ```clip``destination_time``` [float]

Duplicate the given clip to the Arrangement, placing it at the given _destination_time_ in beats.

### insert_device

Parameters: `device_name` [symbol] `target_index` [int] (optional)

Attempts to insert the device specified by `device_name` at the given index in the track's device chain. If no index is provided, attempts to insert the device at the end of the chain. Throws an error if insertion is not possible.

`device_name` is the name as it appears in the UI of Live.

Not all indices are valid. As can be expected, indices outside of the range defined by the current length of the device chain are invalid, but there are other limitations: for example, a MIDI effect can't be inserted after an instrument. The rule of thumb is that if an index would be invalid when inserting using the mouse, it's invalid here.

At the moment, only native Live devices can be inserted. Max for Live devices and plug-in are not supported.

_Available since Live 12.3._

### jump_in_running_session_clip

Parameter: `beats`

`beats` [float] is the amount to jump relatively to the current clip position.

Modify playback position in running Session clip, if any.

### stop_all_clips

Stops all playing and fired clips in this track.
