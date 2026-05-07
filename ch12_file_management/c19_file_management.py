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


