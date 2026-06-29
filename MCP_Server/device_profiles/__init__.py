"""Device profile registry.

Maps Ableton device class_names to their parameter profiles.
Each profile module exports a single PROFILE dict with:
  meta         — identification and version metadata
  capabilities — what the device can do (True/False flags)
  parameters   — name → {index, min, max, unit, ...} mapping
  groups       — logical groupings of parameters

Usage:
  from MCP_Server.device_profiles import get_profile
  profile = get_profile("Eq8")   # returns dict or None
"""

from . import eq8, compressor, utility, drum_buss, saturator, serum2

_MODULES = [eq8, compressor, utility, drum_buss, saturator, serum2]

REGISTRY = {
    module.PROFILE["meta"]["class_name"]: module.PROFILE
    for module in _MODULES
}


def get_profile(class_name):
    """Return the device profile for the given class_name, or None."""
    return REGISTRY.get(class_name, None)


def list_profiles():
    """Return a list of known class_names."""
    return list(REGISTRY.keys())
