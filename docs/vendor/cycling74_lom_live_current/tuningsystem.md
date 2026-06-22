---
source_url: "https://docs.cycling74.com/apiref/lom/tuningsystem/"
fetched_at: "2026-06-21T21:08:29.0289328-04:00"
---
# TuningSystem

This class represents a tuning system in Live.

## Canonical Path

```clike
live_set tuning_system
```

## Properties

### name symbolobserve

The name of the currently active tuning system.

### pseudo_octave_in_cents floatread-only

The pseudo octave in cents of the currently active tuning system.

### lowest_note dictionaryobserve

The note index within the pseudo octave and octave of the lowest note.

### highest_note dictionaryobserve

The note index within the pseudo octave and octave of the highest note.

### reference_pitch dictionaryobserve

The reference pitch of the current tuning system.

### note_tunings dictionaryobserve

The relative note tunings of the Tuning System in cents. Provided as a single-element dictionary holding an array.
