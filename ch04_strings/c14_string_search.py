# ─── Ch04 | Challenge 1: Where Is It? ────────────────────────────────────────
# Use .find() to print the index where "ip" starts in config
config = "interface GigabitEthernet0/0/1 ip address 10.0.1.1 255.255.255.0"
print('Challenge 1 answer:')



# ─── Ch04 | Challenge 2: Is It In There? ─────────────────────────────────────
# Use 'in' to check if "ERROR" is in log_line — print True or False
log_line = "2024-01-15 10:23:45 ERROR - Device unreachable: 10.0.0.254"
print('Challenge 2 answer:')



# ─── Ch04 | Challenge 3: Count the Errors ────────────────────────────────────
# Count how many times "ERROR" appears in the log string and print the count
log = "ERROR: timeout ERROR: retry ERROR: connection lost WARNING: high latency"
print('Challenge 3 answer:')



# ─── Ch04 | Challenge 4: Flag the Error ──────────────────────────────────────
# If log_line contains "ERROR", print "ALERT: error detected" — otherwise print "OK"
log_line = "2024-01-15 10:23:45 ERROR - Device unreachable: 10.0.0.254"
print('Challenge 4 answer:')



# ─── Ch04 | Challenge 5: Is It Local? ────────────────────────────────────────
# Check if ip starts with "192.168" using startswith() — print "Local" or "External"
ip = "192.168.10.50"
print('Challenge 5 answer:')



# ─── Ch04 | Challenge 6: Check the Extension ─────────────────────────────────
# Check if filename ends with ".py" — print True or False
filename = "deploy_config.py"
print('Challenge 6 answer:')



# ─── Ch04 | Challenge 7: Not In There ────────────────────────────────────────
# Check if "CRITICAL" is NOT in log_line — print True or False
log_line = "2024-01-15 WARNING: High CPU on RTR-01"
print('Challenge 7 answer:')



# ─── Ch04 | Challenge 8: Case-Insensitive Search ─────────────────────────────
# Check if "error" appears in log_line regardless of case
# Convert to lowercase first, then use 'in' — print True or False
log_line = "2024-01-15 WARNING: High Error Rate Detected on RTR-01"
print('Challenge 8 answer:')



# ─── Ch04 | Challenge 9: Find After Position ─────────────────────────────────
# Use .find() with a start argument to find the SECOND occurrence of "ERROR" in log
# Print the index of the second "ERROR"
log = "ERROR: timeout at 10:01 ERROR: retry at 10:02"
print('Challenge 9 answer:')



# ─── Ch04 | Challenge 10: Replace Only First ─────────────────────────────────
# Use .replace() with count=1 to replace only the first "192.168" in config with "10.10"
config = "192.168.1.1 routes to 192.168.2.0 via 192.168.1.254"
print('Challenge 10 answer:')



# ─── Ch04 | Challenge 11: Last Slash ─────────────────────────────────────────
# Use .rfind() to find the index of the LAST "/" in path and print it
path = "/var/log/network/core/2024-01-15.log"
print('Challenge 11 answer:')



# ─── Ch04 | Challenge 12: Extract Between Markers ────────────────────────────
# Use .find() and slicing to extract the text between "[" and "]"
# Expected: "CRITICAL"
log_line = "2024-01-15 10:23:45 [CRITICAL] Core switch unreachable"
print('Challenge 12 answer:')



# ─── Ch04 | Challenge 13: Check Both Conditions ──────────────────────────────
# Print "Authenticated" if log_line contains BOTH "auth" AND "success"
# Print "Failed" if it contains "auth" AND "fail"
# Print "Other" otherwise
log_line = "auth success for user admin from 10.0.0.5"
print('Challenge 13 answer:')



# ─── Ch04 | Challenge 14: Extract IP From Line ───────────────────────────────
# Find the position of ": " in log_line using .find(), then slice everything after it
# Expected: "10.0.0.254"
log_line = "Device unreachable: 10.0.0.254"
print('Challenge 14 answer:')



# ─── Ch04 | Challenge 15: Filename Without Extension ─────────────────────────
# Use .rfind() to find the last "." in filename, then slice to get just the base name
# Expected: "deploy_config"
filename = "deploy_config.py"
print('Challenge 15 answer:')



