# Ch01: Simple f-String ─────────────────────────────────────
# Use an f-string to print: "Device: CORE-RTR-01 | IP: 10.0.0.1"
hostname = "CORE-RTR-01"
ip = "10.0.0.1"
print('Challenge 1 answer:')



# Ch02: Math in the Message ─────────────────────────────────
# Use an f-string to print the hostname and cpu_usage rounded to 1 decimal place
# Expected: "CORE-RTR-01 is at 73.6% CPU"
hostname = "CORE-RTR-01"
cpu_usage = 73.6
print('Challenge 2 answer:')



# Ch03: The Big Block ───────────────────────────────────────
# Store the 3-line network report below in a triple-quoted string and print it
# Line 1: === Pruhart Tech Network Status ===
# Line 2: Status: DEGRADED
# Line 3: Affected Sites: 3
print('Challenge 3 answer:')



# Ch04: Right-Align a Number ────────────────────────────────
# Print port_number right-aligned in a field 10 characters wide using .rjust()
port_number = 8080
print('Challenge 4 answer:')



# Ch05: Two Decimal Places ──────────────────────────────────
# Print bandwidth formatted to exactly 2 decimal places using an f-string format spec
bandwidth = 95.6789
print('Challenge 5 answer:')



# Ch06: Build a Divider ─────────────────────────────────────
# Print a divider of 40 "-" characters using the * operator — no hardcoding
print('Challenge 6 answer:')



# Ch07: Formatted Table Row ─────────────────────────────────
# Print one table row with f-string padding so columns align:
# | CORE-RTR-01      | 10.0.0.1       | UP     |
# Use left-align :<16 for device, :<14 for ip, :<6 for status
device = "CORE-RTR-01"
ip = "10.0.0.1"
status = "UP"
print('Challenge 7 answer:')



# Ch08: Percent Sign in f-String ────────────────────────────
# Use an f-string format spec to print load as a percentage with 1 decimal place
# Expected: "Load: 87.3%"
load = 0.873
print('Challenge 8 answer:')



# Ch09: Zero-Pad a Port ─────────────────────────────────────
# Print port_number zero-padded to 6 digits using an f-string format spec
# Expected: "005443"
port_number = 5443
print('Challenge 9 answer:')



# Ch10: Hex Output ─────────────────────────────────────────
# Print vlan_id in hexadecimal format using an f-string format spec
# Expected: "VLAN hex: 0x1e" for vlan_id = 30
vlan_id = 30
print('Challenge 10 answer:')



# Ch11: Center a Title ─────────────────────────────────────
# Print title centered in a 50-character field padded with "=" on each side
title = "INTERFACE REPORT"
print('Challenge 11 answer:')



# Ch12: Left-Align a Single Name ───────────────────────────
# Print device left-aligned in a 20-character field using f-string padding
# Then print it again in a 20-char field with "." filling empty space on the right
device = "SW-DISTRIBUTION-02"
print('Challenge 12 answer:')



# Ch13: Multi-Line f-String Report ─────────────────────────
# Build and print a 3-line report using a triple-quoted f-string
hostname = "EDGE-RTR-02"
ip = "203.0.113.5"
status = "DEGRADED"
print('Challenge 13 answer:')



# Ch14: Table Header + Two Rows ────────────────────────────
# Print a header row and two data rows using three separate print statements
# Columns: Device (20 wide), IP (16 wide), Status (8 wide)
device1, ip1, status1 = "CORE-RTR-01", "10.0.0.1", "UP"
device2, ip2, status2 = "SW-CORE-02", "10.0.0.2", "DOWN"
print('Challenge 14 answer:')



# Ch15: Repeat a Pattern ───────────────────────────────────
# Print a warning banner using the * operator — no hardcoding:
# !!!!!!!!!!!!!!!!!!! WARNING !!!!!!!!!!!!!!!!!!!
warning = "WARNING"
print('Challenge 15 answer:')



# Ch16: Dynamic Field Width ────────────────────────────────
# Use a variable as the field width in an f-string
# Print hostname left-aligned in a field width equal to max_width
hostname = "RTR-01"
max_width = 20
print('Challenge 16 answer:')



