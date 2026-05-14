# ─── Ch04 | Challenge 1: Shout It Out ────────────────────────────────────────
# Print device_name in all uppercase, then all lowercase
device_name = "Core-Router-01"



# ─── Ch04 | Challenge 2: Clean User Input ────────────────────────────────────
# Strip the whitespace from messy_input and print the cleaned result
messy_input = "   192.168.1.1   "



# ─── Ch04 | Challenge 3: Find and Replace ────────────────────────────────────
# Replace "failed" with "timed out" in the error message and print it
error_msg = "Connection to 192.168.1.1 has failed"



# ─── Ch04 | Challenge 4: Word by Word ────────────────────────────────────────
# Split sentence into a list of words and print each word on its own line
sentence = "The firewall denied access to the internal subnet"



# ─── Ch04 | Challenge 5: Rejoin the Crew ─────────────────────────────────────
# Join the hostnames list into a single comma-separated string and print it
hostnames = ["RTR-01", "SW-02", "FW-03", "AP-04"]



# ─── Ch04 | Challenge 6: How Many A's? ───────────────────────────────────────
# Count how many times the letter 'a' appears in log_line (case-insensitive)
# Hint: convert to lowercase first, then use .count()
log_line = "authentication failure at 192.168.1.100 - invalid password attempt"



# ─── Ch04 | Challenge 7: Does It Match? ──────────────────────────────────────
# Check if filename starts with "log" AND ends with ".txt" — print True or False
filename = "log_2024_01_15.txt"



# ─── Ch04 | Challenge 8: Title Case ──────────────────────────────────────────
# Print device_desc in title case using .title()
device_desc = "core distribution switch layer 2"



# ─── Ch04 | Challenge 9: Count Words ─────────────────────────────────────────
# Split the sentence into words and print how many words it contains
sentence = "Enable logging for all interfaces on the core router"



# ─── Ch04 | Challenge 10: Remove All Spaces ──────────────────────────────────
# Remove every space from mac_addr and print the result
# Expected: "AA:BB:CC:DD:EE:FF"
mac_addr = "AA : BB : CC : DD : EE : FF"



# ─── Ch04 | Challenge 11: Strip Custom Chars ─────────────────────────────────
# Strip the leading and trailing dashes from padded_name and print it
# Expected: "CORE-RTR-01"
padded_name = "---CORE-RTR-01---"



# ─── Ch04 | Challenge 12: Starts With Any Prefix? ────────────────────────────
# Check if hostname starts with "RTR", "SW", or "FW" using startswith with a tuple
# Print "Valid prefix" or "Unknown prefix"
hostname = "FW-EDGE-01"



# ─── Ch04 | Challenge 13: Split a CSV Line ────────────────────────────────────
# Split csv_line on "," and print each field on its own line
csv_line = "CORE-RTR-01,10.0.0.1,router,UP"



# ─── Ch04 | Challenge 14: Build a Banner ─────────────────────────────────────
# Use .center() to print title centered in a 40-character wide field padded with "="
title = "NETWORK STATUS"



# ─── Ch04 | Challenge 15: Extract Key-Value ──────────────────────────────────
# Split config_entry on "=" — print just the value (the part after the "=")
# Expected: "10.0.0.1"
config_entry = "ip_address=10.0.0.1"



# ─── Ch04 | Challenge 16: Sanitize Hostname ──────────────────────────────────
# Replace spaces with "-" and convert to uppercase — print the result
# Expected: "CORE-ROUTER-01"
raw_name = "core router 01"



# ─── Ch04 | Challenge 17: Capitalize First Only ──────────────────────────────
# Use .capitalize() to print alert_msg with only the first letter capitalized
alert_msg = "CRITICAL: core switch is unreachable"



# ─── Ch04 | Challenge 18: Check for Digits in Username ───────────────────────
# Print True if username contains at least one digit, False otherwise
# Hint: use any() with a generator, or loop through the characters
username = "admin007"



# ─── Ch04 | Challenge 19: Repeat a Divider ───────────────────────────────────
# Print a divider of 50 "=" characters using the * operator
# Then print title centered in it using .center()
title = "Device Inventory"



# ─── Ch04 | Challenge 20: Replace Multiple Words ─────────────────────────────
# Chain .replace() calls to replace "error" with "issue" AND "failed" with "timeout"
log = "error: connection failed to host"



# ─── Ch04 | Challenge 21: Split and Rejoin Different Delimiter ───────────────
# Split hostname on "-", then rejoin the parts with "_" and print
# Expected: "RTR_CORE_01"
hostname = "RTR-CORE-01"



# ─── Ch04 | Challenge 22: Find a Substring ───────────────────────────────────
# Use .find() to locate where "password" starts in log_line
# Print the index, or print -1 if not found (find returns -1 automatically)
log_line = "auth failed password=secret123 for user admin"



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



# ─── Ch04 | Challenge 24: WGU Style — Redact Password ───────────────────────
# Complete the Python function redact_password.
# The function should accept a log line string, find the token starting with
# "password=", and replace the value after "=" with "****". Return the redacted line.
# Hint: split() to find the token, then replace it.
#
# Example: redact_password("auth failed password=secret123 for user admin")
#          → "auth failed password=**** for user admin"
# Example: redact_password("login password=abc99 accepted")
#          → "login password=**** accepted"
#
def redact_password(log_line):
    pass



# ─── Ch04 | Challenge 25: WGU Style — Count Keyword in Log Lines ─────────────
# Complete the Python function count_keyword_lines.
# The function should accept a list of log line strings and a keyword string.
# Return the count of lines that contain the keyword (case-sensitive).
#
# Example: count_keyword_lines(["ERROR: timeout", "INFO: ok", "ERROR: lost"], "ERROR") → 2
# Example: count_keyword_lines(["INFO: up", "WARNING: slow"], "ERROR") → 0
#
def count_keyword_lines(log_lines, keyword):
    pass
