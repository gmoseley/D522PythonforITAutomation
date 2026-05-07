# ─── Ch04 | Challenge 1: Math in the Message ─────────────────────────────────
# Use an f-string to print: "CORE-RTR-01 is at 73.6% CPU (rounded: 74%)"
# Hint: use round() inside the f-string
hostname = "CORE-RTR-01"
cpu_usage = 73.6
print(f'{hostname} is at {round(cpu_usage,2)}% CPU')


# ─── Ch04 | Challenge 2: The Big Block ───────────────────────────────────────
#Store the 3-line network report below in a triple-quoted string and print it
report = """
Line 1: "=== Pruhart Tech Network Status ==="
Line 2: "Status: DEGRADED"
Line 3: "Affected Sites: 3"
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
