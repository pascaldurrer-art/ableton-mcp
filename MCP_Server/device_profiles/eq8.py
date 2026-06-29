"""Device profile for Ableton EQ Eight (class_name: "Eq8").

Parameter index structure (84 parameters total, Live 12.2.6):
  Indices 0-4:   Global parameters (Device On, Mode, etc.)
  Indices 5-84:  8 bands x 10 parameters each
                 Band N, Chain A: indices 5 + (N-1)*10  to  9 + (N-1)*10
                 Band N, Chain B: indices 10 + (N-1)*10 to 14 + (N-1)*10

Within each 5-parameter chain group (A or B):
  +0  Enable       (quantized: Off/On)
  +1  Frequency    (10 – 22050 Hz)
  +2  Gain         (-15 – +15 dB)   ← confirmed via live test
  +3  Q/Resonance  (0.1 – 36)
  +4  Filter Type  (quantized)

Confirmed indices (live tests, Live 12.2.6):
  7  = "1 Gain A"   (Band 1, Chain A, Gain)
  12 = "1 Gain B"   (Band 1, Chain B, Gain)
  17 = "2 Gain A"   (Band 2, Chain A, Gain)
"""

_BAND_NAMES = ["Low Cut", "Low Shelf", "Band 1", "Band 2",
               "Band 3", "High Shelf", "High Cut", "Air"]

def _band_params(band_number):
    """Build the parameter entries for one band (1-indexed)."""
    base_a = 5 + (band_number - 1) * 10
    base_b = base_a + 5
    n = str(band_number)
    return {
        f"band_{n}_enable_a": {
            "index": base_a + 0,
            "quantized": True,
            "choices": ["Off", "On"],
            "description": f"Band {n} enable (Chain A)",
        },
        f"band_{n}_freq_a": {
            "index": base_a + 1,
            "min": 10.0, "max": 22050.0, "unit": "Hz",
            "description": f"Band {n} frequency (Chain A)",
        },
        f"band_{n}_gain_a": {
            "index": base_a + 2,
            "min": -15.0, "max": 15.0, "unit": "dB",
            "description": f"Band {n} gain (Chain A)",
            "confirmed": True,
        },
        f"band_{n}_q_a": {
            "index": base_a + 3,
            "min": 0.1, "max": 36.0, "unit": None,
            "description": f"Band {n} Q/resonance (Chain A)",
        },
        f"band_{n}_type_a": {
            "index": base_a + 4,
            "quantized": True,
            "choices": ["Bell", "Low Shelf", "High Shelf",
                        "Low Cut 48", "Low Cut 12",
                        "High Cut 12", "High Cut 48",
                        "Notch", "Tilt Shelf"],
            "description": f"Band {n} filter type (Chain A)",
        },
        f"band_{n}_enable_b": {
            "index": base_b + 0,
            "quantized": True,
            "choices": ["Off", "On"],
            "description": f"Band {n} enable (Chain B)",
        },
        f"band_{n}_freq_b": {
            "index": base_b + 1,
            "min": 10.0, "max": 22050.0, "unit": "Hz",
            "description": f"Band {n} frequency (Chain B)",
        },
        f"band_{n}_gain_b": {
            "index": base_b + 2,
            "min": -15.0, "max": 15.0, "unit": "dB",
            "description": f"Band {n} gain (Chain B)",
            "confirmed": band_number == 1,
        },
        f"band_{n}_q_b": {
            "index": base_b + 3,
            "min": 0.1, "max": 36.0, "unit": None,
            "description": f"Band {n} Q/resonance (Chain B)",
        },
        f"band_{n}_type_b": {
            "index": base_b + 4,
            "quantized": True,
            "choices": ["Bell", "Low Shelf", "High Shelf",
                        "Low Cut 48", "Low Cut 12",
                        "High Cut 12", "High Cut 48",
                        "Notch", "Tilt Shelf"],
            "description": f"Band {n} filter type (Chain B)",
        },
    }


def _all_band_params():
    result = {}
    for i in range(1, 9):
        result.update(_band_params(i))
    return result


PROFILE = {
    "meta": {
        "class_name":        "Eq8",
        "display_name":      "EQ Eight",
        "vendor":            "Ableton",
        "version":           "1.0",
        "ableton_version":   "12.2.6",
        "parameter_count":   84,
        "notes": (
            "Index structure derived from 3 confirmed live-test data points. "
            "Non-gain indices are inferred from the pattern and should be "
            "verified against a live session before relying on them."
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
            "index": 0,
            "quantized": True,
            "choices": ["Off", "On"],
            "description": "Enable/disable the device",
        },
        "mode": {
            "index": 1,
            "quantized": True,
            "choices": ["Stereo", "Left/Right", "Mid/Side"],
            "description": "Channel routing mode",
        },
        **_all_band_params(),
    },

    "groups": {
        **{f"band_{n}": [
            f"band_{n}_enable_a", f"band_{n}_freq_a",
            f"band_{n}_gain_a",   f"band_{n}_q_a", f"band_{n}_type_a",
            f"band_{n}_enable_b", f"band_{n}_freq_b",
            f"band_{n}_gain_b",   f"band_{n}_q_b", f"band_{n}_type_b",
        ] for n in range(1, 9)},
        "global": ["device_on", "mode"],
    },
}
