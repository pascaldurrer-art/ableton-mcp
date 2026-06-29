"""Device profile for Ableton Compressor (class_name: "Compressor2").

Parameter indices are approximate and should be verified against a live
session via get_device_parameters before relying on them.
"""

PROFILE = {
    "meta": {
        "class_name":       "Compressor2",
        "display_name":     "Compressor",
        "vendor":           "Ableton",
        "version":          "1.0",
        "ableton_version":  "12.2.6",
        "parameter_count":  None,
        "notes": "Parameter indices not yet verified. Run get_device_parameters to confirm.",
    },

    "capabilities": {
        "supports_threshold":   True,
        "supports_ratio":       True,
        "supports_attack":      True,
        "supports_release":     True,
        "supports_gain":        True,
        "supports_knee":        True,
        "supports_sidechain":   True,
        "supports_lookahead":   True,
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
        "threshold": {
            "index": 1,
            "min": -36.0, "max": 0.0, "unit": "dB",
            "description": "Compression threshold",
            "confirmed": False,
        },
        "ratio": {
            "index": 2,
            "min": 1.0, "max": 10.0, "unit": ":1",
            "description": "Compression ratio",
            "confirmed": False,
        },
        "attack": {
            "index": 3,
            "min": 0.01, "max": 200.0, "unit": "ms",
            "description": "Attack time",
            "confirmed": False,
        },
        "release": {
            "index": 4,
            "min": 1.0, "max": 1200.0, "unit": "ms",
            "description": "Release time (set to 0 for Auto)",
            "confirmed": False,
        },
        "gain": {
            "index": 5,
            "min": -12.0, "max": 12.0, "unit": "dB",
            "description": "Output gain (makeup gain)",
            "confirmed": False,
        },
        "knee": {
            "index": 6,
            "min": 0.0, "max": 24.0, "unit": "dB",
            "description": "Knee width",
            "confirmed": False,
        },
    },

    "groups": {
        "dynamics":  ["threshold", "ratio", "knee"],
        "timing":    ["attack", "release"],
        "output":    ["gain"],
        "global":    ["device_on"],
    },
}
