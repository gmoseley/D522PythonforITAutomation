# ─── Ch04 | Challenge 1: Simple f-String ─────────────────────────────────────
# Use an f-string to print: "Device: CORE-RTR-01 | IP: 10.0.0.1"
hostname = "CORE-RTR-01"
ip = "10.0.0.1"



# ─── Ch04 | Challenge 2: Math in the Message ─────────────────────────────────
# Use an f-string to print: "CORE-RTR-01 is at 73.6% CPU (rounded: 74%)"
hostname = "CORE-RTR-01"
cpu_usage = 73.6



# ─── Ch04 | Challenge 3: The Big Block ───────────────────────────────────────
# Store the 3-line network report below in a triple-quoted string and print it
# Line 1: === Pruhart Tech Network Status ===
# Line 2: Status: DEGRADED
# Line 3: Affected Sites: 3



# ─── Ch04 | Challenge 4: Right-Align a Number ────────────────────────────────
# Print port_number right-aligned in a field 10 characters wide using .rjust()
port_number = 8080



# ─── Ch04 | Challenge 5: Two Decimal Places ──────────────────────────────────
# Print bandwidth formatted to exactly 2 decimal places using an f-string format spec
bandwidth = 95.6789



# ─── Ch04 | Challenge 6: Build a Divider ─────────────────────────────────────
# Print a divider of 40 "-" characters using the * operator — no hardcoding



# ─── Ch04 | Challenge 7: Formatted Table Row ─────────────────────────────────
# Print one table row with f-string padding so columns align:
# | CORE-RTR-01      | 10.0.0.1       | UP     |
# Use left-align :<16 for device, :<14 for ip, :<6 for status
device = "CORE-RTR-01"
ip = "10.0.0.1"
status = "UP"



# ─── Ch04 | Challenge 8: Percent Sign in f-String ────────────────────────────
# Use an f-string format spec to print load as a percentage with 1 decimal place
# Expected: "Load: 87.3%"
load = 0.873



# ─── Ch04 | Challenge 9: Zero-Pad a Port ─────────────────────────────────────
# Print port_number zero-padded to 6 digits using an f-string format spec
# Expected: "005443"
port_number = 5443



# ─── Ch04 | Challenge 10: Hex Output ─────────────────────────────────────────
# Print vlan_id in hexadecimal format using an f-string format spec
# Expected: "VLAN hex: 0x1e" for vlan_id = 30
vlan_id = 30



# ─── Ch04 | Challenge 11: Center a Title ─────────────────────────────────────
# Print title centered in a 50-character field padded with "=" on each side
title = "INTERFACE REPORT"



# ─── Ch04 | Challenge 12: Left-Align a Column ────────────────────────────────
# Print each item in devices left-aligned in a 20-char field — one per line
devices = ["CORE-RTR-01", "SW-DISTRIBUTION-02", "FW-01"]



# ─── Ch04 | Challenge 13: Multi-Line f-String Report ─────────────────────────
# Build and print a 3-line report using a triple-quoted f-string
hostname = "EDGE-RTR-02"
ip = "203.0.113.5"
status = "DEGRADED"



# ─── Ch04 | Challenge 14: Table Header + Rows ────────────────────────────────
# Print a header row and two data rows — all columns aligned using f-string padding
# Columns: Device (20 wide), IP (16 wide), Status (8 wide)
devices = [
    ("CORE-RTR-01", "10.0.0.1", "UP"),
    ("SW-CORE-02", "10.0.0.2", "DOWN"),
]



# ─── Ch04 | Challenge 15: Repeat a Pattern ───────────────────────────────────
# Print a warning banner that looks like this (use * operator, no hardcoding):
# !!!!!!!!!!!!!!!!!!! WARNING !!!!!!!!!!!!!!!!!!!
warning = "WARNING"



# ─── Ch04 | Challenge 16: Dynamic Field Width ────────────────────────────────
# Use a variable as the field width in an f-string (nested f-string or format())
# Print hostname left-aligned in a field width equal to max_width
hostname = "RTR-01"
max_width = 20



# ─── Ch04 | Challenge 17: Integer vs Float Division Display ──────────────────
# Print both the floor division and float division of packets / interval
# Format: "Floor: 125 | Float: 125.50"
packets = 251
interval = 2



# ─── Ch04 | Challenge 18: Build a Log Line ───────────────────────────────────
# Build and print a structured log line using an f-string
# Format: "[2024-01-15 10:23:45] [ERROR] CORE-RTR-01: Interface GigE0/1 went DOWN"
timestamp = "2024-01-15 10:23:45"
level = "ERROR"
device = "CORE-RTR-01"
message = "Interface GigE0/1 went DOWN"



# ─── Ch04 | Challenge 19: Uptime Formatter ───────────────────────────────────
# Calculate hours and minutes from total_minutes using // and %
# Print: "Uptime: 3 hours, 47 minutes"
total_minutes = 227



# ─── Ch04 | Challenge 20: Bandwidth in Two Units ─────────────────────────────
# Print bandwidth_mbps converted to both MB/s and GB/s, each to 3 decimal places
# Format: "125.000 MB/s | 0.125 GB/s"
bandwidth_mbps = 125.0



# ─── Ch04 | Challenge 21: Build a Status Table ───────────────────────────────
# Print a full status table with a header, divider, and rows from the data list
# Use f-string padding: device 18 wide, ip 15 wide, status 8 wide
data = [
    ("CORE-RTR-01", "10.0.0.1", "UP"),
    ("SW-DIST-01", "10.0.0.2", "UP"),
    ("FW-EDGE-01", "203.0.113.1", "DOWN"),
]



# ─── Ch04 | Challenge 22: Multiline Triple-Quoted Config ─────────────────────
# Store and print a realistic Cisco-style config block in a triple-quoted string
# Include: interface, ip address, and no shutdown lines



# ─── Ch04 | Challenge 23: WGU Style — Format Uptime ─────────────────────────
# Complete the Python function format_uptime.
# The function should accept an integer total_minutes and return a string
# formatted as "X hours, Y minutes". Use // for hours and % for remainder.
#
# Example: format_uptime(150) → "2 hours, 30 minutes"
# Example: format_uptime(90) → "1 hours, 30 minutes"
#
def format_uptime(total_minutes):
    pass



# ─── Ch04 | Challenge 24: WGU Style — Format Patch Report ───────────────────
# Complete the Python function format_patch_report.
# The function should accept a list of dicts with keys "hostname", "ip", "patched" (bool).
# Return a multi-line string where each line is formatted as:
# "| HOSTNAME         | IP              | STATUS   |"
# Use f-string padding: hostname left-aligned 16 chars, ip 15 chars, status 8 chars.
# Status is "PATCHED" if patched is True, else "PENDING".
# Join the lines with newline characters.
#
# Example input: [{"hostname": "CORE-RTR-01", "ip": "10.0.0.1", "patched": True}]
# Example output: "| CORE-RTR-01      | 10.0.0.1        | PATCHED  |"
#
def format_patch_report(devices):
    pass



# ─── Ch04 | Challenge 25: WGU Style — Format RGB ────────────────────────────
# Complete the Python function format_rgb.
# The function should accept a list of three integers [r, g, b] and return a
# properly formatted RGB color string with no spaces between values.
#
# Example: format_rgb([255, 165, 13]) → "rgb(255,165,13)"
# Example: format_rgb([0, 0, 0]) → "rgb(0,0,0)"
#
def format_rgb(rgb):
    pass
