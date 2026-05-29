# ─── Ch04 | Challenge 1: Is It a Number? ─────────────────────────────────────
# Use .isdigit() to check user_input — if valid, convert to int and print x2, else warn
user_input = "67"
print('Challenge 1 answer:')



# ─── Ch04 | Challenge 2: Letters Only ────────────────────────────────────────
# Use .isalpha() to check if username contains only letters — print "pass" or "fail"
username = "admin123"
print('Challenge 2 answer:')



# ─── Ch04 | Challenge 3: Upper or Lower? ─────────────────────────────────────
# Check alert_code with .isupper() and .islower() — print which one it is, or "mixed"
alert_code = "CRITICAL"
print('Challenge 3 answer:')



# ─── Ch04 | Challenge 4: Valid Hostname Prefix ───────────────────────────────
# Use .startswith() to check if hostname starts with "RTR", "SW", or "FW"
# Print "Valid prefix" or "Unknown prefix"
hostname = "SW-CORE-01"
print('Challenge 4 answer:')



# ─── Ch04 | Challenge 5: Store the Bool ──────────────────────────────────────
# Store the result of (port == 443) in a variable called is_secure
# Then use it in an if/else to print "Secure" or "Insecure"
port = 443
print('Challenge 5 answer:')



# ─── Ch04 | Challenge 6: Empty Check ─────────────────────────────────────────
# An empty string is falsy — use a separate if/else on each variable to print "has data" or "empty"
# Do not use a loop — write two separate if/else blocks
hostname1 = "RTR-01"
hostname2 = ""
print('Challenge 6 answer:')



# ─── Ch04 | Challenge 7: Alphanumeric Check ──────────────────────────────────
# Use .isalnum() to check if token is alphanumeric — print True or False
token = "A1B2C3"
print('Challenge 7 answer:')



# ─── Ch04 | Challenge 8: Log File Check ──────────────────────────────────────
# Check if filename ends with ".log" — print True or False
filename = "syslog.log"
print('Challenge 8 answer:')



# ─── Ch04 | Challenge 9: Both Conditions ─────────────────────────────────────
# Print "Valid log file" only if filename starts with "log" AND ends with ".txt"
# Otherwise print "Not a log file"
filename = "log_2024_01_15.txt"
print('Challenge 9 answer:')



# ─── Ch04 | Challenge 10: None Check ─────────────────────────────────────────
# Check if result is None using 'is None' — print "No data" or the value
result = None
print('Challenge 10 answer:')



# ─── Ch04 | Challenge 11: Count True Conditions ──────────────────────────────
# Without a loop, use boolean arithmetic to count how many of these conditions are True
# Conditions: is_admin is True, port > 0, hostname starts with "RTR", status equals "UP"
# Print the count
is_admin = True
port = 8080
hostname = "RTR-01"
status = "DOWN"
print('Challenge 11 answer:')



# ─── Ch04 | Challenge 12: Not Operator ───────────────────────────────────────
# Use the 'not' operator: print "No errors found" if error_list is empty, else print its length
error_list = []
print('Challenge 12 answer:')



# ─── Ch04 | Challenge 13: Compound AND/OR ────────────────────────────────────
# Print "Access granted" if is_admin is True OR (is_active AND has_vpn) is True
# Otherwise print "Access denied"
is_admin = False
is_active = True
has_vpn = True
print('Challenge 13 answer:')



# ─── Ch04 | Challenge 14: All Digits? ────────────────────────────────────────
# Check if every character in port_str is a digit using .isdigit()
# If so, convert to int and check if it's in range 1-65535 — print "Valid" or "Invalid"
port_str = "8080"
print('Challenge 14 answer:')



# ─── Ch04 | Challenge 15: Short-Circuit Evaluation ───────────────────────────
# Use 'and' short-circuit: only call .upper() on hostname if hostname is not None
# Print the uppercased name, or "No hostname" if it's None
hostname = None
print('Challenge 15 answer:')



