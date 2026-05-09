# ─── Ch04 | Challenge 1: Shout It Out ────────────────────────────────────────
# Print device_name in all uppercase, then all lowercase
device_name = "Core-Router-01"
print(device_name.upper())
print(device_name.lower())


# ─── Ch04 | Challenge 2: Clean User Input ────────────────────────────────────
# Strip the whitespace from messy_input and print the cleaned result
messy_input = '   192.168.1.1   '
print(messy_input.replace(' ',''))



# ─── Ch04 | Challenge 3: Find and Replace ────────────────────────────────────
# Replace "failed" with "timed out" in the error message and print it
error_msg = "Connection to 192.168.1.1 has failed"
print(error_msg.replace('failed','timed out'))


# ─── Ch04 | Challenge 4: Word by Word ────────────────────────────────────────
# Split sentence into a list of words and print each word on its own line
sentence = "The firewall denied access to the internal subnet"
print(sentence.split())


# ─── Ch04 | Challenge 5: Rejoin the Crew ─────────────────────────────────────
# Join the hostnames list into a single comma-separated string and print it
hostnames = ["RTR-01", "SW-02", "FW-03", "AP-04"]
print(", ".join(hostnames))



# ─── Ch04 | Challenge 6: How Many A's? ───────────────────────────────────────
# Count how many times the letter 'a' appears in log_line (case-insensitive)
log_line = "authentication failure at 192.168.1.100 - invalid password attempt"
print(log_line.count('a'))



# ─── Ch04 | Challenge 7: Does It Match? ──────────────────────────────────────
# Check if filename starts with "log" AND ends with ".txt" — print True or False
filename = "log_2024_01_15.txt"
print(filename.startswith('log') and filename.endswith('.txt'))


# ─── Ch04 | Challenge 8: WGU Style — Normalize Hostname ──────────────────────
# Complete the Python function normalize_hostname.
# The function should accept a hostname string that may have leading/trailing
# whitespace, strip the whitespace, convert to uppercase, and return the result.
#
# Example: normalize_hostname("  core-router-01  ") → "CORE-ROUTER-01"
# Example: normalize_hostname("  fw-edge-01") → "FW-EDGE-01"
#
def normalize_hostname(hostname):
    pass



# ─── Ch04 | Challenge 9: WGU Style — Mask the Last Octet ─────────────────────
# Complete the Python function mask_ip.
# The function should accept an IPv4 address string, replace everything after
# the last dot with "xxx", and return the masked IP.
#
# Example: mask_ip("192.168.1.105") → "192.168.1.xxx"
# Example: mask_ip("10.0.0.254") → "10.0.0.xxx"
#
def mask_ip(ip):
    pass



# ─── Ch04 | Challenge 10: WGU Style — Count a Keyword ────────────────────────
# Complete the Python function count_keyword.
# The function should accept a log_line string and a keyword string,
# and return an integer count of how many times keyword appears in log_line.
# The search should be case-insensitive.
#
# Example: count_keyword("ERROR error Error ok", "error") → 3
# Example: count_keyword("INFO: startup complete", "error") → 0
#
def count_keyword(log_line, keyword):
    pass

