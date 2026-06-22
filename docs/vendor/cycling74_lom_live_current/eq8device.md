---
source_url: "https://docs.cycling74.com/apiref/lom/eq8device/"
fetched_at: "2026-06-21T21:07:36.3751320-04:00"
---
# Eq8Device

This class represents an instance of an EQ Eight device in Live.

An Eq8Device has all the properties, functions and children of a Device. Listed below are members unique to Eq8Device.

## Properties

### edit_mode boolobserve

Access to EQ Eight's edit mode, which toggles the channel currently available for editing. The available edit modes depend on the global mode (see `global_mode`) and are encoded as follows:

In L/R mode: 0 = L, 1 = R

In M/S mode: 0 = M, 1 = S

In Stereo mode: 0 = A, 1 = B (inactive)

### global_mode intobserve

Access to EQ Eight's global mode. The modes are encoded as follows:

0 = Stereo

1 = L/R

2 = M/S

### oversample boolobserve

Access to EQ Eight's Oversampling parameter. 0 = Off, 1 = On.
