---
source_url: "https://docs.cycling74.com/apiref/lom/device/"
fetched_at: "2026-06-21T21:07:18.1239217-04:00"
---
# Device

This class represents a MIDI or audio device in Live.

## Canonical Paths

```clike
live_set tracks N devices M
```

```clike
live_set tracks N devices M chains L devices K
```

```clike
live_set tracks N devices M return_chains L devices K
```

## Children

### parameters list of [DeviceParameter](https://docs.cycling74.com/apiref/lom/deviceparameter/ "DeviceParameter")read-onlyobserve

Only automatable parameters are accessible. See [DeviceParameter](https://docs.cycling74.com/apiref/lom/device/#DeviceParameter) to learn how to modify them.

### view [Device.View](https://docs.cycling74.com/apiref/lom/device_view/ "Device.View")read-only

## Properties

### can_have_chains boolread-only

0 for a single device

1 for a device Rack

### can_have_drum_pads boolread-only

1 for Drum Racks

### class_display_name symbolread-only

Get the original name of the device (e.g. `Operator`, `Auto Filter`).

### class_name symbolread-only

Live device type such as `MidiChord`, `Operator`, `Limiter`, `MxDeviceAudioEffect`, or `PluginDevice`.

### is_active boolread-onlyobserve

0 = either the device itself or its enclosing Rack device is off.

### name symbolobserve

This is the string shown in the title bar of the device.

### type intread-only

The type of the device. Possible types are: 0 = undefined, 1 = instrument, 2 = audio_effect, 4 = midi_effect.

### latency_in_samples intread-onlyobserve

Device latency in samples.

### latency_in_ms floatread-onlyobserve

Device latency in milliseconds.

### can_compare_ab boolread-only

1 for devices that support the AB Compare feature. 0 otherwise.

_Available since Live 12.3._

### is_using_compare_preset_b boolobserve

1 if the device has compare preset B loaded. 0 otherwise.

(Only relevant if _can_compare_ab_, otherwise errors.)

_Available since Live 12.3._

## Functions

### store_chosen_bank

Parameters:

`script_index` [int]

`bank_index` [int]

(This is related to hardware control surfaces and is usually not relevant.)

### save_preset_to_compare_ab_slot

Save the device state to the other compare AB slot.

(Only relevant if _can_compare_ab_, otherwise errors.)

_Available since Live 12.3._
