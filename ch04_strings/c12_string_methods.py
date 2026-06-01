# ─── Ch04 | Challenge 1: Shout It Out ────────────────────────────────────────
# Print device_name in all uppercase, then all lowercase
device_name = "Core-Router-01"
print('Challenge 1 answer:')
print(device_name.upper())



# ─── Ch04 | Challenge 2: Clean User Input ────────────────────────────────────
# Strip the whitespace from messy_input and print the cleaned result
messy_input = "   192.168.1.1   "
print('Challenge 2 answer:')
print(messy_input.replace(' ',''))




# ─── Ch04 | Challenge 3: Find and Replace ────────────────────────────────────
# Replace "failed" with "timed out" in the error message and print it
error_msg = "Connection to 192.168.1.1 has failed"
print('Challenge 3 answer:')
print(error_msg.replace('failed','timed out'))


# ─── Ch04 | Challenge 4: First Field ─────────────────────────────────────────
# Split csv_line on "," and print just the first field using an index
csv_line = "CORE-RTR-01,10.0.0.1,router,UP"
print('Challenge 4 answer:')
print(csv_line.split(',')[:1])


# ─── Ch04 | Challenge 5: Rejoin the Crew ─────────────────────────────────────
# Join the hostnames list into a single comma-separated string and print it
hostnames = ["RTR-01", "SW-02", "FW-03", "AP-04"]
print('Challenge 5 answer:')
print(','.join(hostnames))



# ─── Ch04 | Challenge 6: How Many A's? ───────────────────────────────────────
# Count how many times the letter 'a' appears in log_line (case-insensitive)
# Hint: convert to lowercase first, then use .count()
log_line = "authentication failure at 192.168.1.100 - invalid password attempt"
print('Challenge 6 answer:')
print(log_line.count('a'))



# ─── Ch04 | Challenge 7: Does It Match? ──────────────────────────────────────
# Check if filename starts with "log" AND ends with ".txt" — print True or False
filename = "log_2024_01_15.txt"
print('Challenge 7 answer:')



# ─── Ch04 | Challenge 8: Title Case ──────────────────────────────────────────
# Print device_desc in title case using .title()
device_desc = "core distribution switch layer 2"
print('Challenge 8 answer:')



# ─── Ch04 | Challenge 9: Count Words ─────────────────────────────────────────
# Split the sentence into words and print how many words it contains using len()
sentence = "Enable logging for all interfaces on the core router"
print('Challenge 9 answer:')



# ─── Ch04 | Challenge 10: Remove All Spaces ──────────────────────────────────
# Remove every space from mac_addr using .replace() and print the result
# Expected: "AA:BB:CC:DD:EE:FF"
mac_addr = "AA : BB : CC : DD : EE : FF"
print('Challenge 10 answer:')



# ─── Ch04 | Challenge 11: Strip Custom Chars ─────────────────────────────────
# Strip the leading and trailing dashes from padded_name and print it
# Expected: "CORE-RTR-01"
padded_name = "---CORE-RTR-01---"
print('Challenge 11 answer:')



# ─── Ch04 | Challenge 12: Starts With Any Prefix? ────────────────────────────
# Check if hostname starts with "RTR", "SW", or "FW" using startswith with a tuple
# Print "Valid prefix" or "Unknown prefix"
hostname = "FW-EDGE-01"
print('Challenge 12 answer:')



# ─── Ch04 | Challenge 13: Last Field in CSV ──────────────────────────────────
# Split csv_line on "," and print just the last field using a negative index
# Expected: "UP"
csv_line = "CORE-RTR-01,10.0.0.1,router,UP"
print('Challenge 13 answer:')



# ─── Ch04 | Challenge 14: Build a Banner ─────────────────────────────────────
# Use .center() to print title centered in a 40-character wide field padded with "="
title = "NETWORK STATUS"
print('Challenge 14 answer:')



# ─── Ch04 | Challenge 15: Extract Key-Value ──────────────────────────────────
# Split config_entry on "=" — print just the value (the part after the "=")
# Expected: "10.0.0.1"
config_entry = "ip_address=10.0.0.1"
print('Challenge 15 answer:')