# ─── Ch04 | Challenge 16: Severity Label ─────────────────────────────────────
# Check log_line for "CRITICAL", "ERROR", "WARNING", "INFO" in that priority order
# Print the first one found, or "UNKNOWN" if none match
log_line = "2024-01-15 ERROR: BGP peer dropped"
print('Challenge 16 answer:')



# ─── Ch04 | Challenge 17: Find the Value After a Key ─────────────────────────
# Find "port=" in config, then slice from after the "=" to the next space to get the value
# Expected: "443"
config = "host=10.0.0.1 port=443 proto=tcp"
print('Challenge 17 answer:')



# ─── Ch04 | Challenge 18: Redact Sensitive Value ─────────────────────────────
# Find "password=" in log_line, use .split() to isolate the full token, then .replace() it
# Expected: "auth failed password=**** for user admin"
log_line = "auth failed password=secret123 for user admin"
print('Challenge 18 answer:')



# ─── Ch04 | Challenge 19: Extract Filename From Path ─────────────────────────
# Use .rfind() to locate the last "/" in path, then slice everything after it
# Expected: "2024-01-15.log"
path = "/var/log/network/core/2024-01-15.log"
print('Challenge 19 answer:')



# ─── Ch04 | Challenge 20: Find Value Between Markers ─────────────────────────
# Find "hostname=" in config, then slice from after the "=" to the next space
# Expected: "CORE-RTR-01"
config = "hostname=CORE-RTR-01 ip=10.0.0.1 status=UP"
print('Challenge 20 answer:')



# ─── Ch04 | Challenge 21: Count Present Severities ──────────────────────────
# Without a loop, use 'in' and boolean arithmetic to count how many of the four
# severity keywords appear at least once in log
# Expected: 3 (ERROR, WARNING, and INFO are present; CRITICAL is not)
log = "ERROR: disk full WARNING: high CPU INFO: backup started"
print('Challenge 21 answer:')



# ─── Ch04 | Challenge 22: Validate IP Format ─────────────────────────────────
# Check that ip contains exactly 3 dots using .count(".")
# AND that ip starts with a digit using [0].isdigit()
# AND that ip ends with a digit using [-1].isdigit()
# Print "Valid format" or "Invalid format"
ip = "192.168.1.105"
print('Challenge 22 answer:')



# ─── Ch04 | Challenge 23: WGU Style — Get Log Severity ──────────────────────
# Complete the Python function get_log_severity.
# The function should accept a log string and return the severity level found in it.
# Check in this priority order: "CRITICAL", "ERROR", "WARNING", "INFO".
# Return the first one found. If none match, return "UNKNOWN".
#
# Example: get_log_severity("CRITICAL: core switch down") → "CRITICAL"
# Example: get_log_severity("INFO: startup complete") → "INFO"
# Example: get_log_severity("System rebooted") → "UNKNOWN"
#
def get_log_severity(log_line):
    pass

print('Challenge 23 answer:')
print(get_log_severity("CRITICAL: core switch down"))
print(get_log_severity("INFO: startup complete"))
print(get_log_severity("System rebooted"))



# ─── Ch04 | Challenge 24: WGU Style — Find Second Occurrence ────────────────
# Complete the Python function find_second_occurrence.
# Use .find() twice: once to locate the first match, then again starting after it.
# Return the index of the second occurrence, or -1 if there is no second match.
#
# Example: find_second_occurrence("ERROR: timeout ERROR: retry", "ERROR") → 17
# Example: find_second_occurrence("WARNING: high CPU", "ERROR") → -1
#
def find_second_occurrence(text, keyword):
    pass

print('Challenge 24 answer:')
print(find_second_occurrence("ERROR: timeout ERROR: retry", "ERROR"))
print(find_second_occurrence("WARNING: high CPU", "ERROR"))



# ─── Ch04 | Challenge 25: WGU Style — Extract Config Value ──────────────────
# Complete the Python function extract_config_value.
# The function should accept a config string and a key string.
# Find the key in the string, then return everything after "key=" up to the
# next space (or end of string). Return None if the key is not found.
#
# Example: extract_config_value("host=10.0.0.1 port=443 proto=tcp", "port") → "443"
# Example: extract_config_value("host=10.0.0.1 port=443", "vlan") → None
#
def extract_config_value(config, key):
    pass

print('Challenge 25 answer:')
print(extract_config_value("host=10.0.0.1 port=443 proto=tcp", "port"))
print(extract_config_value("host=10.0.0.1 port=443", "vlan"))