# Ch17: Integer vs Float Division Display ──────────────────
# Print both the floor division and float division of packets / interval
# Format: "Floor: 125 | Float: 125.50"
packets = 251
interval = 2
print('Challenge 17 answer:')



# Ch18: Build a Log Line ───────────────────────────────────
# Build and print a structured log line using an f-string
# Format: "[2024-01-15 10:23:45] [ERROR] CORE-RTR-01: Interface GigE0/1 went DOWN"
timestamp = "2024-01-15 10:23:45"
level = "ERROR"
device = "CORE-RTR-01"
message = "Interface GigE0/1 went DOWN"
print('Challenge 18 answer:')



# Ch19: Uptime Formatter ───────────────────────────────────
# Calculate hours and minutes from total_minutes using // and %
# Print: "Uptime: 3 hours, 47 minutes"
total_minutes = 227
print('Challenge 19 answer:')



# Ch20: Bandwidth in Two Units ─────────────────────────────
# Print bandwidth_mbps converted to both MB/s and GB/s, each to 3 decimal places
# Format: "125.000 MB/s | 0.125 GB/s"
bandwidth_mbps = 125.0
print('Challenge 20 answer:')



# Ch21: Full Status Report ─────────────────────────────────
# Build and print a complete status report using f-strings — no loop
# Print: a header line, a divider of 40 "=" chars, then all three device rows
# Use f-string padding: device 18 wide, ip 15 wide, status 8 wide
device1, ip1, status1 = "CORE-RTR-01", "10.0.0.1", "UP"
device2, ip2, status2 = "SW-DIST-01", "10.0.0.2", "UP"
device3, ip3, status3 = "FW-EDGE-01", "203.0.113.1", "DOWN"
print('Challenge 21 answer:')



# Ch22: Multiline Triple-Quoted Config ─────────────────────
# Store and print a Cisco-style config block in a triple-quoted f-string
# Include: interface line, ip address line, and no shutdown line
interface = "GigabitEthernet0/0/1"
ip_addr = "10.0.0.1"
subnet = "255.255.255.0"
print('Challenge 22 answer:')



# Ch23: WGU Style — Format Uptime ─────────────────────────
# Complete the Python function format_uptime.
# The function should accept an integer total_minutes and return a string
# formatted as "X hours, Y minutes". Use // for hours and % for remainder.
#
# Example: format_uptime(150) → "2 hours, 30 minutes"
# Example: format_uptime(90) → "1 hours, 30 minutes"
#
def format_uptime(total_minutes):
    pass

print('Challenge 23 answer:')
print(format_uptime(150))
print(format_uptime(90))



# Ch24: WGU Style — Format Log Line ───────────────────────
# Complete the Python function format_log_line.
# The function should accept timestamp, level, device, and message strings.
# Return a formatted log line: "[timestamp] [level] device: message"
#
# Example: format_log_line("2024-01-15 10:23:45", "ERROR", "CORE-RTR-01", "Link down")
#          → "[2024-01-15 10:23:45] [ERROR] CORE-RTR-01: Link down"
# Example: format_log_line("2024-01-16 08:00:00", "INFO", "SW-01", "Port up")
#          → "[2024-01-16 08:00:00] [INFO] SW-01: Port up"
#
def format_log_line(timestamp, level, device, message):
    pass

print('Challenge 24 answer:')
print(format_log_line("2024-01-15 10:23:45", "ERROR", "CORE-RTR-01", "Link down"))
print(format_log_line("2024-01-16 08:00:00", "INFO", "SW-01", "Port up"))



# Ch25: WGU Style — Format RGB ────────────────────────────
# Complete the Python function format_rgb.
# The function should accept a list of three integers [r, g, b] and return a
# properly formatted RGB color string with no spaces between values.
#
# Example: format_rgb([255, 165, 13]) → "rgb(255,165,13)"
# Example: format_rgb([0, 0, 0]) → "rgb(0,0,0)"
#
def format_rgb(rgb):
    pass

print('Challenge 25 answer:')
print(format_rgb([255, 165, 13]))
print(format_rgb([0, 0, 0]))