# ─── Ch04 | Challenge 16: Sanitize Hostname ──────────────────────────────────
# Replace spaces with "-" and convert to uppercase — print the result
# Expected: "CORE-ROUTER-01"
raw_name = "core router 01"
print('Challenge 16 answer:')



# ─── Ch04 | Challenge 17: Extract the Command ────────────────────────────────
# Strip whitespace, split on " ", take the first word, and convert to uppercase
# Expected: "INTERFACE"
raw_command = "  interface GigabitEthernet0/0/1  "
print('Challenge 17 answer:')



# ─── Ch04 | Challenge 18: Rebuild the Hostname ───────────────────────────────
# Split hostname on "-", replace the middle segment with "DIST", rejoin with "-" and print
# Expected: "RTR-DIST-01"
hostname = "RTR-CORE-01"
print('Challenge 18 answer:')



# ─── Ch04 | Challenge 19: Repeat a Divider ───────────────────────────────────
# Print a divider of 50 "=" characters using *, then print title centered inside it
title = "Device Inventory"
print('Challenge 19 answer:')



# ─── Ch04 | Challenge 20: Replace Multiple Words ─────────────────────────────
# Chain .replace() calls to replace "error" with "issue" AND "failed" with "timeout"
log = "error: connection failed to host"
print('Challenge 20 answer:')



# ─── Ch04 | Challenge 21: Split and Rejoin Different Delimiter ───────────────
# Split hostname on "-", rejoin the parts with "_" and print
# Expected: "RTR_CORE_01"
hostname = "RTR-CORE-01"
print('Challenge 21 answer:')



# ─── Ch04 | Challenge 22: Extract Between Brackets ───────────────────────────
# Use .find() and slicing to extract the text between "[" and "]"
# Expected: "CRITICAL"
log_line = "2024-01-15 10:23:45 [CRITICAL] Core switch unreachable"
print('Challenge 22 answer:')



# ─── Ch04 | Challenge 23: WGU Style — Normalize Hostname ─────────────────────
# Complete the Python function normalize_hostname.
# The function should accept a hostname string that may have leading/trailing
# whitespace, strip the whitespace, convert to uppercase, and return the result.
#
# Example: normalize_hostname("  core-router-01  ") → "CORE-ROUTER-01"
# Example: normalize_hostname("  fw-edge-01") → "FW-EDGE-01"
#
def normalize_hostname(hostname):
    pass

h1 = "  core-router-01  "
h2 = "  fw-edge-01"
print('Challenge 23 answer:')
print(normalize_hostname(h1))
print(normalize_hostname(h2))



# ─── Ch04 | Challenge 24: WGU Style — Redact Password ───────────────────────
# Complete the Python function redact_password.
# The function should accept a log line string, find the token starting with
# "password=", and replace the value after "=" with "****". Return the redacted line.
# Hint: use split() to isolate the token, then replace it.
#
# Example: redact_password("auth failed password=secret123 for user admin")
#          → "auth failed password=**** for user admin"
# Example: redact_password("login password=abc99 accepted")
#          → "login password=**** accepted"
#
def redact_password(log_line):
    pass

l1 = "auth failed password=secret123 for user admin"
l2 = "login password=abc99 accepted"
print('Challenge 24 answer:')
print(redact_password(l1))
print(redact_password(l2))



# ─── Ch04 | Challenge 25: WGU Style — Rebuild Config Entry ──────────────────
# Complete the Python function rebuild_config_entry.
# The function should accept a config string like "key=value" and a new value string.
# Split on "=", replace the value part, rejoin with "=", and return the result.
#
# Example: rebuild_config_entry("ip_address=10.0.0.1", "192.168.1.1") → "ip_address=192.168.1.1"
# Example: rebuild_config_entry("hostname=CORE-RTR-01", "EDGE-RTR-01") → "hostname=EDGE-RTR-01"
#
def rebuild_config_entry(config_str, new_value):
    pass

c1 = "ip_address=10.0.0.1"
c2 = "hostname=CORE-RTR-01"
print('Challenge 25 answer:')
print(rebuild_config_entry(c1, "192.168.1.1"))
print(rebuild_config_entry(c2, "EDGE-RTR-01"))
