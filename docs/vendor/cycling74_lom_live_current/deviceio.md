---
source_url: "https://docs.cycling74.com/apiref/lom/deviceio/"
fetched_at: "2026-06-21T21:07:20.3233831-04:00"
---
# DeviceIO

This class represents an input or output bus of a Live device.

## Properties

### available_routing_channels dictionaryread-onlyobserve

The available channels for this input/output bus. The channels are represented as a _dictionary_ with the following key:

`available_routing_channels` [list]

The list contains _dictionaries_ as described in _routing_channel_.

### available_routing_types dictionaryread-onlyobserve

The available types for this input/output bus. The types are represented as a _dictionary_ with the following key:

`available_routing_types` [list]

The list contains _dictionaries_ as described in _routing_type_.

### default_external_routing_channel_is_none bool

1 = the default routing channel for External routing types is none.

_Available since Live 11.0._

### routing_channel dictionaryobserve

The current routing channel for this input/output bus. It is represented as a _dictionary_ with the following keys:

`display_name` [symbol]

`identifier` [symbol]

Can be set to any of the values found in _available_routing_channels._

### routing_type dictionaryobserve

The current routing type for this input/output bus. It is represented as a _dictionary_ with the following keys:

`display_name` [symbol]

`identifier` [symbol]

Can be set to any of the values found in _available_routing_types._
