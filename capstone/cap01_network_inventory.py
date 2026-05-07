# ─── Capstone 1: Network Inventory Scanner ────────────────────────────────────
#
# Difficulty: Beginner
# Reference file: data/devices.txt
#
# Scenario:
# Nora needs a quick inventory of all Pruhart Tech devices organized by type.
# Device names follow this convention: TYPE-ROLE-NUMBER (e.g. CORE-RTR-01)
#
# Requirements:
# 1. Read data/devices.txt and load all hostnames into a list
# 2. Categorize each device by its prefix:
#    - starts with "CORE"   → Core Devices
#    - starts with "DIST"   → Distribution Devices
#    - starts with "ACCESS" → Access Devices
#    - starts with "FW"     → Firewalls
#    - starts with "AP"     → Access Points
#    - starts with anything else → Servers / Other
# 3. Store each category as a key in a dictionary with a list of devices as the value
# 4. Print a summary showing each category and how many devices are in it
# 5. Write the full categorized inventory to a new file: output/inventory_report.txt
#
# Expected output (example):
#   Core Devices       : 2
#   Distribution Devices: 3
#   Access Devices     : 4
#   Firewalls          : 2
#   Access Points      : 4
#   Servers / Other    : 3
#
# Concepts used: file I/O, lists, dictionaries, loops, string methods, f-strings


