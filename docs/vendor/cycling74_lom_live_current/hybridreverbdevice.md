---
source_url: "https://docs.cycling74.com/apiref/lom/hybridreverbdevice/"
fetched_at: "2026-06-21T21:07:43.8676568-04:00"
---
# HybridReverbDevice

This class represents an instance of a Hybrid Reverb device in Live.

A HybridReverbDevice has all the properties, functions and children of a Device. Listed below are members unique to HybridReverbDevice.

## Properties

### ir_attack_time floatobserve

The attack time of the amplitude envelope for the impulse response, in seconds.

### ir_category_index intobserve

The index of the selected impulse response category.

### ir_category_list StringVectorread-only

The list of impulse response categories.

### ir_decay_time floatobserve

The decay time of the amplitude envelope for the impulse response, in seconds.

### ir_file_index intobserve

The index of the selected impulse response files from the current category.

### ir_file_list StringVectorread-onlyobserve

The list of impulse response files from the selected category.

### ir_size_factor floatobserve

The relative size of the impulse response, 0.0 to 1.0.

### ir_time_shaping_on boolobserve

Enables transforming the current selected impulse response with an amplitude envelope and size parameter.

1 = enabled.
