"""Device profile for Ableton Utility (class_name: "AutoFilter" or "Utility").

Note: Ableton's Utility device class_name may vary by Live version.
Verify with get_track_info before use.
Parameter indices are approximate and should be verified.
"""

PROFILE = {
    "meta": {
        "class_name":       "Utility",
        "display_name":     "Utility",
        "vendor":           "Ableton",
        "version":          "1.0",
        "ableton_version":  "12.2.6",
        "parameter_count":  None,
        "notes": (
            "class_name may differ across Live versions. "
            "Parameter indices not yet verified."
        ),
    },

    "capabilities": {
        "supports_gain":        True,
        "supports_panning":     True,
        "supports_width":       True,
        "supports_mono":        True,
        "supports_mute":        True,
        "supports_mid_side":    False,
        "supports_dynamic":     False,
    },

    "parameters": {
        "device_on": {
            "index": 0,
            "quantized": True,
            "choices": ["Off", "On"],
            "description": "Enable/disable the device",
        },
        "gain": {
            "index": 1,
            "min": 0.0, "max": 4.0, "unit": "linear",
            "description": "Input gain (linear, 1.0 = 0 dB)",
            "confirmed": False,
        },
        "panning": {
            "index": 2,
            "min": -1.0, "max": 1.0, "unit": None,
            "description": "Stereo panning (-1 = full left, +1 = full right)",
            "confirmed": False,
        },
        "width": {
            "index": 3,
            "min": 0.0, "max": 2.0, "unit": None,
            "description": "Stereo width (0 = mono, 1 = unchanged, 2 = wide)",
            "confirmed": False,
        },
        "mono": {
            "index": 4,
            "quantized": True,
            "choices": ["Off", "On"],
            "description": "Collapse to mono",
            "confirmed": False,
        },
        "mute": {
            "index": 5,
            "quantized": True,
            "choices": ["Off", "On"],
            "description": "Mute the signal",
            "confirmed": False,
        },
    },

    "groups": {
        "level":    ["gain", "mute"],
        "stereo":   ["panning", "width", "mono"],
        "global":   ["device_on"],
    },
}
