# ─── Ch04 | Challenge 1: Where Is It? ────────────────────────────────────────
# Use .find() to print the index where "ip address" starts in config
config = "interface GigabitEthernet0/0/1 ip address 10.0.1.1 255.255.255.0"



# ─── Ch04 | Challenge 2: Find or Fail ────────────────────────────────────────
# Use .index() to find "subnet" in config — catch the ValueError if not found
config = "interface GigabitEthernet0/0/1 ip address 10.0.1.1 255.255.255.0"



# ─── Ch04 | Challenge 3: Is It Local? ────────────────────────────────────────
# Check if ip starts with "192.168" using 'in' — print "Local" or "External"
ip = "192.168.10.50"



# ─── Ch04 | Challenge 4: Count the Hits ──────────────────────────────────────
# Count how many times "ERROR" appears in the log string and print the count
log = "ERROR: timeout ERROR: retry ERROR: connection lost WARNING: high latency"



# ─── Ch04 | Challenge 5: Flag the Error ──────────────────────────────────────
# If log_line contains "ERROR", print "ALERT: error detected" — otherwise print "OK"
log_line = "2024-01-15 10:23:45 ERROR - Device unreachable: 10.0.0.254"



# ─── Ch04 | Challenge 6: Filter the Noise ────────────────────────────────────
# Loop through log_lines and print only lines that contain "CRITICAL"
log_lines = [
    "INFO: System startup complete",
    "CRITICAL: Core switch unreachable",
    "WARNING: High CPU on RTR-01",
    "CRITICAL: Firewall policy violation",
    "INFO: Backup completed successfully",
]



# ─── Ch04 | Challenge 7: Find After Position ─────────────────────────────────
# Use .find() with a start argument to find the SECOND occurrence of "ERROR" in log
# Print the index of the second "ERROR"
log = "ERROR: timeout at 10:01 ERROR: retry at 10:02"



# ─── Ch04 | Challenge 8: Does It End With Extension? ─────────────────────────
# Check if each filename ends with ".py" — print the filename and True/False
filenames = ["setup.py", "network_log.txt", "deploy.py", "config.json"]



# ─── Ch04 | Challenge 9: Search Case-Insensitive ─────────────────────────────
# Check if "error" appears in log_line regardless of case
# Convert to lowercase first, then use 'in'
log_line = "2024-01-15 WARNING: High Error Rate Detected on RTR-01"



# ─── Ch04 | Challenge 10: Find All Severities ────────────────────────────────
# Loop through log_lines and categorize each: print "HIGH" if it contains "CRITICAL"
# or "ERROR", "LOW" if it contains "INFO" or "WARNING", "UNKNOWN" otherwise
log_lines = [
    "CRITICAL: disk full",
    "INFO: backup ok",
    "ERROR: link down",
    "WARNING: high memory",
    "DEBUG: trace started",
]



# ─── Ch04 | Challenge 11: Count Lines With Keyword ────────────────────────────
# Count how many lines in log_lines contain "FAILED" and print the count
log_lines = [
    "AUTH FAILED: bad password",
    "INFO: user logged in",
    "AUTH FAILED: account locked",
    "INFO: session started",
    "CONN FAILED: timeout",
]



# ─── Ch04 | Challenge 12: Build a Search Result ──────────────────────────────
# For each line in log_lines, print the line number (starting at 1) and the line
# only if it contains "DOWN"
log_lines = [
    "RTR-01: Interface UP",
    "SW-01: Port 3 DOWN",
    "FW-01: Policy applied",
    "RTR-02: Interface DOWN",
    "SW-02: All ports UP",
]



# ─── Ch04 | Challenge 13: Extract IP From Line ───────────────────────────────
# Find the position of the first digit that starts the IP using .find()
# Then slice from that position to the end and split on the first space to isolate the IP
# Expected: "10.0.0.254"
log_line = "Device unreachable: 10.0.0.254 - check routing table"



# ─── Ch04 | Challenge 14: Check Multiple Substrings ──────────────────────────
# Print "Authenticated" if log_line contains BOTH "auth" AND "success"
# Print "Failed" if it contains "auth" AND "fail"
# Print "Other" otherwise
log_line = "auth success for user admin from 10.0.0.5"



# ─── Ch04 | Challenge 15: Replace Only First Occurrence ──────────────────────
# Use .replace() with count=1 to replace only the first "192.168" in config with "10.10"
config = "192.168.1.1 routes to 192.168.2.0 via 192.168.1.254"



# ─── Ch04 | Challenge 16: Collect Matching Lines ─────────────────────────────
# Build a list of lines from log_lines that contain "TIMEOUT" and print the list
log_lines = [
    "CONN TIMEOUT: 10.0.0.5",
    "INFO: RTR-01 up",
    "CONN TIMEOUT: 10.0.0.12",
    "ERROR: disk full",
    "CONN TIMEOUT: 172.16.0.1",
]



# ─── Ch04 | Challenge 17: Find First Non-Match ───────────────────────────────
# Loop through statuses and print the FIRST hostname whose status is not "UP"
# Print "All UP" if none found
devices = [
    ("RTR-01", "UP"),
    ("SW-01", "UP"),
    ("FW-01", "DOWN"),
    ("AP-01", "UP"),
]



# ─── Ch04 | Challenge 18: Highlight Errors ───────────────────────────────────
# For each line in log_lines, if it contains "ERROR" print it with ">>> " prepended
# otherwise print it as-is
log_lines = [
    "INFO: startup complete",
    "ERROR: NTP sync failed",
    "WARNING: high memory",
    "ERROR: BGP peer dropped",
]



# ─── Ch04 | Challenge 19: Count Unique Keywords ──────────────────────────────
# Count how many of the keywords appear at least once in the full log string
# Print the count
keywords = ["ERROR", "WARNING", "CRITICAL", "INFO"]
log = "ERROR: disk full WARNING: high CPU INFO: backup started INFO: done"



# ─── Ch04 | Challenge 20: Find Between Markers ───────────────────────────────
# Extract the text between "[" and "]" in log_line using .find() and slicing
# Expected: "CRITICAL"
log_line = "2024-01-15 10:23:45 [CRITICAL] Core switch unreachable"



# ─── Ch04 | Challenge 21: Search and Replace in a List ───────────────────────
# Build a new list where every line containing "DOWN" has "DOWN" replaced with "OFFLINE"
# Print the new list
log_lines = [
    "RTR-01: UP",
    "SW-01: DOWN",
    "FW-01: UP",
    "AP-01: DOWN",
]



# ─── Ch04 | Challenge 22: Find the Last Occurrence ───────────────────────────
# Use .rfind() to find the index of the LAST occurrence of "/" in path and print it
path = "/var/log/network/core/2024-01-15.log"



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



# ─── Ch04 | Challenge 24: WGU Style — Identify High CPU ─────────────────────
# Complete the Python function identify_high_cpu.
# The function should accept a list of floats representing CPU usage percentages.
# Return a list of INTEGER INDICES where CPU usage is greater than 90.0.
#
# Example: identify_high_cpu([85.0, 92.5, 88.0, 95.2]) → [1, 3]
# Example: identify_high_cpu([91.0, 88.8]) → [0]
# Example: identify_high_cpu([80.0, 85.0]) → []
#
def identify_high_cpu(cpu_list):
    pass



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
