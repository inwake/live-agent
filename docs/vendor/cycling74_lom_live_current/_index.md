---
source_url: "https://docs.cycling74.com/apiref/lom/"
fetched_at: "2026-06-21T21:06:51.8619034-04:00"
---
# LOM - The Live Object Model

_Objects which comprise the Live API described by their structure, properties and functions._
The Live Object Model lists a number of Live object classes with their properties and functions, as well as their parent-child relations through which a hierarchy is formed. Please refer to the [Live API overview chapter](https://docs.cycling74.com/userguide/m4l/live_api/) for definitions of the basic Live API terms and a list of the Max objects used to access it.

_This document refers to Ableton Live version 12.3.5_

## Object Model Overview

| _Click on the classes to navigate to their description._ |
| --- |

Expand

## API Objects

| Item | Description |
| --- | --- |
| [Application](https://docs.cycling74.com/apiref/lom/application/) | This class represents the Live application. It is reachable by the root path live_app ... |
| [Application.View](https://docs.cycling74.com/apiref/lom/application_view/) | This class represents the aspects of the Live application related to viewing the application.... |
| [Chain](https://docs.cycling74.com/apiref/lom/chain/) | This class represents a group device chain in Live. |
| [ChainMixerDevice](https://docs.cycling74.com/apiref/lom/chainmixerdevice/) | This class represents a chain's mixer device in Live. |
| [Clip](https://docs.cycling74.com/apiref/lom/clip/) | This class represents a clip in Live. It can be either an audio clip or a MIDI clip in the Arr... |
| [Clip.View](https://docs.cycling74.com/apiref/lom/clip_view/) | Representing the view aspects of a Clip. |
| [ClipSlot](https://docs.cycling74.com/apiref/lom/clipslot/) | This class represents an entry in Live's Session View matrix. The properties ... |
| [CompressorDevice](https://docs.cycling74.com/apiref/lom/compressordevice/) | This class represents a Compressor device in Live. A CompressorDevice shares all of the ch... |
| [ControlSurface](https://docs.cycling74.com/apiref/lom/controlsurface/) | A ControlSurface can be reached either directly by the root path control_surfaces N or by g... |
| [CuePoint](https://docs.cycling74.com/apiref/lom/cuepoint/) | Represents a locator in the Arrangement View. |
| [Device](https://docs.cycling74.com/apiref/lom/device/) | This class represents a MIDI or audio device in Live. |
| [Device.View](https://docs.cycling74.com/apiref/lom/device_view/) | Representing the view aspects of a Device. |
| [DeviceIO](https://docs.cycling74.com/apiref/lom/deviceio/) | This class represents an input or output bus of a Live device. |
| [DeviceParameter](https://docs.cycling74.com/apiref/lom/deviceparameter/) | This class represents an (automatable) parameter within a MIDI or audio device. To modify a de... |
| [DriftDevice](https://docs.cycling74.com/apiref/lom/driftdevice/) | This class represents an instance of a Drift device in Live. A DriftDevice has all the... |
| [DrumCellDevice](https://docs.cycling74.com/apiref/lom/drumcelldevice/) | This class represents an instance of a Drum Sampler device in Live. A DrumCell has all... |
| [DrumChain](https://docs.cycling74.com/apiref/lom/drumchain/) | This class represents a Drum Rack device chain in Live. A DrumChain is a type ... |
| [DrumPad](https://docs.cycling74.com/apiref/lom/drumpad/) | This class represents a Drum Rack pad in Live. |
| [Eq8Device](https://docs.cycling74.com/apiref/lom/eq8device/) | This class represents an instance of an EQ Eight device in Live. An Eq8Device has all ... |
| [Eq8Device.View](https://docs.cycling74.com/apiref/lom/eq8device_view/) | Represents the view aspects of an Eq8Device. An Eq8Device.View has all the children, p... |
| [Groove](https://docs.cycling74.com/apiref/lom/groove/) | This class represents a groove in Live. Available since Live 11.0. ... |
| [GroovePool](https://docs.cycling74.com/apiref/lom/groovepool/) | This class represents the groove pool in Live. It provides access to the current set's list of groov... |
| [HybridReverbDevice](https://docs.cycling74.com/apiref/lom/hybridreverbdevice/) | This class represents an instance of a Hybrid Reverb device in Live. A HybridReverbDev... |
| [LooperDevice](https://docs.cycling74.com/apiref/lom/looperdevice/) | This class represents an instance of a Looper device in Live. An LooperDevice has all ... |
| [MaxDevice](https://docs.cycling74.com/apiref/lom/maxdevice/) | This class represents a Max for Live device in Live. A MaxDevice is a type of Device... |
| [MeldDevice](https://docs.cycling74.com/apiref/lom/melddevice/) | This class represents an instance of a Meld device in Live. A MeldDevice has all the p... |
| [MixerDevice](https://docs.cycling74.com/apiref/lom/mixerdevice/) | This class represents a mixer device in Live. It provides access to volume, panning and other ... |
| [PluginDevice](https://docs.cycling74.com/apiref/lom/plugindevice/) | This class represents a plug-in device. A PluginDevice is a type of Device, meaning ... |
| [RackDevice](https://docs.cycling74.com/apiref/lom/rackdevice/) | This class represents a Live Rack Device. A RackDevice is a type of Device, meaning th... |
| [RackDevice.View](https://docs.cycling74.com/apiref/lom/rackdevice_view/) | Represents the view aspects of a Rack Device. A RackDevice.View is a type of Device.Vi... |
| [RoarDevice](https://docs.cycling74.com/apiref/lom/roardevice/) | This class represents an instance of a Roar device in Live. A RoarDevice has all the p... |
| [Sample](https://docs.cycling74.com/apiref/lom/sample/) | This class represents a sample file loaded into Simpler. |
| [Scene](https://docs.cycling74.com/apiref/lom/scene/) | This class represents a series of clip slots in Live's Session View matrix.... |
| [ShifterDevice](https://docs.cycling74.com/apiref/lom/shifterdevice/) | This class represents an instance of the Shifter audio effect. A ShifterDevice is a ty... |
| [SimplerDevice](https://docs.cycling74.com/apiref/lom/simplerdevice/) | This class represents an instance of Simpler. A SimplerDevice is a type of device, mea... |
| [SimplerDevice.View](https://docs.cycling74.com/apiref/lom/simplerdevice_view/) | Represents the view aspects of a SimplerDevice. A SimplerDevice.View is a type of Device.V... |
| [Song](https://docs.cycling74.com/apiref/lom/song/) | This class represents a Live Set. The current Live Set is reachable by the root path li... |
| [Song.View](https://docs.cycling74.com/apiref/lom/song_view/) | This class represents the view aspects of a Live document: the Session and Arrangement Views.... |
| [SpectralResonatorDevice](https://docs.cycling74.com/apiref/lom/spectralresonatordevice/) | This class represents an instance of a Spectral Resonator device in Live. An SpectralR... |
| [TakeLane](https://docs.cycling74.com/apiref/lom/takelane/) | This class represents a take lane in Live. Tracks in Live can have take lanes in Arrangement View, w... |
| [this_device](https://docs.cycling74.com/apiref/lom/this_device/) | This root path represents the device containing the live.path object to which the ... |
| [Track](https://docs.cycling74.com/apiref/lom/track/) | This class represents a track in Live. It can either be an audio track, a MIDI track, a return... |
| [Track.View](https://docs.cycling74.com/apiref/lom/track_view/) | Representing the view aspects of a track. |
| [TuningSystem](https://docs.cycling74.com/apiref/lom/tuningsystem/) | This class represents a tuning system in Live. |
| [WavetableDevice](https://docs.cycling74.com/apiref/lom/wavetabledevice/) | This class represents a Wavetable instrument. A WavetableDevice shares all of the ch... |
