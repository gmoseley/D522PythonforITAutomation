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



# ─── Ch04 | Challenge 9: WGU Style — Redact Password ────────────────────────
# Complete the Python function redact_password.
# The function should accept a log line string like
# "auth failed password=secret123 for user admin", find the value after
# "password=" and replace it with "****". Return the redacted line.
# Hint: use split() to find the token starting with "password=", then replace it.
#
# Example: redact_password("auth failed password=secret123 for user admin")
#          → "auth failed password=**** for user admin"
# Example: redact_password("login password=abc99 accepted")
#          → "login password=**** accepted"
#
def redact_password(log_line):
    pass



# ─── Ch04 | Challenge 10: WGU Style — Validate ID ────────────────────────────
# Complete the Python function validate_id.
# The function should accept a string and return True if ALL of these are true:
#   - Total length is exactly 8 characters
#   - First 3 characters are all uppercase letters
#   - Last 5 characters are all digits
# Return False otherwise.
#
# Example: validate_id("HRD00123") → True
# Example: validate_id("Ops123456") → False
# Example: validate_id("HRD0012") → False
#
def validate_id(employee_id):
    pass

