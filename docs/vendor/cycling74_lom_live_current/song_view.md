---
source_url: "https://docs.cycling74.com/apiref/lom/song_view/"
fetched_at: "2026-06-21T21:08:13.7971115-04:00"
---
# Song.View

This class represents the view aspects of a Live document: the Session and Arrangement Views.

## Canonical Path

```clike
live_set view
```

## Children

### detail_clip [Clip](https://docs.cycling74.com/apiref/lom/clip/ "Clip")observe

The clip currently displayed in the Live application's Detail View.

### highlighted_clip_slot [ClipSlot](https://docs.cycling74.com/apiref/lom/clipslot/ "ClipSlot")

The slot highlighted in the Session View.

### selected_chain [Chain](https://docs.cycling74.com/apiref/lom/chain/ "Chain")observe

The highlighted chain, or "id 0"

### selected_parameter [DeviceParameter](https://docs.cycling74.com/apiref/lom/deviceparameter/ "DeviceParameter")read-onlyobserve

The selected parameter, or "id 0"

### selected_scene [Scene](https://docs.cycling74.com/apiref/lom/scene/ "Scene")observe

### selected_track [Track](https://docs.cycling74.com/apiref/lom/track/ "Track")observe

## Properties

### draw_mode boolobserve

Reflects the state of the envelope/automation Draw Mode Switch in the transport bar, as toggled with Cmd/Ctrl-B.

0 = breakpoint editing (shows arrow), 1 = drawing (shows pencil)

### follow_song boolobserve

Reflects the state of the Follow switch in the transport bar as toggled with Cmd/Ctrl-F.

0 = don't follow playback position, 1 = follow playback position

## Functions

### select_device

Parameter: `id NN`

Selects the given device object in its track.

You may obtain the id using a [live.path](https://docs.cycling74.com/reference/live.path "live.path") or by using `get devices` on a track, for example.

The track containing the device will not be shown automatically, and the device gets the appointed device (blue hand) only if its track is selected.
