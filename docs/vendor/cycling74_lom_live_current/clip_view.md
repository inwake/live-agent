---
source_url: "https://docs.cycling74.com/apiref/lom/clip_view/"
fetched_at: "2026-06-21T21:07:01.9030031-04:00"
---
# Clip.View

Representing the view aspects of a Clip.

## Canonical Path

```clike
live_set tracks N clip_slots M clip view
```

## Properties

### grid_is_triplet bool

Get/set whether the clip is displayed with a triplet grid.

### grid_quantization int

Get/set the grid quantization.

## Functions

### hide_envelope

Hide the Envelopes box.

### select_envelope_parameter

Parameter: [DeviceParameter]

Select the specified device parameter in the Envelopes box.

### show_envelope

Show the Envelopes box.

### show_loop

If the clip is visible in Live's Detail View, this function will make the current loop visible there.
