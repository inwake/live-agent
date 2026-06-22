---
source_url: "https://docs.cycling74.com/apiref/lom/groove/"
fetched_at: "2026-06-21T21:07:38.7494644-04:00"
---
# Groove

This class represents a groove in Live.

_Available since Live 11.0._

All grooves are stored in Live's groove pool.

## Canonical Paths

```clike
live_set groove_pool grooves N
```

```clike
live_set tracks N clip_slots M clip groove
```

## Children

### base int

Get/set the groove's base grid (index based setter).

0 = 1/4

1 = 1/8

2 = 1/8T

3 = 1/16

4 = 1/16T

5 = 1/32

### name symbolobserve

Get/set/observe the name of the groove.

### quantization_amount floatobserve

Get/set/observe the groove's quantization amount.

### random_amount floatobserve

Get/set/observe the groove's random amount.

### timing_amount floatobserve

Get/set/observe the groove's timing amount.

### velocity_amount floatobserve

Get/set/observe the groove's velocity amount.
