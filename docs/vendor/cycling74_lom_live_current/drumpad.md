---
source_url: "https://docs.cycling74.com/apiref/lom/drumpad/"
fetched_at: "2026-06-21T21:07:31.7414775-04:00"
---
# DrumPad

This class represents a Drum Rack pad in Live.

## Canonical Path

```clike
live_set tracks N devices M drum_pads L
```

## Children

### chains [Chain](https://docs.cycling74.com/apiref/lom/chain/ "Chain")read-onlyobserve

## Properties

### mute boolobserve

1 = muted

### name symbolread-onlyobserve

### note intread-only

### solo boolobserve

1 = soloed (Solo switch on)

Does not automatically turn Solo off in other chains.

## Functions

### delete_all_chains
