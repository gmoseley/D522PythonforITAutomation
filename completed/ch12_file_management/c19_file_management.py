# Ch01: Write a Log ─────────────────────────────────────────
# Write log_entries to "network_log.txt" — one entry per line
log_entries = [
    "2024-01-15 10:00 - RTR-01 connection UP",
    "2024-01-15 10:01 - SW-01 port DOWN",
    "2024-01-15 10:02 - FW-01 policy applied",
]
print('Challenge 1 answer:')



# Ch02: Read It Back ────────────────────────────────────────
# Open "network_log.txt" and print its full contents using .read()
print('Challenge 2 answer:')



# Ch03: Append an Entry ─────────────────────────────────────
# Append new_entry to "network_log.txt" without overwriting existing lines
new_entry = "2024-01-15 10:03 - AP-01 rebooted\n"
print('Challenge 3 answer:')



# Ch04: Line by Line ────────────────────────────────────────
# Read "network_log.txt" line by line — print each with its line number starting at 1
# Format: "1: 2024-01-15 10:00 - RTR-01 connection UP"
print('Challenge 4 answer:')



# Ch05: Does It Exist? ──────────────────────────────────────
# Use os.path.exists() to check each file before opening — print "Found" or "Missing"
import os
filenames = ["network_log.txt", "missing_config.txt", "audit_log.txt"]
print('Challenge 5 answer:')



# Ch06: Count the Lines ─────────────────────────────────────
# Read "network_log.txt" and print how many lines it contains
print('Challenge 6 answer:')



# Ch07: Find All Errors ─────────────────────────────────────
# Read "network_log.txt" line by line — collect and print only lines containing "ERROR"
print('Challenge 7 answer:')



# Ch08: Make a Backup ───────────────────────────────────────
# Copy "network_log.txt" to "network_log_backup.txt" using shutil.copy()
import shutil
print('Challenge 8 answer:')



# Ch09: Clean Up ────────────────────────────────────────────
# Delete "network_log_backup.txt" if it exists using os.path.exists() + os.remove()
print('Challenge 9 answer:')



# Ch10: Write a Report ─────────────────────────────────────
# Read "network_log.txt", count lines by severity (INFO / WARNING / ERROR)
# Write a summary report to "report.txt" with counts for each level
print('Challenge 10 answer:')



# Ch11: Read Lines into a List ─────────────────────────────
# Read all lines from "network_log.txt" into a list using .readlines()
# Strip each line of whitespace and print the list
print('Challenge 11 answer:')



# Ch12: Write Multiple Files ────────────────────────────────
# Write a separate .txt file for each device in devices
# Filename: "{hostname}.txt", Content: "hostname: {hostname}\nip: {ip}\nstatus: {status}"
devices = [
    ("RTR-01", "10.0.0.1", "UP"),
    ("SW-01",  "10.0.0.2", "DOWN"),
    ("FW-01",  "10.0.0.3", "UP"),
]
print('Challenge 12 answer:')



# Ch13: Parse a Log File ───────────────────────────────────
# Read "network_log.txt" line by line — build a list of dicts with keys "timestamp" and "message"
# Split each line on " - " to separate the two parts; print the list
print('Challenge 13 answer:')



# Ch14: os.path Toolkit ────────────────────────────────────
# For the path below, print: basename, dirname, extension, and whether it exists
import os
path = "c:/Users/gmoseley/OneDrive/College/D522 - Python for IT Automation/VSCClaude/ch12_file_management/network_log.txt"
print('Challenge 14 answer:')



# Ch15: Build a File Path ──────────────────────────────────
# Use os.path.join() to build a full path from parts — print it
# Parts: base_dir, "logs", "2024", "january", "network_log.txt"
base_dir = "C:/data"
print('Challenge 15 answer:')



# Ch16: List Files in a Directory ──────────────────────────
# Use os.listdir() to print all files in the current directory
# Filter to only show .py files
print('Challenge 16 answer:')



# Ch17: Read a CSV File ────────────────────────────────────
# Write devices_csv to "devices.csv", then read it back using csv.reader
# Print each row as a list
import csv
devices_csv = "hostname,ip,role\nRTR-01,10.0.0.1,router\nSW-01,10.0.0.2,switch\n"
print('Challenge 17 answer:')



# Ch18: Write CSV with DictWriter ──────────────────────────
# Write device_records to "devices_dict.csv" using csv.DictWriter
# Include the header row
device_records = [
    {"hostname": "RTR-01", "ip": "10.0.0.1", "role": "router"},
    {"hostname": "SW-01",  "ip": "10.0.0.2", "role": "switch"},
]
print('Challenge 18 answer:')



# Ch19: Read JSON Config ───────────────────────────────────
# Write device_config to "device_config.json" using json.dump
# Read it back with json.load and print just the "hostname" value
import json
device_config = {"hostname": "CORE-RTR-01", "ip": "10.0.0.1", "role": "core"}
print('Challenge 19 answer:')



# Ch20: Search a File and Replace ─────────────────────────
# Read "network_log.txt", replace every occurrence of "DOWN" with "OFFLINE"
# Write the modified content back to the same file
print('Challenge 20 answer:')



# Ch21: Rotate a Log ───────────────────────────────────────
# If "network_log.txt" has more than 3 lines, rename it to "network_log.bak"
# and create a fresh empty "network_log.txt"
# Print "Rotated" or "No rotation needed"
print('Challenge 21 answer:')



# Ch22: Walk a Directory ───────────────────────────────────
# Use os.walk() to print all .py files found anywhere under the project root
# Print the full path for each file found
import os
root = "c:/Users/gmoseley/OneDrive/College/D522 - Python for IT Automation/VSCClaude"
print('Challenge 22 answer:')



# Ch23: WGU Style — File Exists Check ─────────────────────
# Complete the Python function file_exists_check.
# Accept a filepath string and return True if the file exists, False if not.
# Use os.path.exists().
#
# Example: file_exists_check("network_log.txt") → True
# Example: file_exists_check("missing.txt") → False
#
import os
def file_exists_check(filepath):
    pass

print('Challenge 23 answer:')
print(file_exists_check("network_log.txt"))
print(file_exists_check("missing.txt"))



# Ch24: WGU Style — Find Lines With Keyword ───────────────
# Complete the Python function find_lines_with.
# Accept a filepath string and a keyword string.
# Open the file and return a list of lines (stripped) that contain the keyword.
#
# Example: find_lines_with("network_log.txt", "ERROR") → ["ERROR: timeout", "ERROR: retry"]
#
def find_lines_with(filepath, keyword):
    pass

print('Challenge 24 answer:')
print(find_lines_with("network_log.txt", "DOWN"))



# Ch25: WGU Style — Write Dict to CSV ─────────────────────
# Complete the Python function write_dict_to_csv.
# Accept a filename string and append two predefined device records using csv.DictWriter.
# Use append mode ('a') and extrasaction='ignore'. Do NOT write a header row.
# Write these two rows:
#   data = [
#       {"device_name": "Router1", "ip_address": "192.168.1.1"},
#       {"device_name": "Router2", "ip_address": "192.168.1.2"},
#   ]
# Fieldnames: ["device_name", "ip_address"]
#
# Example: write_dict_to_csv("devices.csv") → appends 2 rows to the file
#
import csv
def write_dict_to_csv(filename):
    pass

print('Challenge 25 answer:')
write_dict_to_csv("devices.csv")
