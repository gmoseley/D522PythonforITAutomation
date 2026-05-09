# ─── Ch04 | Challenge 1: Math in the Message ─────────────────────────────────
# Use an f-string to print: "CORE-RTR-01 is at 73.6% CPU (rounded: 74%)"
# Hint: use round() inside the f-string
hostname = "CORE-RTR-01"
cpu_usage = 73.6
print(f'{hostname} is at {round(cpu_usage,2)}% CPU (rounded: {round(cpu_usage)}%)')


# ─── Ch04 | Challenge 2: The Big Block ───────────────────────────────────────
#Store the 3-line network report below in a triple-quoted string and print it
report = """
=== Pruhart Tech Network Status ===
Status: DEGRADED
Affected Sites: 3
"""
print(report)


# ─── Ch04 | Challenge 3: Line It Up ──────────────────────────────────────────
# Print port_number right-aligned in a field 10 characters wide
port_number = 8080
print(str(port_number).rjust(10))


# ─── Ch04 | Challenge 4: Two Decimal Places ──────────────────────────────────
# Print bandwidth formatted to exactly 2 decimal places
bandwidth = 95.6789
print(round(bandwidth,2))


# ─── Ch04 | Challenge 5: Build a Divider ─────────────────────────────────────
# Print a divider that looks like this: ----------------------------------------
# Do it by repeating "-" using the * operator — no hardcoding
print('-' * 40)
    



# ─── Ch04 | Challenge 6: Formatted Table Row ─────────────────────────────────
# Print one row of a table using f-string padding so columns align:
# | CORE-RTR-01      | 10.0.0.1       | UP     |
device = "CORE-RTR-01"
ip = "10.0.0.1"
status = "UP"

print(f'| {device:<16} | {ip:<16} | {status:<16} |')


# ─── Ch04 | Challenge 7: WGU Style — Format Uptime ───────────────────────────
# Complete the Python function format_uptime.
# The function should accept an integer representing total minutes of uptime,
# and return a string formatted as "X hours, Y minutes".
# Use floor division (//) to get hours and modulo (%) to get remaining minutes.
#
# Example: format_uptime(150) → "2 hours, 30 minutes"
# Example: format_uptime(90) → "1 hours, 30 minutes"
#
def format_uptime(total_minutes):
    pass



# ─── Ch04 | Challenge 8: WGU Style — Format Patch Report ────────────────────
# Complete the Python function format_patch_report.
# The function should accept a list of dicts, each with keys "hostname", "ip",
# and "patched" (bool). Return a multi-line string where each line is formatted as:
# "| HOSTNAME         | IP              | STATUS   |"
# Use f-string padding: hostname left-aligned 16 chars, ip 15 chars, status 8 chars.
# Status is "PATCHED" if patched is True, else "PENDING".
# Join the lines with newline characters.
#
# Example: format_patch_report([{"hostname": "CORE-RTR-01", "ip": "10.0.0.1", "patched": True}])
#          → "| CORE-RTR-01      | 10.0.0.1        | PATCHED  |"
#
def format_patch_report(devices):
    pass
