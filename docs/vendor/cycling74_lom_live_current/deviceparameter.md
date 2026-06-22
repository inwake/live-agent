---
source_url: "https://docs.cycling74.com/apiref/lom/deviceparameter/"
fetched_at: "2026-06-21T21:07:22.5157272-04:00"
---
# DeviceParameter

This class represents an (automatable) parameter within a MIDI or audio device. To modify a device parameter, set its `value` property or send its object ID to [live.remote~](https://docs.cycling74.com/reference/live.remote~ "live.remote~").

## Canonical Path

```clike
live_set tracks N devices M parameters L
```

## Properties

### automation_state intread-onlyobserve

Get the automation state of the parameter.

0 = no automation.

1 = automation active.

2 = automation overridden.

### default_value floatread-only

Get the default value for this parameter.

Only available for parameters that aren't quantized (see _is_quantized_).

### is_enabled boolread-only

1 = the parameter value can be modified directly by the user, by sending `set` to a [live.object](https://docs.cycling74.com/reference/live.object "live.object"), by automation or by an assigned MIDI message or keystroke.

Parameters can be disabled because they are macro-controlled, or they are controlled by a live-remote~ object, or because Live thinks that they should not be moved.

### is_quantized boolread-only

1 for booleans and enums

0 for int/float parameters

Although parameters like MidiPitch.Pitch appear quantized to the user, they actually have an is_quantized value of 0.

### max floatread-only

Largest allowed value.

### min floatread-only

Lowest allowed value.

### name symbolread-only

The short parameter name as shown in the (closed) automation chooser.

### original_name symbolread-only

The name of a Macro parameter before its assignment.

### state intread-onlyobserve

The active state of the parameter.

0 = the parameter is active and can be changed.

1 = the parameter can be changed but isn't active, so changes won't have an audible effect.

2 = the parameter cannot be changed.

### value floatobserve

The internal value between min and max. Use display_value for the value as visible in the GUI.

### display_value floatobserve

The value as visible in the GUI.

### value_items StringVectorread-only

Get a list of the possible values for this parameter.

Only available for parameters that are quantized (see _is_quantized_).

## Functions

### re_enable_automation

Re-enable automation for this parameter.

### str_for_value

Parameter: `value` [float] Returns: [symbol] String representation of the specified value.

### __str__

Returns: [symbol] String representation of the current parameter value.
