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


# ─── Ch04 | Challenge 7: WGU Style — Get Log Severity ───────────────────────
# Complete the Python function get_log_severity.
# The function should accept a log string and return the severity level found in it.
# Check in this priority order: "CRITICAL", "ERROR", "WARNING", "INFO".
# Return the first one found. If none are found, return "UNKNOWN".
#
# Example: get_log_severity("CRITICAL: core switch down") → "CRITICAL"
# Example: get_log_severity("INFO: startup complete") → "INFO"
# Example: get_log_severity("System rebooted") → "UNKNOWN"
#
def get_log_severity(log_line):
    pass



# ─── Ch04 | Challenge 8: WGU Style — Identify High CPU ──────────────────────
# Complete the Python function identify_high_cpu.
# The function should accept a list of floats representing CPU usage percentages.
# Return a list of INTEGER INDICES (not the values themselves) where CPU usage
# is greater than 90.0.
#
# Example: identify_high_cpu([85.0, 92.5, 88.0, 95.2]) → [1, 3]
# Example: identify_high_cpu([91.0, 88.8]) → [0]
# Example: identify_high_cpu([80.0, 85.0]) → []
#
def identify_high_cpu(cpu_list):
    pass