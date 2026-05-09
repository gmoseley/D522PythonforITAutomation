# ─── Ch13 | Challenge 1: Know Your Environment ───────────────────────────────
# Use os to print: current working directory and a list of files in that directory
#import os



# ─── Ch13 | Challenge 2: System Info ─────────────────────────────────────────
# Use sys to print the Python version and the OS platform this is running on
#import sys



# ─── Ch13 | Challenge 3: What Time Is It? ────────────────────────────────────
# Print the current date and time formatted as: "2024-01-15 10:23:45"
#from datetime import datetime



# ─── Ch13 | Challenge 4: Roll the Dice ───────────────────────────────────────
# Simulate rolling a 6-sided die 5 times — print each result
#import random



# ─── Ch13 | Challenge 5: Find the IP ─────────────────────────────────────────
# Use re to extract the IP address from log_line and print it
#import re
#log_line = "2024-01-15 10:23:45 - Device 192.168.1.105 unreachable - check routing"



# ─── Ch13 | Challenge 6: Read a Config ───────────────────────────────────────
# Write device_config to device_config.json, read it back, print only the ip value
#import json
#device_config = {"hostname": "CORE-RTR-01", "ip": "10.0.0.1", "role": "core"}



# ─── Ch13 | Challenge 7: Walk the Directory ──────────────────────────────────
# Use os.walk() to print every file in the Python project folder (non-recursive is fine)
#import os



# ─── Ch13 | Challenge 8: Build a Timestamp Filename ─────────────────────────
# Use datetime to generate a log filename like: "log_20240115_102345.txt" and print it
#from datetime import datetime



# ─── Ch13 | Challenge 9: Pick a Random Device ────────────────────────────────
# Load devices.txt into a list, use random.choice() to pick one and print it
#import random



# ─── Ch13 | Challenge 10: Your Own Module ────────────────────────────────────
# Create helpers.py in this folder with two functions:
#   - ping_check(ip): prints "Pinging {ip}..."
#   - categorize(hostname): returns "Router", "Switch", "Firewall", or "Unknown"
# Import helpers here and call both functions



# ─── Ch13 | Challenge 11: WGU Style — Get File Extension ────────────────────
# Complete the Python function get_file_extension.
# The function should accept a filename string and return just the file extension
# including the dot. Use os.path.splitext().
#
# Example: get_file_extension("network_log.txt") → ".txt"
# Example: get_file_extension("config.json") → ".json"
#
import os
def get_file_extension(filename):
    pass



# ─── Ch13 | Challenge 12: WGU Style — Days Since Date ───────────────────────
# Complete the Python function days_since.
# The function should accept a date string formatted as "YYYY-MM-DD",
# parse it using datetime.strptime, and return the number of days between that
# date and today (datetime.now()) as an integer.
#
# Example: days_since("2024-01-01") → (some positive integer, grows over time)
#
from datetime import datetime
def days_since(date_string):
    pass



# ─── Ch13 | Challenge 13: WGU Style — Extract All IPs ───────────────────────
# Complete the Python function extract_all_ips.
# The function should accept a text string and use re.findall() with the pattern
# r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b' to find all IPv4 addresses.
# Return them as a list.
#
# Example: extract_all_ips("Host 10.0.0.1 and 192.168.1.5 down") → ["10.0.0.1", "192.168.1.5"]
# Example: extract_all_ips("No IPs here") → []
#
import re
def extract_all_ips(text):
    pass



# ─── Ch13 | Challenge 14: WGU Style — Find Latest ───────────────────────────
# Complete the Python function find_latest.
# The function should accept an unordered list of datetime strings, parse each one
# using the format "%m/%d/%Y %I:%M %p", and return the most recent as a datetime object.
# Use max() with a key or on the parsed list.
# This matches exact WGU assessment question 29.
#
# Example: find_latest(['12/15/2023 08:45 AM', '12/16/2023 11:20 AM'])
#          → datetime(2023, 12, 16, 11, 20)
#
def find_latest(upload_times):
    pass


