# ─── Ch04 | Challenge 1: Where Is It? ────────────────────────────────────────
# Use .find() to print the index where "ip address" starts in config
config = "interface GigabitEthernet0/0/1 ip address 10.0.1.1 255.255.255.0"
print(config.find('ip address'))



# ─── Ch04 | Challenge 2: Find or Fail ────────────────────────────────────────
# Use .index() to find "subnet" in config — catch the ValueError if not found
config = "interface GigabitEthernet0/0/1 ip address 10.0.1.1 255.255.255.0"
try:
    print(config.index('subnet'))
except ValueError: 
    print('not found')
    

# ─── Ch04 | Challenge 3: Is It Local? ────────────────────────────────────────
# Check if ip starts with "192.168" using 'in' and print "Local" or "External"
ip = "192.168.10.50"
if '192.168' in ip:
    print('Local')
else:
    print('External')


# ─── Ch04 | Challenge 4: Count the Hits ──────────────────────────────────────
# Count how many times "ERROR" appears in the log string and print the count
log = "ERROR: timeout ERROR: retry ERROR: connection lost WARNING: high latency"
print(log.count('ERROR'))


# ─── Ch04 | Challenge 5: Flag the Error ──────────────────────────────────────
# If log_line contains "ERROR", print "ALERT: error detected" otherwise "OK"
log_line = "2024-01-15 10:23:45 ERROR - Device unreachable: 10.0.0.254"
if 'ERROR' in log_line:
    print('ALERT: error detected')
else:
    print('OK')


# ─── Ch04 | Challenge 6: Filter the Noise ────────────────────────────────────
# Loop through log_lines and print only lines that contain "CRITICAL"
log_lines = [
    "INFO: System startup complete",
    "CRITICAL: Core switch unreachable",
    "WARNING: High CPU on RTR-01",
    "CRITICAL: Firewall policy violation",
    "INFO: Backup completed successfully",
]
for i in log_lines:
    if 'CRITICAL' in i:
        print(i)


# ─── Ch04 | Challenge 7: WGU Style — Flag Critical Events ────────────────────
# Complete the Python function is_critical_event.
# The function should accept a log_line string and return True if it contains
# "CRITICAL" or "ERROR" (case-sensitive), otherwise return False.
#
# Example: is_critical_event("CRITICAL: Core switch unreachable") → True
# Example: is_critical_event("INFO: System startup complete") → False
#
def is_critical_event(log_line):
    pass



# ─── Ch04 | Challenge 8: WGU Style — Extract the IP ─────────────────────────
# Complete the Python function extract_ip.
# The function should accept a log_line string that contains an IPv4 address
# somewhere in it. Find the position of the first digit that starts an IP,
# and return just the IP address substring.
# Hint: use .split() and check each token with .replace('.','').isdigit()
#
# Example: extract_ip("Device 192.168.1.105 unreachable") → "192.168.1.105"
# Example: extract_ip("Blocked host 10.0.0.5 on port 22") → "10.0.0.5"
#
def extract_ip(log_line):
    pass