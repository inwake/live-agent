---
source_url: "https://docs.cycling74.com/apiref/lom/mixerdevice/"
fetched_at: "2026-06-21T21:07:52.4470231-04:00"
---
# MixerDevice

This class represents a mixer device in Live. It provides access to volume, panning and other [DeviceParameter](https://docs.cycling74.com/apiref/lom/mixerdevice/#DeviceParameter) objects. See [DeviceParameter](https://docs.cycling74.com/apiref/lom/mixerdevice/#DeviceParameter) to learn how to modify them.

## Canonical Path

```clike
live_set tracks N mixer_device
```

## Children

### sends list of [DeviceParameter](https://docs.cycling74.com/apiref/lom/deviceparameter/ "DeviceParameter")read-onlyobserve

One send per return track.

### cue_volume [DeviceParameter](https://docs.cycling74.com/apiref/lom/deviceparameter/ "DeviceParameter")read-only

[in master track only]

### crossfader [DeviceParameter](https://docs.cycling74.com/apiref/lom/deviceparameter/ "DeviceParameter")read-only

[in master track only]

### left_split_stereo [DeviceParameter](https://docs.cycling74.com/apiref/lom/deviceparameter/ "DeviceParameter")read-only

The Track's Left Split Stereo Pan Parameter.

### panning [DeviceParameter](https://docs.cycling74.com/apiref/lom/deviceparameter/ "DeviceParameter")read-only

### right_split_stereo [DeviceParameter](https://docs.cycling74.com/apiref/lom/deviceparameter/ "DeviceParameter")read-only

The Track's Right Split Stereo Pan Parameter.

### song_tempo [DeviceParameter](https://docs.cycling74.com/apiref/lom/deviceparameter/ "DeviceParameter")read-only

[in master track only]

### track_activator [DeviceParameter](https://docs.cycling74.com/apiref/lom/deviceparameter/ "DeviceParameter")read-only

### volume [DeviceParameter](https://docs.cycling74.com/apiref/lom/deviceparameter/ "DeviceParameter")read-only

## Properties

### crossfade_assign intobserve

0 = A, 1 = none, 2 = B [not in master track]

### panning_mode intobserve

Access to the Track mixer's pan mode: 0 = Stereo, 1 = Split Stereo.
