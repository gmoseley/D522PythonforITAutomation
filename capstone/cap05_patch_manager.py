# ─── Capstone 5: Nora's Patch Manager ────────────────────────────────────────
#
# Difficulty: Advanced
# Reference files: data/devices.txt, data/device_config.json
#
# Scenario:
# This is the full Pruhart Tech scenario. Nora needs to run a patch management
# script that reads the device list, checks which devices are unpatched,
# simulates deploying the patch, logs all activity, and writes a final report.
#
# Requirements:
# 1. Accept an optional command-line argument: --dry-run (use sys.argv)
#    - In dry-run mode, print what WOULD happen but don't write output files
# 2. Read data/device_config.json and filter to only unpatched devices
# 3. For each unpatched device:
#    - Print "Patching {hostname} ({ip})..." 
#    - Simulate success/failure using random.choice([True, False])
#    - Log a timestamped entry to output/patch_log.txt (skip in dry-run)
# 4. Track results in a dictionary: {hostname: "success" or "failed"}
# 5. Handle file errors with try/except throughout
# 6. Print a final summary:
#    - Total devices checked
#    - Already patched: X
#    - Patch attempted: X
#    - Successful: X
#    - Failed: X
# 7. Write the summary to output/patch_summary.txt (skip in dry-run)
#
# Concepts used: sys, json, random, datetime, file I/O, loops, dicts,
#                error handling, f-strings, booleans, functions


