---
source_url: "https://docs.cycling74.com/apiref/lom/wavetabledevice/"
fetched_at: "2026-06-21T21:08:31.0898128-04:00"
---
# WavetableDevice

This class represents a Wavetable instrument.

A WavetableDevice shares all of the children, functions and properties that a Device has. Listed below are members unique to it.

## Properties

### filter_routing intobserve

Access to the current filter routing. 0 = Serial, 1 = Parallel, 2 = Split.

### mono_poly intobserve

Access to Wavetable's Poly/Mono switch. 0 = Mono, 1 = Poly.

### oscillator_1_effect_mode intobserve

Access to oscillator 1's effect mode. 0 = None, 1 = Fm, 2 = Classic, 3 = Modern.

### oscillator_2_effect_mode intobserve

Access to oscillator 2's effect mode.

### oscillator_1_wavetable_category observe

Access to oscillator 1's wavetable category selector.

### oscillator_2_wavetable_category observe

Access to oscillator 2's wavetable category selector.

### oscillator_1_wavetable_index observe

Access to oscillator 1's wavetable index selector.

### oscillator_2_wavetable_index observe

Access to oscillator 2's wavetable index selector.

### oscillator_1_wavetables StringVectorread-onlyobserve

List of names of the wavetables currently available for oscillator 1. Depends on the current wavetable category selection (see _oscillator_1_wavetable_category_).

### oscillator_2_wavetables StringVectorread-onlyobserve

List of names of the wavetables currently available for oscillator 2. Depends on the current wavetable category selection (see _oscillator_2_wavetable_category_).

### oscillator_wavetable_categories StringVectorread-only

List of the names of the available wavetable categories.

### poly_voices intobserve

The current number of polyphonic voices.

### unison_mode intobserve

Access to Wavetable's unison mode parameter.

0 = None

1 = Classic

2 = Shimmer

3 = Noise

4 = Phase Sync

5 = Position Spread

6 = Random Note

### unison_voice_count intobserve

Access to the number of unison voices.

### visible_modulation_target_names StringVectorread-onlyobserve

List of the names of modulation targets currently visible in the modulation matrix.

## Functions

### add_parameter_to_modulation_matrix

Parameter: `parameter_to_add` [DeviceParameter]

Add an instrument parameter to the modulation matrix. Only works for parameters that can be modulated (see _is_parameter_modulatable_).

### get_modulation_target_parameter_name

Parameter: `index` [int]

Return the modulation target parameter name at _index_ in the modulation matrix as a [symbol].

### get_modulation_value

Parameters: `modulation_target_index` [int] `modulation_source_index` [int]

Return the amount of the modulation of the parameter at `modulation_target_index` by the modulation source at `modulation_source_index` in Wavetable's modulation matrix.

### is_parameter_modulatable

Parameter: `parameter` [DeviceParameter]

1 = `parameter` can be modulated. Call this before `add_parameter_to_modulation_matrix`.

### set_modulation_value

Parameters: `modulation_target_index` [int] `modulation_source_index` [int]

Set the amount of the modulation of the parameter at `modulation_target_index` by the modulation source at `modulation_source_index` in Wavetable's modulation matrix.
