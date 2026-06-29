"""Device profile for Ableton Drum Buss (class_name: "DrumBuss").

Parameter indices are approximate and should be verified against a live
session via get_device_parameters before relying on them.
"""

PROFILE = {
    "meta": {
        "class_name":       "DrumBuss",
        "display_name":     "Drum Buss",
        "vendor":           "Ableton",
        "version":          "1.0",
        "ableton_version":  "12.2.6",
        "parameter_count":  None,
        "notes": "Parameter indices not yet verified. Run get_device_parameters to confirm.",
    },

    "capabilities": {
        "supports_gain":        True,
        "supports_drive":       True,
        "supports_crunch":      True,
        "supports_transients":  True,
        "supports_boom":        True,
        "supports_room":        True,
        "supports_high_pass":   True,
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
        "drive": {
            "index": 1,
            "min": 0.0, "max": 1.0, "unit": None,
            "description": "Saturation/drive amount",
            "confirmed": False,
        },
        "crunch": {
            "index": 2,
            "min": 0.0, "max": 1.0, "unit": None,
            "description": "High-frequency crunch amount",
            "confirmed": False,
        },
        "transients": {
            "index": 3,
            "min": -1.0, "max": 1.0, "unit": None,
            "description": "Transient shaping (negative = softer, positive = snappier)",
            "confirmed": False,
        },
        "boom_freq": {
            "index": 4,
            "min": 20.0, "max": 200.0, "unit": "Hz",
            "description": "Boom frequency center",
            "confirmed": False,
        },
        "boom_amount": {
            "index": 5,
            "min": 0.0, "max": 1.0, "unit": None,
            "description": "Boom (low-end emphasis) amount",
            "confirmed": False,
        },
        "room": {
            "index": 6,
            "min": 0.0, "max": 1.0, "unit": None,
            "description": "Room reverb amount",
            "confirmed": False,
        },
        "high_pass": {
            "index": 7,
            "min": 20.0, "max": 500.0, "unit": "Hz",
            "description": "High-pass filter frequency",
            "confirmed": False,
        },
        "gain": {
            "index": 8,
            "min": -12.0, "max": 12.0, "unit": "dB",
            "description": "Output gain",
            "confirmed": False,
        },
    },

    "groups": {
        "saturation":   ["drive", "crunch"],
        "transient":    ["transients"],
        "low_end":      ["boom_freq", "boom_amount"],
        "ambience":     ["room"],
        "filter":       ["high_pass"],
        "output":       ["gain"],
        "global":       ["device_on"],
    },
}
