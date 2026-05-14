# ─── Ch04 | Challenge 1: Is It a Number? ─────────────────────────────────────
# Use .isdigit() to check user_input — if valid, convert to int and print x2, else warn
user_input = "67"



# ─── Ch04 | Challenge 2: Letters Only ────────────────────────────────────────
# Use .isalpha() to check if username contains only letters — print "pass" or "fail"
username = "admin123"



# ─── Ch04 | Challenge 3: Upper or Lower? ─────────────────────────────────────
# Check alert_code with .isupper() and .islower() — print which one it is, or "mixed"
alert_code = "CRITICAL"



# ─── Ch04 | Challenge 4: Valid Hostname Prefix ───────────────────────────────
# Use .startswith() to check if hostname starts with "RTR", "SW", or "FW"
# Print "Valid prefix" or "Unknown prefix"
hostname = "SW-CORE-01"



# ─── Ch04 | Challenge 5: Store the Bool ──────────────────────────────────────
# Store the result of (port == 443) in a variable called is_secure
# Then use it in an if/else to print "Secure" or "Insecure"
port = 443



# ─── Ch04 | Challenge 6: Truthy or Falsy? ────────────────────────────────────
# For each value in the list, print "truthy" or "falsy" using an if/else
values = [0, "", "hello", [], [1], None, 42]



# ─── Ch04 | Challenge 7: Alphanumeric Check ──────────────────────────────────
# Use .isalnum() to check if token is alphanumeric — print True or False
token = "A1B2C3"



# ─── Ch04 | Challenge 8: Ends With Check ─────────────────────────────────────
# Check if each filename in the list ends with ".log" — print filename + True/False
filenames = ["syslog.log", "config.txt", "access.log", "error.json"]



# ─── Ch04 | Challenge 9: Both Conditions ─────────────────────────────────────
# Print "Valid log file" only if filename starts with "log" AND ends with ".txt"
# Otherwise print "Not a log file"
filename = "log_2024_01_15.txt"



# ─── Ch04 | Challenge 10: None Check ─────────────────────────────────────────
# Check if result is None using 'is None' — print "No data" or the value
result = None



# ─── Ch04 | Challenge 11: Boolean Arithmetic ─────────────────────────────────
# Count how many values in the list are truthy by summing booleans
# Hint: True == 1, False == 0 in arithmetic context
values = [0, 1, "", "ok", None, 42, [], [1]]



# ─── Ch04 | Challenge 12: Not Operator ───────────────────────────────────────
# Use the 'not' operator: print "No errors found" if error_list is empty, else print its length
error_list = []



# ─── Ch04 | Challenge 13: Compound AND/OR ────────────────────────────────────
# Print "Access granted" if is_admin is True OR (is_active AND has_vpn) is True
# Otherwise print "Access denied"
is_admin = False
is_active = True
has_vpn = True



# ─── Ch04 | Challenge 14: All Digits? ────────────────────────────────────────
# Check if every character in port_str is a digit using .isdigit()
# If so, convert to int and check if it's in range 1-65535 — print "Valid" or "Invalid"
port_str = "8080"



# ─── Ch04 | Challenge 15: Short-Circuit Evaluation ───────────────────────────
# Use 'and' short-circuit: only call .upper() on hostname if hostname is not None
# Print the uppercased name, or "No hostname" if it's None
hostname = None



# ─── Ch04 | Challenge 16: Boolean from Comparison Chain ──────────────────────
# Store the result of (1 <= score <= 100) in is_valid_score
# Print it, then use it in an if/else to print "Valid score" or "Out of range"
score = 87



# ─── Ch04 | Challenge 17: Filter with Bool ───────────────────────────────────
# Build a new list containing only the truthy values from mixed_data
mixed_data = [0, "RTR-01", None, "SW-02", "", 42, False, "FW-01"]



# ─── Ch04 | Challenge 18: Validate IP Octet ──────────────────────────────────
# Check if octet_str is all digits AND 0 <= int(octet_str) <= 255
# Print "Valid" or "Invalid"
octet_str = "192"



# ─── Ch04 | Challenge 19: Classify Port ──────────────────────────────────────
# Classify port using boolean expressions:
# Well-known: 1-1023  |  Registered: 1024-49151  |  Dynamic: 49152-65535
# Print the category, or "Invalid" if out of range
port = 8080



# ─── Ch04 | Challenge 20: Any and All ────────────────────────────────────────
# Use any() to check if at least one device is "DOWN"
# Use all() to check if every device is "UP"
# Print both results
statuses = ["UP", "UP", "DOWN", "UP"]



# ─── Ch04 | Challenge 21: Validate Username Rules ────────────────────────────
# Print "Valid" only if ALL of these are true:
#   - Length is between 4 and 16 characters
#   - First character is alpha (.isalpha())
#   - The rest is alphanumeric (.isalnum())
# Otherwise print "Invalid" with a reason
username = "admin007"



# ─── Ch04 | Challenge 22: Ternary-Style Expression ───────────────────────────
# Use a one-line conditional expression to set label = "CRITICAL" if cpu > 90 else "OK"
# Then print label
cpu = 95.2



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
