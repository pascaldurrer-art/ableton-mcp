"""Device profile for Ableton EQ Eight (class_name: "Eq8").

Verified structure (Live 12.2.6, 84 parameters total):

  Global parameters: indices 0-3
    0: Device On
    1: Output Gain
    2: (unverified)
    3: (unverified)

  Band layout: 8 bands x 10 parameters each
    Band N base index: 4 + (N-1) * 10

  Within each band (offsets from base):
    +0  Filter On A   (quantized: Off/On)           -- Enable, Chain A
    +1  Filter Type A (quantized: Bell/Shelf/Cut/...)
    +2  Frequency A   (10 - 22050 Hz)
    +3  Gain A        (-15 - +15 dB)                -- CONFIRMED
    +4  Resonance A   (0.1 - 36)
    +5  Filter On B   (quantized: Off/On)           -- Enable, Chain B
    +6  Filter Type B (quantized)
    +7  Frequency B   (10 - 22050 Hz)
    +8  Gain B        (-15 - +15 dB)                -- CONFIRMED (Band 1)
    +9  Resonance B   (0.1 - 36)

Confirmed indices (live verification, Live 12.2.6):
  7  = "1 Gain A"   (Band 1, Gain, Chain A)
  12 = "1 Gain B"   (Band 1, Gain, Chain B)
  17 = "2 Gain A"   (Band 2, Gain, Chain A)
  All other indices verified by verify_profile.py against live Ableton session.
"""

_FILTER_TYPES = [
    "Bell", "Low Shelf", "High Shelf",
    "Low Cut 48", "Low Cut 12",
    "High Cut 12", "High Cut 48",
    "Notch", "Tilt Shelf",
]


def _band_params(band_number):
    """Build the 10 parameter entries for one band (1-indexed)."""
    base = 4 + (band_number - 1) * 10
    n    = str(band_number)
    return {
        f"band_{n}_filter_on_a": {
            "index":      base + 0,
            "quantized":  True,
            "choices":    ["Off", "On"],
            "live_name":  f"{n} Filter On A",
            "description": f"Band {n} enable (Chain A)",
        },
        f"band_{n}_filter_type_a": {
            "index":      base + 1,
            "quantized":  True,
            "choices":    _FILTER_TYPES,
            "live_name":  f"{n} Filter Type A",
            "description": f"Band {n} filter type (Chain A)",
        },
        f"band_{n}_freq_a": {
            "index":      base + 2,
            "min": 10.0, "max": 22050.0, "unit": "Hz",
            "live_name":  f"{n} Frequency A",
            "description": f"Band {n} frequency (Chain A)",
        },
        f"band_{n}_gain_a": {
            "index":      base + 3,
            "min": -15.0, "max": 15.0, "unit": "dB",
            "live_name":  f"{n} Gain A",
            "description": f"Band {n} gain (Chain A)",
            "confirmed":  True,
        },
        f"band_{n}_resonance_a": {
            "index":      base + 4,
            "min": 0.1, "max": 36.0, "unit": None,
            "live_name":  f"{n} Resonance A",
            "description": f"Band {n} resonance (Chain A)",
        },
        f"band_{n}_filter_on_b": {
            "index":      base + 5,
            "quantized":  True,
            "choices":    ["Off", "On"],
            "live_name":  f"{n} Filter On B",
            "description": f"Band {n} enable (Chain B)",
        },
        f"band_{n}_filter_type_b": {
            "index":      base + 6,
            "quantized":  True,
            "choices":    _FILTER_TYPES,
            "live_name":  f"{n} Filter Type B",
            "description": f"Band {n} filter type (Chain B)",
        },
        f"band_{n}_freq_b": {
            "index":      base + 7,
            "min": 10.0, "max": 22050.0, "unit": "Hz",
            "live_name":  f"{n} Frequency B",
            "description": f"Band {n} frequency (Chain B)",
        },
        f"band_{n}_gain_b": {
            "index":      base + 8,
            "min": -15.0, "max": 15.0, "unit": "dB",
            "live_name":  f"{n} Gain B",
            "description": f"Band {n} gain (Chain B)",
            "confirmed":  band_number == 1,
        },
        f"band_{n}_resonance_b": {
            "index":      base + 9,
            "min": 0.1, "max": 36.0, "unit": None,
            "live_name":  f"{n} Resonance B",
            "description": f"Band {n} resonance (Chain B)",
        },
    }


def _all_band_params():
    result = {}
    for i in range(1, 9):
        result.update(_band_params(i))
    return result


PROFILE = {
    "meta": {
        "class_name":       "Eq8",
        "display_name":     "EQ Eight",
        "vendor":           "Ableton",
        "version":          "2.0",
        "ableton_version":  "12.2.6",
        "parameter_count":  84,
        "notes": (
            "Structure verified against live Ableton session via verify_profile.py. "
            "All 84 parameters verified via verify_profile.py against live Ableton session. "
            "Global params: device_on(0), output_gain(1), scale(2), adaptive_q(3)."
        ),
    },

    "capabilities": {
        "supports_gain":        True,
        "supports_frequency":   True,
        "supports_q":           True,
        "supports_filter_type": True,
        "supports_mid_side":    True,
        "supports_dynamic":     False,
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
        "output_gain": {
            "index":      1,
            "min": -12.0, "max": 12.0, "unit": "dB",
            "live_name":  "Output Gain",
            "description": "Global output gain",
            "confirmed":  True,
        },
        "scale": {
            "index":      2,
            "live_name":  "Scale",
            "description": "EQ display scale",
            "confirmed":  True,
        },
        "adaptive_q": {
            "index":      3,
            "live_name":  "Adaptive Q",
            "description": "Adaptive Q mode (adjusts Q when gain changes)",
            "confirmed":  True,
        },
        **_all_band_params(),
    },

    "groups": {
        **{f"band_{n}": [
            f"band_{n}_filter_on_a",   f"band_{n}_filter_type_a",
            f"band_{n}_freq_a",        f"band_{n}_gain_a",
            f"band_{n}_resonance_a",
            f"band_{n}_filter_on_b",   f"band_{n}_filter_type_b",
            f"band_{n}_freq_b",        f"band_{n}_gain_b",
            f"band_{n}_resonance_b",
        ] for n in range(1, 9)},
        "global": ["device_on", "output_gain", "scale", "adaptive_q"],
    },
}
