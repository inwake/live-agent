# Plugin parameter limits

Do not claim full arbitrary VST3 control.

The clean v1 boundary is: this project can read and set parameters exposed to Ableton Live as `DeviceParameter` objects. Commercial plugins often contain many internal parameters that are not exposed to Live's parameter list until configured or made available by the plugin.

## Supported

- List `Device.parameters`.
- Read parameter metadata: name, original name, value, display value, min, max, automation state where available.
- Set parameter value when the parameter is exposed and enabled.
- Diagnose when a plugin exposes zero or suspiciously few parameters.

## Not supported in v1

- Full VST3 internal parameter enumeration.
- Reading plugin-specific hidden state.
- Reading arbitrary GUI knob state.
- Opening the plugin GUI and scraping it.
- Pretending Options.txt removes all plugin limits.

## Optional helper

A later helper can generate an `Options.txt` recommendation for `-_PluginAutoPopulateThreshold=128`, but this must be framed as an unsupported Ableton option with a max of 128 exposed plugin parameters.
