# ─── Capstone 4: User Access Auditor ─────────────────────────────────────────
#
# Difficulty: Intermediate
# Reference file: data/users.csv
#
# Scenario:
# Security policy at Pruhart Tech requires that:
#   - Inactive accounts (active = False) must not have VPN access
#   - Users who haven't logged in within 90 days are flagged as stale
#   - External vendors must be reviewed quarterly
#
# Requirements:
# 1. Read data/users.csv manually (no csv module — use open() and split(","))
# 2. Skip the header row
# 3. For each user, check all three policy rules above
# 4. Build a list of violation dictionaries: {username, department, violation}
# 5. Print a formatted table of all violations to the terminal
# 6. Write violations to output/access_violations.txt
# 7. Print a final count: X violations found across Y users
#
# Hint: use datetime.strptime() to parse last_login and compare to today's date
# from datetime import datetime
# today = datetime.now()
# last = datetime.strptime("2024-01-15", "%Y-%m-%d")
# days_since = (today - last).days
#
# Concepts used: file I/O, loops, lists, dictionaries, datetime, string methods, f-strings


