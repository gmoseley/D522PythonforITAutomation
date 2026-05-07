# ─── Ch04 | Challenge 1: Where Is It? ────────────────────────────────────────
# Use .find() to print the index where "ip address" starts in config
config = "interface GigabitEthernet0/0/1 ip address 10.0.1.1 255.255.255.0"
print(config.find('ip address'))



# ─── Ch04 | Challenge 2: Find or Fail ────────────────────────────────────────
# Use .index() to find "subnet" in config — catch the ValueError if not found
config = "interface GigabitEthernet0/0/1 ip address 10.0.1.1 255.255.255.0"
try:
    print(config.index('255.255.255.0'))
except ValueError: 
    print('not found')
    

# ─── Ch04 | Challenge 3: Is It Local? ────────────────────────────────────────
# Check if ip starts with "192.168" using 'in' and print "Local" or "External"
ip = "192.168.10.50"
if '192.' in ip:
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
    print('ALERT')
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