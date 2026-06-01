# Ch01: Know Your Environment ───────────────────────────────
# Use os to print: current working directory and a sorted list of .py files in it
import os
print('Challenge 1 answer:')



# Ch02: System Info ─────────────────────────────────────────
# Use sys to print the Python version string and the OS platform
import sys
print('Challenge 2 answer:')



# Ch03: What Time Is It? ────────────────────────────────────
# Print the current date and time formatted as: "2024-01-15 10:23:45"
from datetime import datetime
print('Challenge 3 answer:')



# Ch04: Roll the Dice ───────────────────────────────────────
# Simulate rolling a 6-sided die 5 times — print each result on one line
import random
print('Challenge 4 answer:')



# Ch05: Find the IP ─────────────────────────────────────────
# Use re to extract the first IP address from log_line and print it
import re
log_line = "2024-01-15 10:23:45 - Device 192.168.1.105 unreachable - check routing"
print('Challenge 5 answer:')



# Ch06: Read a JSON Config ──────────────────────────────────
# Write device_config to "device_config.json", read it back, print only the "ip" value
import json
device_config = {"hostname": "CORE-RTR-01", "ip": "10.0.0.1", "role": "core"}
print('Challenge 6 answer:')



# Ch07: Walk the Directory ──────────────────────────────────
# Use os.walk() to print every .py file found under the project root (non-recursive is fine)
import os
root = "c:/Users/gmoseley/OneDrive/College/D522 - Python for IT Automation/VSCClaude"
print('Challenge 7 answer:')



# Ch08: Build a Timestamp Filename ─────────────────────────
# Use datetime to generate a log filename like: "log_20240115_102345.txt" and print it
from datetime import datetime
print('Challenge 8 answer:')



# Ch09: Pick a Random Device ────────────────────────────────
# Create a list of 5 device hostnames, use random.choice() to pick one and print it
import random
print('Challenge 9 answer:')



# Ch10: Your Own Module ────────────────────────────────────
# Create helpers.py in this folder with two functions:
#   - ping_check(ip): prints "Pinging {ip}..."
#   - categorize(hostname): returns "Router", "Switch", "Firewall", or "Unknown"
# Import helpers here and call both functions with sample values
print('Challenge 10 answer:')



# Ch11: os.path Deep Dive ──────────────────────────────────
# For log_path, print: the filename only, the directory only, the extension,
# the path without extension, and whether the file exists
import os
log_path = "/var/log/network/core_switch_2024.log"
print('Challenge 11 answer:')



# Ch12: Shuffle and Sample ─────────────────────────────────
# Shuffle devices in place, then pick a random sample of 3 without repeats — print both
import random
devices = ["RTR-01", "SW-01", "FW-01", "AP-01", "RTR-02", "SW-02"]
print('Challenge 12 answer:')



# Ch13: Parse a Date String ────────────────────────────────
# Parse date_str into a datetime object using strptime, then print just the year and month
from datetime import datetime
date_str = "15/01/2024 10:23:45"
print('Challenge 13 answer:')



# Ch14: Days Between Dates ─────────────────────────────────
# Calculate and print the number of days between start_date and end_date
from datetime import datetime
start_date = "2024-01-01"
end_date = "2024-03-15"
print('Challenge 14 answer:')



# Ch15: Find All IPs in a Block of Text ────────────────────
# Use re.findall() to extract every IP address from log_block and print the list
import re
log_block = """
RTR-01 at 10.0.0.1 connected to SW-01 at 10.0.0.2
FW-01 at 203.0.113.1 blocked traffic from 198.51.100.5
AP-01 at 192.168.1.10 associated 192.168.1.55
"""
print('Challenge 15 answer:')



# Ch16: Environment Variable ───────────────────────────────
# Use os.environ.get() to read the "PATH" environment variable — print the first entry
# (split on ";" on Windows, ":" on Linux/Mac)
import os
print('Challenge 16 answer:')



# Ch17: Regex Match vs Search ──────────────────────────────
# Use re.match() to check if line starts with a date pattern "YYYY-MM-DD"
# Use re.search() to find "ERROR" anywhere in the line — print both results
import re
line = "2024-01-15 10:23:45 ERROR - Link down on RTR-01"
print('Challenge 17 answer:')



# Ch18: JSON List ──────────────────────────────────────────
# Write device_list to "devices.json", read it back, and print each device's hostname
import json
device_list = [
    {"hostname": "RTR-01", "ip": "10.0.0.1"},
    {"hostname": "SW-01",  "ip": "10.0.0.2"},
    {"hostname": "FW-01",  "ip": "10.0.0.3"},
]
print('Challenge 18 answer:')



# Ch19: Format a Timestamp ─────────────────────────────────
# Print now in three different formats:
#   - ISO 8601:     "2024-01-15T10:23:45"
#   - Human-friendly: "January 15, 2024 10:23 AM"
#   - Log filename: "log_20240115_102345.txt"
from datetime import datetime
print('Challenge 19 answer:')



# Ch20: Regex Named Groups ─────────────────────────────────
# Use a regex with named groups to parse log_line into timestamp, level, and message
# Pattern hint: (?P<name>...)
import re
log_line = "2024-01-15 10:23:45 [ERROR] Core switch unreachable"
print('Challenge 20 answer:')



# Ch21: sys.argv Preview ───────────────────────────────────
# Print a usage message showing how this script would be called from the command line
# Then print each argument from sys.argv with its index
# (Run as: python c20_modules.py arg1 arg2)
import sys
print('Challenge 21 answer:')



# Ch22: Combine datetime + re + os ────────────────────────
# Get the current datetime formatted as "YYYYMMDD_HHMMSS"
# Use re.sub() to replace any non-alphanumeric characters in hostname with "_"
# Build and print a log filename: "{sanitized_hostname}_{timestamp}.log"
from datetime import datetime
import re
hostname = "CORE-RTR 01"
print('Challenge 22 answer:')



# Ch23: WGU Style — Get File Extension ────────────────────
# Complete the Python function get_file_extension.
# Accept a filename string and return just the file extension including the dot.
# Use os.path.splitext().
#
# Example: get_file_extension("network_log.txt") → ".txt"
# Example: get_file_extension("config.json") → ".json"
#
import os
def get_file_extension(filename):
    pass

print('Challenge 23 answer:')
print(get_file_extension("network_log.txt"))
print(get_file_extension("config.json"))



# Ch24: WGU Style — Days Since Date ───────────────────────
# Complete the Python function days_since.
# Accept a date string formatted as "YYYY-MM-DD", parse it with strptime,
# and return the number of days between that date and today as an integer.
#
# Example: days_since("2024-01-01") → (some positive integer, grows over time)
#
from datetime import datetime
def days_since(date_string):
    pass

print('Challenge 24 answer:')
print(days_since("2024-01-01"))



# Ch25: WGU Style — Find Latest Datetime ──────────────────
# Complete the Python function find_latest.
# Accept a list of datetime strings in format "%m/%d/%Y %I:%M %p".
# Parse each and return the most recent as a datetime object.
# Use max() on the parsed list.
#
# Example: find_latest(['12/15/2023 08:45 AM', '12/16/2023 11:20 AM'])
#          → datetime(2023, 12, 16, 11, 20)
#
from datetime import datetime
def find_latest(upload_times):
    pass

upload_times1 = ['12/15/2023 08:45 AM', '12/16/2023 11:20 AM', '12/14/2023 03:30 PM']
print('Challenge 25 answer:')
print(find_latest(upload_times1))
