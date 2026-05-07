# ─── Capstone 3: Device Config Validator ─────────────────────────────────────
#
# Difficulty: Intermediate
# Reference file: data/device_config.json
#
# Scenario:
# Before the security patch rollout, Nora needs to validate that every device
# entry in the config file has all required fields and correct data types.
#
# Requirements:
# 1. Read and parse data/device_config.json using the json module
# 2. For each device, validate:
#    - All required keys exist: hostname, ip, role, vendor, os, patched
#    - "ip" matches a basic pattern: 4 groups of numbers separated by dots (use re or split)
#    - "patched" is a boolean (use isinstance())
#    - "hostname" is uppercase (use .isupper() on the alpha parts)
# 3. Print PASS or FAIL for each device with the reason if it fails
# 4. Print a final summary: X of Y devices passed validation
# 5. Write failed devices to output/validation_failures.txt
#
# Concepts used: json, re, loops, dictionaries, string methods, booleans, file I/O


