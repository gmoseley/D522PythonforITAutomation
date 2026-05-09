# ─── Ch10 | Challenge 1: Count to Ten ────────────────────────────────────────
# Use a while loop to print numbers 1 through 10



# ─── Ch10 | Challenge 2: Countdown ───────────────────────────────────────────
# Count down from 10 to 1 using a while loop, then print "Liftoff!"



# ─── Ch10 | Challenge 3: Break on Command ────────────────────────────────────
# Keep prompting the user for input — break out of the loop when they type "quit"



# ─── Ch10 | Challenge 4: Skip the Evens ──────────────────────────────────────
# Loop i from 1 to 20 — use continue to skip even numbers, only print odds



# ─── Ch10 | Challenge 5: Keep Asking ─────────────────────────────────────────
# Use while True to keep asking for a number — only exit when input is a valid int



# ─── Ch10 | Challenge 6: Retry Logic ─────────────────────────────────────────
# Simulate connection retries — loop up to max_retries, print each attempt, then "Failed"
#max_retries = 3
#host = "10.0.0.254"



# ─── Ch10 | Challenge 7: While vs For ────────────────────────────────────────
# Sum all numbers 1-100 using a while loop, then again using a for loop — compare results



# ─── Ch10 | Challenge 8: Poll Until Ready ────────────────────────────────────
# Simulate polling a device status — loop until status is "UP", incrementing attempts
# Use a counter to break after 5 attempts if it never comes UP
#import random
#def get_status(): return random.choice(["DOWN", "DOWN", "UP"])  # simulated



# ─── Ch10 | Challenge 9: Menu Loop ───────────────────────────────────────────
# Build a simple text menu that keeps running until the user picks "Exit"
# Options: 1) Show devices  2) Show logs  3) Exit



# ─── Ch10 | Challenge 10: WGU Style — Sum to N ───────────────────────────────
# Complete the Python function sum_to_n.
# The function should accept a positive integer n, use a while loop to sum
# all integers from 1 through n (inclusive), and return the total.
#
# Example: sum_to_n(5) → 15   (1+2+3+4+5)
# Example: sum_to_n(10) → 55
#
def sum_to_n(n):
    pass



# ─── Ch10 | Challenge 11: WGU Style — Collect Even Numbers ───────────────────
# Complete the Python function collect_evens.
# The function should accept a positive integer limit, use a while loop to
# collect all even numbers from 2 up to and including limit (if even),
# and return them as a list.
#
# Example: collect_evens(10) → [2, 4, 6, 8, 10]
# Example: collect_evens(7) → [2, 4, 6]
#
def collect_evens(limit):
    pass



# ─── Ch10 | Challenge 12: WGU Style — Count Retries ─────────────────────────
# Complete the Python function count_retries.
# The function should accept a list of status strings like "DOWN" and "UP",
# use a while loop to count how many "DOWN" statuses appear before the first "UP",
# and return that count. If "UP" never appears, return the total list length.
#
# Example: count_retries(["DOWN", "DOWN", "UP", "DOWN"]) → 2
# Example: count_retries(["DOWN", "DOWN", "DOWN"]) → 3
#
def count_retries(statuses):
    pass



# ─── Ch10 | Challenge 13: WGU Style — Find First Match ───────────────────────
# Complete the Python function find_first_match.
# The function should accept a list of log strings and a keyword string,
# use a while loop to find the first log entry that contains keyword,
# and return that entry. If no match is found, return None.
#
# Example: find_first_match(["INFO: ok", "ERROR: down", "INFO: ok"], "ERROR") → "ERROR: down"
# Example: find_first_match(["INFO: ok", "INFO: ok"], "ERROR") → None
#
def find_first_match(logs, keyword):
    pass


