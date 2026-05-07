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


