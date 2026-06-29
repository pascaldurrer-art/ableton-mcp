"""Device profile for Ableton Saturator (class_name: "Saturator").

Parameter indices are approximate and should be verified against a live
session via get_device_parameters before relying on them.
"""

PROFILE = {
    "meta": {
        "class_name":       "Saturator",
        "display_name":     "Saturator",
        "vendor":           "Ableton",
        "version":          "1.0",
        "ableton_version":  "12.2.6",
        "parameter_count":  None,
        "notes": "Parameter indices not yet verified. Run get_device_parameters to confirm.",
    },

    "capabilities": {
        "supports_drive":           True,
        "supports_gain":            True,
        "supports_saturation_type": True,
        "supports_waveshaping":     True,
        "supports_dry_wet":         True,
        "supports_mid_side":        False,
        "supports_dynamic":         False,
    },

    "parameters": {
        "device_on": {
            "index": 0,
            "quantized": True,
            "choices": ["Off", "On"],
            "description": "Enable/disable the device",
        },
        "drive": {
            "index": 1,
            "min": 0.0, "max": 1.0, "unit": None,
            "description": "Drive/saturation intensity",
            "confirmed": False,
        },
        "type": {
            "index": 2,
            "quantized": True,
            "choices": ["Analog Clip", "Soft Sine", "Medium Curve",
                        "Hard Curve", "Sinoid Fold", "Digital Clip"],
            "description": "Saturation curve type",
            "confirmed": False,
        },
        "base": {
            "index": 3,
            "min": 0.0, "max": 1.0, "unit": None,
            "description": "Waveshaper base (for Soft/Medium/Hard modes)",
            "confirmed": False,
        },
        "freq": {
            "index": 4,
            "min": 10.0, "max": 22050.0, "unit": "Hz",
            "description": "Waveshaper frequency parameter",
            "confirmed": False,
        },
        "width": {
            "index": 5,
            "min": 0.0, "max": 1.0, "unit": None,
            "description": "Waveshaper width",
            "confirmed": False,
        },
        "output_gain": {
            "index": 6,
            "min": -12.0, "max": 12.0, "unit": "dB",
            "description": "Output gain",
            "confirmed": False,
        },
        "dry_wet": {
            "index": 7,
            "min": 0.0, "max": 1.0, "unit": None,
            "description": "Dry/wet mix (0 = dry, 1 = full wet)",
            "confirmed": False,
        },
    },

    "groups": {
        "saturation": ["drive", "type", "base", "freq", "width"],
        "output":     ["output_gain", "dry_wet"],
        "global":     ["device_on"],
    },
}
