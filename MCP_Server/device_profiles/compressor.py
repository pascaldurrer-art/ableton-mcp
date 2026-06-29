"""Device profile for Ableton Compressor (class_name: "Compressor2").

Verified structure (Live 12.2.6, 23 parameters total):

  All 23 parameters verified via get_device_parameters against a live session.
  Sidechain parameters (indices 14-22) are exposed as normal device parameters
  and can be set via set_device_parameter / set_multiple_device_parameters.

  NOTE: Sidechain SOURCE (which track feeds the sidechain) is NOT a device
  parameter — it is track input routing and requires set_track_input_routing.
"""

PROFILE = {
    "meta": {
        "class_name":       "Compressor2",
        "display_name":     "Compressor",
        "vendor":           "Ableton",
        "version":          "2.0",
        "ableton_version":  "12.2.6",
        "parameter_count":  23,
        "notes": (
            "All 23 parameters verified against live Ableton session. "
            "Sidechain source routing requires set_track_input_routing, "
            "not set_device_parameter."
        ),
    },

    "capabilities": {
        "supports_threshold":   True,
        "supports_ratio":       True,
        "supports_attack":      True,
        "supports_release":     True,
        "supports_gain":        True,
        "supports_knee":        True,
        "supports_sidechain":   True,
        "supports_sidechain_eq": True,
        "supports_lookahead":   True,
        "supports_mid_side":    False,
        "supports_dynamic":     True,
    },

    "parameters": {
        "device_on": {
            "index":      0,
            "quantized":  True,
            "choices":    ["Off", "On"],
            "live_name":  "Device On",
            "description": "Enable/disable the device",
            "confirmed":  True,
        },
        "threshold": {
            "index":      1,
            "min": 0.0, "max": 1.0, "unit": "dB (normalized)",
            "live_name":  "Threshold",
            "description": "Compression threshold (-36 to 0 dB, normalized 0-1)",
            "confirmed":  True,
        },
        "ratio": {
            "index":      2,
            "min": 0.0, "max": 1.0, "unit": "normalized",
            "live_name":  "Ratio",
            "description": "Compression ratio (normalized 0-1, display: X:1)",
            "confirmed":  True,
        },
        "expansion_ratio": {
            "index":      3,
            "min": 1.0, "max": 2.0, "unit": "normalized",
            "live_name":  "Expansion Ratio",
            "description": "Expansion ratio below threshold (1.0 = off)",
            "confirmed":  True,
        },
        "attack": {
            "index":      4,
            "min": 0.0, "max": 1.0, "unit": "ms (normalized)",
            "live_name":  "Attack",
            "description": "Attack time (normalized 0-1, display: ms)",
            "confirmed":  True,
        },
        "release": {
            "index":      5,
            "min": 0.0, "max": 1.0, "unit": "ms (normalized)",
            "live_name":  "Release",
            "description": "Release time (normalized 0-1, display: ms). Ignored when auto_release is On.",
            "confirmed":  True,
        },
        "auto_release": {
            "index":      6,
            "quantized":  True,
            "choices":    ["Off", "On"],
            "live_name":  "Auto Release On/Off",
            "description": "Automatic release time",
            "confirmed":  True,
        },
        "output_gain": {
            "index":      7,
            "min": -36.0, "max": 36.0, "unit": "dB",
            "live_name":  "Output Gain",
            "description": "Output gain (dB)",
            "confirmed":  True,
        },
        "makeup": {
            "index":      8,
            "quantized":  True,
            "choices":    ["Off", "On"],
            "live_name":  "Makeup",
            "description": "Auto makeup gain",
            "confirmed":  True,
        },
        "dry_wet": {
            "index":      9,
            "min": 0.0, "max": 1.0, "unit": "%",
            "live_name":  "Dry/Wet",
            "description": "Dry/wet mix (0=dry, 1=wet)",
            "confirmed":  True,
        },
        "model": {
            "index":      10,
            "quantized":  True,
            "choices":    ["Peak", "RMS", "Expand"],
            "live_name":  "Model",
            "description": "Detection model: Peak / RMS / Expand",
            "confirmed":  True,
        },
        "env_mode": {
            "index":      11,
            "quantized":  True,
            "choices":    ["Lin", "Log"],
            "live_name":  "Env Mode",
            "description": "Envelope mode: Linear or Logarithmic",
            "confirmed":  True,
        },
        "knee": {
            "index":      12,
            "min": 0.0, "max": 18.0, "unit": "dB",
            "live_name":  "Knee",
            "description": "Soft knee width in dB",
            "confirmed":  True,
        },
        "lookahead": {
            "index":      13,
            "quantized":  True,
            "choices":    ["0 ms", "1 ms", "10 ms"],
            "live_name":  "LookAhead",
            "description": "Lookahead time",
            "confirmed":  True,
        },
        "sc_listen": {
            "index":      14,
            "quantized":  True,
            "choices":    ["Off", "On"],
            "live_name":  "S/C Listen",
            "description": "Monitor the sidechain signal",
            "confirmed":  True,
        },
        "sc_eq_on": {
            "index":      15,
            "quantized":  True,
            "choices":    ["Off", "On"],
            "live_name":  "S/C EQ On",
            "description": "Enable sidechain EQ",
            "confirmed":  True,
        },
        "sc_eq_type": {
            "index":      16,
            "quantized":  True,
            "choices":    ["Low shelf", "Low pass", "Bell", "Notch", "High pass", "High shelf"],
            "live_name":  "S/C EQ Type",
            "description": "Sidechain EQ filter type",
            "confirmed":  True,
        },
        "sc_eq_freq": {
            "index":      17,
            "min": 0.0, "max": 1.0, "unit": "Hz (normalized)",
            "live_name":  "S/C EQ Freq",
            "description": "Sidechain EQ frequency (normalized, display: Hz)",
            "confirmed":  True,
        },
        "sc_eq_q": {
            "index":      18,
            "min": 0.0, "max": 1.0, "unit": "normalized",
            "live_name":  "S/C EQ Q",
            "description": "Sidechain EQ Q/resonance (normalized)",
            "confirmed":  True,
        },
        "sc_eq_gain": {
            "index":      19,
            "min": -15.0, "max": 15.0, "unit": "dB",
            "live_name":  "S/C EQ Gain",
            "description": "Sidechain EQ gain (dB, only used for Bell/Shelf types)",
            "confirmed":  True,
        },
        "sc_on": {
            "index":      20,
            "quantized":  True,
            "choices":    ["Off", "On"],
            "live_name":  "S/C On",
            "description": "Enable external sidechain input",
            "confirmed":  True,
        },
        "sc_gain": {
            "index":      21,
            "min": 0.0, "max": 1.0, "unit": "dB (normalized)",
            "live_name":  "S/C Gain",
            "description": "Sidechain input gain (normalized)",
            "confirmed":  True,
        },
        "sc_mix": {
            "index":      22,
            "min": 0.0, "max": 1.0, "unit": "%",
            "live_name":  "S/C Mix",
            "description": "Sidechain wet/dry mix",
            "confirmed":  True,
        },
    },

    "groups": {
        "dynamics":   ["threshold", "ratio", "expansion_ratio", "knee"],
        "timing":     ["attack", "release", "auto_release"],
        "output":     ["output_gain", "makeup", "dry_wet"],
        "detection":  ["model", "env_mode", "lookahead"],
        "sidechain":  ["sc_on", "sc_listen", "sc_gain", "sc_mix",
                       "sc_eq_on", "sc_eq_type", "sc_eq_freq", "sc_eq_q", "sc_eq_gain"],
        "global":     ["device_on"],
    },
}
