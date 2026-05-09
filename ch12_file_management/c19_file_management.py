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



# ─── Ch12 | Challenge 11: WGU Style — Count File Lines ──────────────────────
# Complete the Python function count_file_lines.
# The function should accept a filepath string, open the file, count the lines,
# and return the count as an integer.
#
# Example: count_file_lines("network_log.txt") → 20
#
def count_file_lines(filepath):
    pass



# ─── Ch12 | Challenge 12: WGU Style — Find Lines With Keyword ───────────────
# Complete the Python function find_lines_with.
# The function should accept a filepath string and a keyword string,
# read the file line by line, collect all lines that contain keyword,
# and return them as a list of strings (with newlines stripped).
#
# Example: find_lines_with("network_log.txt", "ERROR") → ["ERROR: ...", "ERROR: ..."]
#
def find_lines_with(filepath, keyword):
    pass



# ─── Ch12 | Challenge 13: WGU Style — Write Report Lines ────────────────────
# Complete the Python function write_report.
# The function should accept a filepath string and a list of strings,
# write each string as a line to the file, and return the number of lines written.
#
# Example: write_report("report.txt", ["Line 1", "Line 2"]) → 2
#
def write_report(filepath, lines):
    pass



# ─── Ch12 | Challenge 14: WGU Style — File Exists Check ─────────────────────
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


