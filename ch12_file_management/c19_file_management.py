# ─── Ch12 | Challenge 1: Write a Log ─────────────────────────────────────────
# Write log_entries to network_log.txt — one entry per line
#log_entries = [
#    "2024-01-15 10:00 - RTR-01 connection UP",
#    "2024-01-15 10:01 - SW-01 port DOWN",
#    "2024-01-15 10:02 - FW-01 policy applied",
#]



# ─── Ch12 | Challenge 2: Read It Back ────────────────────────────────────────
# Open network_log.txt and print its full contents



# ─── Ch12 | Challenge 3: Append an Entry ─────────────────────────────────────
# Append new_entry to network_log.txt without overwriting existing lines
#new_entry = "2024-01-15 10:03 - AP-01 rebooted\n"



# ─── Ch12 | Challenge 4: Line by Line ────────────────────────────────────────
# Read network_log.txt line by line — print each with its line number starting at 1



# ─── Ch12 | Challenge 5: Does It Exist? ──────────────────────────────────────
# Use os.path.exists() to check each file before opening — print found or missing
#filenames = ["network_log.txt", "missing_config.txt", "audit_log.txt"]



# ─── Ch12 | Challenge 6: Count the Lines ─────────────────────────────────────
# Read network_log.txt and print how many lines it contains



# ─── Ch12 | Challenge 7: Find All Errors ─────────────────────────────────────
# Read network_log.txt line by line — collect and print only lines containing "ERROR"



# ─── Ch12 | Challenge 8: Make a Backup ───────────────────────────────────────
# Copy network_log.txt to network_log_backup.txt using shutil.copy()



# ─── Ch12 | Challenge 9: Clean Up ────────────────────────────────────────────
# Delete network_log_backup.txt if it exists using os.path.exists() then os.remove()



# ─── Ch12 | Challenge 10: Write a Report ─────────────────────────────────────
# Read network_log.txt, count lines by severity (INFO/WARNING/ERROR),
# write a summary report to report.txt with counts for each level



# ─── Ch12 | Challenge 11: WGU Style — File Exists Check ─────────────────────
# Complete the Python function file_exists_check.
# The function should accept a filepath string and return True if the file exists,
# False if it does not. Use os.path.exists().
#
# Example: file_exists_check("network_log.txt") → True
# Example: file_exists_check("missing.txt") → False
#
import os
def file_exists_check(filepath):
    pass



# ─── Ch12 | Challenge 12: WGU Style — Find Lines With Keyword ───────────────
# Complete the Python function find_lines_with.
# The function should accept a filepath string and a keyword string,
# open the file, and return a list of lines (stripped of whitespace/newlines)
# that contain the keyword.
#
# Example: find_lines_with("network_log.txt", "ERROR") → ["ERROR: timeout", "ERROR: retry"]
#
def find_lines_with(filepath, keyword):
    pass



# ─── Ch12 | Challenge 13: WGU Style — Line Count ────────────────────────────
# Complete the Python function line_count.
# The function should accept a filename string, open the file, and return the
# number of lines as an integer.
# This is the exact WGU assessment question 23.
#
# Example: line_count("network_log.txt") → 3   (if the file has 3 lines)
#
def line_count(filename):
    pass



# ─── Ch12 | Challenge 14: WGU Style — Write Dict to CSV ─────────────────────
# Complete the Python function write_dict_to_csv.
# The function should accept a filename string and append two predefined device
# records to it using csv.DictWriter. Use append mode ('a') and extrasaction='ignore'.
# Do NOT write a header row (the file already has one). Write these two rows:
#   data = [
#       {"device_name": "Router1", "ip_address": "192.168.1.1"},
#       {"device_name": "Router2", "ip_address": "192.168.1.2"},
#   ]
# The fieldnames are ["device_name", "ip_address"].
# This matches exact WGU assessment question 26.
#
# Example: write_dict_to_csv("devices.csv")  → appends 2 rows to the file
#
import csv
def write_dict_to_csv(filename):
    pass


