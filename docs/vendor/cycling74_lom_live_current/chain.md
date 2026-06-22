---
source_url: "https://docs.cycling74.com/apiref/lom/chain/"
fetched_at: "2026-06-21T21:06:57.9231316-04:00"
---
# Chain

This class represents a group device chain in Live.

## Canonical Paths

```clike
live_set tracks N devices M chains L
```

```clike
live_set tracks N devices M return_chains L
```

```clike
live_set tracks N devices M chains L devices K chains P ...
```

```clike
live_set tracks N devices M return_chains L devices K chains P ...
```

## Children

### devices [Device](https://docs.cycling74.com/apiref/lom/device/ "Device")read-onlyobserve

### mixer_device [ChainMixerDevice](https://docs.cycling74.com/apiref/lom/chainmixerdevice/ "ChainMixerDevice")read-only

## Properties

### color intobserve

The RGB value of the chain's color in the form `0x00rrggbb` or (2^16 * red) + (2^8) * green + blue, where red, green and blue are values from 0 (dark) to 255 (light).

When setting the RGB value, the nearest color from the color chooser is taken.

### color_index longobserve

The color index of the chain.

### is_auto_colored boolobserve

1 = the chain will always have the color of the containing track or chain.

### has_audio_input boolread-only

### has_audio_output boolread-only

### has_midi_input boolread-only

### has_midi_output boolread-only

### mute boolobserve

1 = muted (Chain Activator off)

### muted_via_solo boolread-onlyobserve

1 = muted due to another chain being soloed.

### name unicodeobserve

### solo boolobserve

1 = soloed (Solo switch on)

does not automatically turn Solo off in other chains.

## Functions

### delete_device

Parameter: `index` [int]

Delete the device at the given index.

### insert_device

Parameters: `device_name` [symbol] `target_index` [int] (optional)

Attempts to insert the device specified by `device_name` at the given index in the chain. If no index is provided, attempts to insert the device at the end. Throws an error if insertion is not possible.

`device_name` is the name as it appears in the UI of Live.

Not all indices are valid. As can be expected, indices outside of the range defined by the current length of the device chain are invalid, but there are other limitations: for example, a MIDI effect can't be inserted after an instrument. The rule of thumb is that if an index would be invalid when inserting using the mouse, it's invalid here.

At the moment, only native Live devices can be inserted. Max for Live devices and plug-in are not supported.

_Available since Live 12.3._
