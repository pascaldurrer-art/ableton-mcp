"""verify_profile.py — Device profile verifier.

Connects directly to the Ableton Remote Script socket, retrieves live
parameter data for a device, and compares it against the static profile
in device_profiles/.

Usage:
  python -m MCP_Server.verify_profile --class-name Eq8 --track-index 0 --device-index 1

Requirements:
  Ableton must be running with AbletonMCP loaded as a Control Surface.

Exit codes:
  0 — all profile entries verified
  1 — one or more entries wrong or unverifiable
"""

import argparse
import json
import os
import socket
import sys


# ── Socket communication ───────────────────────────────────────────────────────

HOST = os.environ.get("ABLETON_HOST", "localhost")
PORT = int(os.environ.get("ABLETON_PORT", "9877"))
TIMEOUT = 15.0


def _send_command(sock, command_type, params=None):
    payload = json.dumps({"type": command_type, "params": params or {}})
    sock.sendall(payload.encode("utf-8"))
    chunks = []
    while True:
        chunk = sock.recv(65536)
        if not chunk:
            break
        chunks.append(chunk)
        try:
            return json.loads(b"".join(chunks).decode("utf-8"))
        except json.JSONDecodeError:
            continue
    raise RuntimeError("Connection closed before a complete response was received.")


def fetch_live_parameters(track_index, device_index):
    """Return the raw parameter list from Ableton for the given device."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(TIMEOUT)
        try:
            sock.connect((HOST, PORT))
        except ConnectionRefusedError:
            print(f"ERROR: Cannot connect to Ableton on {HOST}:{PORT}.")
            print("       Make sure Ableton is running and AbletonMCP is active.")
            sys.exit(1)

        response = _send_command(sock, "get_device_parameters", {
            "track_index":          track_index,
            "device_index":         device_index,
            "include_display_value": False,
            "limit":                None,
        })

    if response.get("status") != "success":
        msg = response.get("message", "Unknown error")
        print(f"ERROR from Ableton: {msg}")
        sys.exit(1)

    return response["result"]


# ── Profile loading ────────────────────────────────────────────────────────────

def load_profile(class_name):
    from MCP_Server.device_profiles import get_profile
    profile = get_profile(class_name)
    if profile is None:
        from MCP_Server.device_profiles import list_profiles
        print(f"ERROR: No profile found for '{class_name}'.")
        print(f"       Known profiles: {', '.join(list_profiles())}")
        sys.exit(1)
    return profile


# ── Comparison ─────────────────────────────────────────────────────────────────

def _normalise(name):
    """Case-insensitive, whitespace-collapsed comparison key."""
    return " ".join(name.lower().split())


def compare(profile, live_result):
    """Compare profile entries against live Ableton data.

    Returns a list of result dicts, one per profile parameter entry.
    Each dict has keys: param_key, profile_index, live_name, status, note.
    """
    # Build a lookup: index → live parameter name
    live_by_index = {p["index"]: p["name"] for p in live_result["parameters"]}

    results = []

    for param_key, param_def in profile["parameters"].items():
        if "index" not in param_def:
            # Group note or non-indexable entry — skip
            continue

        profile_index = param_def["index"]
        profile_desc  = param_def.get("description", "")
        live_name     = live_by_index.get(profile_index)

        if live_name is None:
            status = "❌"
            note   = f"Index {profile_index} not found in live data (device has {len(live_by_index)} parameters)"
        else:
            # Match: profile description should contain the live name (or vice versa)
            # We also accept an exact match on the key itself after normalisation.
            live_norm  = _normalise(live_name)
            desc_norm  = _normalise(profile_desc)
            key_norm   = _normalise(param_key.replace("_", " "))

            if live_norm in desc_norm or desc_norm in live_norm or live_norm == key_norm:
                status = "✅"
                note   = f'Live name: "{live_name}"'
            else:
                status = "❌"
                note   = f'Live name: "{live_name}" — does not match description: "{profile_desc}"'

        results.append({
            "param_key":     param_key,
            "profile_index": profile_index,
            "live_name":     live_name,
            "status":        status,
            "note":          note,
            "confirmed":     param_def.get("confirmed", False),
        })

    return results


# ── Report ─────────────────────────────────────────────────────────────────────

def print_report(profile, live_result, comparison):
    meta = profile["meta"]
    sep  = "─" * 72

    print()
    print(sep)
    print(f"  Device Profile Verification Report")
    print(f"  Device:          {meta['display_name']} ({meta['class_name']})")
    print(f"  Profile version: {meta['version']}  |  Ableton: {meta['ableton_version']}")
    print(f"  Live track:      {live_result['track_name']}  "
          f"(track {live_result['track_index']}, device {live_result['device_index']})")
    print(f"  Live device:     {live_result['device_name']}  "
          f"({live_result['parameter_count']} parameters)")
    print(sep)

    verified = [r for r in comparison if r["status"] == "✅"]
    wrong    = [r for r in comparison if r["status"] == "❌"]
    total    = len(comparison)

    print(f"\n  Summary")
    print(f"  {'Total profile entries checked:':<36} {total}")
    print(f"  {'✅ Verified:':<36} {len(verified)}")
    print(f"  {'❌ Wrong / not matched:':<36} {len(wrong)}")
    print()

    if wrong:
        print("  Discrepancies")
        print(sep)
        for r in wrong:
            print(f"  ❌  {r['param_key']}")
            print(f"       Profile index: {r['profile_index']}")
            print(f"       {r['note']}")
            print()

    print("  Full parameter list")
    print(sep)
    col = max(len(r["param_key"]) for r in comparison) + 2
    for r in comparison:
        confirmed_flag = " (was confirmed)" if r["confirmed"] else ""
        print(f"  {r['status']}  {r['param_key']:<{col}} index {r['profile_index']:>3}   {r['note']}{confirmed_flag}")

    print()
    print(sep)

    if wrong:
        print(f"  RESULT: {len(wrong)} discrepancy/ies found — profile needs correction.")
        return 1
    else:
        print(f"  RESULT: All {len(verified)} checked entries verified successfully.")
        return 0


# ── Entry point ────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Verify a device profile against live Ableton data."
    )
    parser.add_argument("--class-name",    required=True,       help="Device class_name (e.g. Eq8)")
    parser.add_argument("--track-index",   type=int, default=0, help="Track index in Ableton (0-based)")
    parser.add_argument("--device-index",  type=int, default=0, help="Device index on that track (0-based)")
    args = parser.parse_args()

    print(f"Connecting to Ableton on {HOST}:{PORT} ...")
    live_result = fetch_live_parameters(args.track_index, args.device_index)
    print(f"Retrieved {live_result['parameter_count']} parameters "
          f"from '{live_result['device_name']}' on '{live_result['track_name']}'.")

    profile    = load_profile(args.class_name)
    comparison = compare(profile, live_result)
    exit_code  = print_report(profile, live_result, comparison)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
