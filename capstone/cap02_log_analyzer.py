# ─── Capstone 2: Log File Analyzer ───────────────────────────────────────────
#
# Difficulty: Beginner-Intermediate
# Reference file: data/network_log.txt
#
# Scenario:
# The NOC at Pruhart Tech needs a script that parses the network log and
# produces a quick incident summary so engineers know where to look first.
#
# Requirements:
# 1. Read data/network_log.txt line by line
# 2. Count total lines, and count each severity level: INFO, WARNING, ERROR, CRITICAL
# 3. Collect all CRITICAL and ERROR lines into separate lists
# 4. Print a summary report to the terminal:
#    - Total log entries
#    - Count per severity
#    - List every CRITICAL event with its timestamp and device name
# 5. Write only the ERROR and CRITICAL lines to output/incident_report.txt
# 6. Handle the case where the log file doesn't exist (try/except)
#
# Hint: each line format is: "YYYY-MM-DD HH:MM:SS SEVERITY DEVICE message"
# Use .split() to parse each field
#
# Concepts used: file I/O, loops, lists, dictionaries, string methods, error handling


