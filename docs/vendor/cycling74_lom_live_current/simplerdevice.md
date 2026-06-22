---
source_url: "https://docs.cycling74.com/apiref/lom/simplerdevice/"
fetched_at: "2026-06-21T21:08:11.7193588-04:00"
---
# SimplerDevice

This class represents an instance of Simpler.

A SimplerDevice is a type of device, meaning that it has all the children, properties and functions that a device has. Listed below are members unique to SimplerDevice.

## Children

### sample [Sample](https://docs.cycling74.com/apiref/lom/sample/ "Sample")read-onlyobserve

The sample currently loaded into Simpler.

## Properties

### can_warp_as boolread-onlyobserve

1 = warp_as is available.

### can_warp_double boolread-onlyobserve

1 = warp_double is available.

### can_warp_half boolread-onlyobserve

1 = warp_half is available.

### multi_sample_mode boolread-onlyobserve

1 = Simpler is in multisample mode.

### pad_slicing boolobserve

1 = slices can be added in Slicing Mode by playing notes which are not yet assigned to existing slices.

### playback_mode intobserve

Get/set Simpler's playback mode.

0 = Classic Mode

1 = One-Shot Mode

2 = Slicing Mode

### playing_position floatread-onlyobserve

The current playing position in the sample, expressed as a value between 0. and 1.

### playing_position_enabled boolread-onlyobserve

1 = Simpler is playing back the sample and showing the playing position.

### retrigger boolobserve

1 = Retrigger is enabled in Simpler.

### slicing_playback_mode intobserve

Get/set Simpler's Slicing Playback Mode.

0 = Mono

1 = Poly

2 = Thru

### voices intobserve

Get/set the number of Voices.

## Functions

### crop

Crop the loaded sample to the active region between the start and end markers.

### guess_playback_length

Returns: [float] An estimated beat time for the playback length between the start and end markers.

### reverse

Reverse the loaded sample.

### warp_as

Parameters: `beats` [int]

Warp the active region between the start and end markers as the specified number of beats.

### warp_double

Double the playback tempo of the active region between the start and end markers.

### warp_half

Halve the playback tempo for the active region between the start and end markers.
