---
source_url: "https://docs.cycling74.com/apiref/lom/application/"
fetched_at: "2026-06-21T21:06:55.8364405-04:00"
---
# Application

This class represents the Live application. It is reachable by the root path `live_app`.

## Canonical Path

```clike
live_app
```

## Children

### view [Application.View](https://docs.cycling74.com/apiref/lom/application_view/ "Application.View")read-only

### control_surfaces list of [ControlSurface](https://docs.cycling74.com/apiref/lom/controlsurface/ "ControlSurface")read-onlyobserve

A list of the control surfaces currently selected in Live's Preferences.

If None is selected in any of the slots or the script is inactive (e.g. when Push2 is selected, but no Push is connected), id 0 will be returned at those indices.

## Properties

### current_dialog_button_count intread-only

The number of buttons in the current message box.

### current_dialog_message symbolread-only

The text of the current message box (empty if no message box is currently shown).

### open_dialog_count intread-onlyobserve

The number of dialog boxes shown.

### average_process_usage floatread-onlyobserve

Reports Live's average CPU load.

Note that Live's CPU meter shows the audio processing load but not Live's overall CPU usage.

### peak_process_usage floatread-onlyobserve

Reports Live's peak CPU load.

Note that Live's CPU meter shows the audio processing load but not Live's overall CPU usage.

## Functions

### get_bugfix_version

Returns: the 2 in Live 9.1.2.

### get_document

Returns: the current Live Set.

### get_major_version

Returns: the 9 in Live 9.1.2.

### get_minor_version

Returns: the 1 in Live 9.1.2.

### get_version_string

Returns: the text 9.1.2 in Live 9.1.2.

### press_current_dialog_button

Parameter: `index`

Press the button with the given index in the current dialog box.
