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
# parse it using datetime, and return the number of days between that date
# and today as an integer.
#
# Example: days_since("2024-01-01") → (some positive integer)
#
from datetime import datetime
def days_since(date_string):
    pass



# ─── Ch13 | Challenge 13: WGU Style — Extract All IPs ───────────────────────
# Complete the Python function extract_all_ips.
# The function should accept a text string, use re.findall() with a pattern
# to extract all IPv4 addresses, and return them as a list.
#
# Example: extract_all_ips("Host 10.0.0.1 and 192.168.1.5 are down") → ["10.0.0.1", "192.168.1.5"]
# Example: extract_all_ips("No IPs here") → []
#
import re
def extract_all_ips(text):
    pass



# ─── Ch13 | Challenge 14: WGU Style — Load JSON Config ──────────────────────
# Complete the Python function load_json_config.
# The function should accept a filepath string, open and parse the JSON file,
# and return the resulting Python dictionary.
#
# Example: load_json_config("data/device_config.json") → [{"hostname": "CORE-RTR-01", ...}, ...]
#
import json
def load_json_config(filepath):
    pass


