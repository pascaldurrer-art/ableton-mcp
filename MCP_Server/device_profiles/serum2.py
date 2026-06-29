"""Device profile for Xfer Records Serum 2 VST (class_name: "Serum2").

Serum 2 exposes 400-700 parameters depending on version and configuration.
Parameter indices are highly plugin-version-dependent and cannot be
determined without inspecting a live session via get_device_parameters.

This profile defines capabilities and known parameter groups only.
Actual indices must be retrieved at runtime.
"""

PROFILE = {
    "meta": {
        "class_name":       "Serum2",
        "display_name":     "Serum 2",
        "vendor":           "Xfer Records",
        "version":          "1.0",
        "plugin_version":   None,
        "ableton_version":  "12.2.6",
        "parameter_count":  None,
        "notes": (
            "VST plugin. Parameter indices vary between plugin versions "
            "and cannot be statically mapped. Use get_device_parameters() "
            "to retrieve the current parameter list at runtime, then "
            "reference by index from that response."
        ),
    },

    "capabilities": {
        "supports_oscillators":     True,
        "supports_filters":         True,
        "supports_envelopes":       True,
        "supports_lfo":             True,
        "supports_effects":         True,
        "supports_modulation":      True,
        "supports_wavetables":      True,
        "supports_unison":          True,
        "supports_mid_side":        False,
        "supports_dynamic":         False,
    },

    "parameters": {},

    "groups": {
        "note": (
            "Serum 2 has no static parameter map in this profile. "
            "Retrieve parameters at runtime with get_device_parameters(), "
            "then use parameter_index values from that response to call "
            "set_device_parameter or set_multiple_device_parameters."
        ),
    },
}