# ─── Ch04 | Challenge 16: Boolean from Comparison Chain ──────────────────────
# Store the result of (1 <= score <= 100) in is_valid_score
# Print it, then use it in an if/else to print "Valid score" or "Out of range"
score = 87
print('Challenge 16 answer:')



# ─── Ch04 | Challenge 17: Status Summary ─────────────────────────────────────
# Without a loop, use boolean arithmetic to count how many devices are "UP"
# Print: "X of 4 devices are UP"
status1 = "UP"
status2 = "DOWN"
status3 = "UP"
status4 = "UP"
print('Challenge 17 answer:')



# ─── Ch04 | Challenge 18: Validate IP Octet ──────────────────────────────────
# Check if octet_str is all digits AND 0 <= int(octet_str) <= 255
# Print "Valid" or "Invalid"
octet_str = "192"
print('Challenge 18 answer:')



# ─── Ch04 | Challenge 19: Classify Port ──────────────────────────────────────
# Classify port using chained boolean comparisons:
# Well-known: 1-1023  |  Registered: 1024-49151  |  Dynamic: 49152-65535
# Print the category, or "Invalid" if out of range
port = 8080
print('Challenge 19 answer:')



# ─── Ch04 | Challenge 20: Any and All ────────────────────────────────────────
# Use any() to check if at least one of these conditions is True
# Use all() to check if all of them are True
# Conditions: is_admin, port > 0, is_active
# Print both results with labels
is_admin = False
port = 8080
is_active = True
print('Challenge 20 answer:')



# ─── Ch04 | Challenge 21: Validate Username Rules ────────────────────────────
# Print "Valid" only if ALL of these are true:
#   - Length is between 4 and 16 characters
#   - First character is alpha (.isalpha())
#   - The rest is alphanumeric (.isalnum() on the slice [1:])
# Otherwise print "Invalid" with a reason
username = "admin007"
print('Challenge 21 answer:')



# ─── Ch04 | Challenge 22: Ternary-Style Expression ───────────────────────────
# Use a one-line conditional expression to set label = "CRITICAL" if cpu > 90 else "OK"
# Then print label
cpu = 95.2
print('Challenge 22 answer:')



# ─── Ch04 | Challenge 23: WGU Style — Validate IP Octet ─────────────────────
# Complete the Python function is_valid_ip_octet.
# The function should accept a string representing one octet of an IP address.
# Return True if the string is all digits AND the integer value is between 0 and 255.
# Return False otherwise.
#
# Example: is_valid_ip_octet("192") → True
# Example: is_valid_ip_octet("256") → False
# Example: is_valid_ip_octet("abc") → False
#
def is_valid_ip_octet(value):
    pass

print('Challenge 23 answer:')
print(is_valid_ip_octet("192"))
print(is_valid_ip_octet("256"))
print(is_valid_ip_octet("abc"))



# ─── Ch04 | Challenge 24: WGU Style — Validate Employee ID ──────────────────
# Complete the Python function validate_id.
# Return True if ALL of these are true:
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

print('Challenge 24 answer:')
print(validate_id("HRD00123"))
print(validate_id("Ops123456"))
print(validate_id("HRD0012"))



# ─── Ch04 | Challenge 25: WGU Style — Classify Device ───────────────────────
# Complete the Python function classify_device.
# The function should accept a hostname string and return its device type:
#   - Starts with "RTR" → "Router"
#   - Starts with "SW"  → "Switch"
#   - Starts with "FW"  → "Firewall"
#   - Starts with "AP"  → "Access Point"
#   - Anything else     → "Unknown"
#
# Example: classify_device("RTR-CORE-01") → "Router"
# Example: classify_device("AP-FLOOR2-01") → "Access Point"
# Example: classify_device("SRV-DB-01") → "Unknown"
#
def classify_device(hostname):
    pass

print('Challenge 25 answer:')
print(classify_device("RTR-CORE-01"))
print(classify_device("AP-FLOOR2-01"))
print(classify_device("SRV-DB-01"))
