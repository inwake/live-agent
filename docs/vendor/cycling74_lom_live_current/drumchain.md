---
source_url: "https://docs.cycling74.com/apiref/lom/drumchain/"
fetched_at: "2026-06-21T21:07:29.6795664-04:00"
---
# DrumChain

This class represents a Drum Rack device chain in Live.

A DrumChain is a type of Chain, meaning that it has all the children, properties and functions that a Chain has. Listed below are the members unique to DrumChain.

## Properties

### in_note intobserve

Get/set the MIDI note that will trigger this chain. The value -1 corresponds to the "All Notes" setting in the UI.

_Available since Live 12.3_

### out_note intobserve

Get/set the MIDI note sent to the devices in the chain.

### choke_group intobserve

Get/set the chain's choke group.
