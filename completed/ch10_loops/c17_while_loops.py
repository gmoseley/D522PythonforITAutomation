# Ch01: Count to Ten ────────────────────────────────────────
# Use a while loop to print numbers 1 through 10
print('Challenge 1 answer:')



# Ch02: Countdown ───────────────────────────────────────────
# Count down from 10 to 1 using a while loop, then print "Liftoff!"
print('Challenge 2 answer:')



# Ch03: Break on Command ────────────────────────────────────
# Keep prompting the user for input — break out of the loop when they type "quit"
# Print "Goodbye!" when the loop ends
print('Challenge 3 answer:')



# Ch04: Skip the Evens ──────────────────────────────────────
# Loop i from 1 to 20 — use continue to skip even numbers, only print odds
print('Challenge 4 answer:')



# Ch05: Keep Asking ─────────────────────────────────────────
# Use while True to keep asking for a number — exit only when input is a valid integer
# Print "Got it: {number}" when valid input is received
print('Challenge 5 answer:')



# Ch06: Retry Logic ─────────────────────────────────────────
# Simulate connection retries — loop up to max_retries, print each attempt number,
# then print "Connection failed after {max_retries} attempts"
max_retries = 3
host = "10.0.0.254"
print('Challenge 6 answer:')



# Ch07: While vs For ────────────────────────────────────────
# Sum all numbers 1–100 using a while loop, then again using a for loop
# Print both results and confirm they match
print('Challenge 7 answer:')



# Ch08: Poll Until Ready ────────────────────────────────────
# Simulate polling a device — loop until status is "UP", incrementing an attempt counter
# Break after 5 attempts if it never comes UP, printing "Gave up after 5 attempts"
# Use a counter variable; simulate status change by toggling after 3 tries
import random
def get_status():
    return random.choice(["DOWN", "DOWN", "UP"])

print('Challenge 8 answer:')



# Ch09: Menu Loop ───────────────────────────────────────────
# Build a text menu that keeps running until the user picks 3 (Exit)
# Options: 1) Show devices  2) Show logs  3) Exit
# Print a message for options 1 and 2; break cleanly on 3
print('Challenge 9 answer:')



# Ch10: Accumulate Until Threshold ────────────────────────
# Add packet sizes one by one until the total exceeds buffer_limit
# Print each running total, then print "Buffer full at: {total}"
buffer_limit = 1500
packet_sizes = [200, 400, 300, 500, 150, 250, 600]
print('Challenge 10 answer:')



# Ch11: Find First Match ───────────────────────────────────
# Use a while loop to scan devices for the first one with status "DOWN"
# Print its hostname, or "All UP" if none found
devices = [
    ("RTR-01", "UP"),
    ("SW-01",  "UP"),
    ("FW-01",  "DOWN"),
    ("AP-01",  "UP"),
]
print('Challenge 11 answer:')



# Ch12: Drain a Queue ──────────────────────────────────────
# Use a while loop with .pop(0) to process items from the front of the queue
# Print "Processing: {item}" for each, stop when the queue is empty
queue = ["task_backup", "task_patch", "task_reboot", "task_audit"]
print('Challenge 12 answer:')



# Ch13: Collect Valid Inputs ───────────────────────────────
# Keep asking for a hostname — add it to a list if it starts with "RTR", "SW", or "FW"
# Stop after 4 valid entries, then print the collected list
# (For testing, simulate input by iterating through a predefined list instead of input())
inputs = ["RTR-01", "LAPTOP-5", "SW-02", "unknown", "FW-03", "RTR-02"]
print('Challenge 13 answer:')



# Ch14: Nested While Loop ──────────────────────────────────
# Use nested while loops to print a 3×3 grid of "row,col" coordinates
# e.g., "0,0  0,1  0,2 / 1,0 ..."  (one row per line)
print('Challenge 14 answer:')



# Ch15: Running Average ────────────────────────────────────
# Loop through cpu_readings — keep a running total and count
# After all readings, print the average formatted to 1 decimal place
cpu_readings = [72.5, 88.1, 65.3, 91.2, 77.8, 84.0, 69.5]
print('Challenge 15 answer:')



# Ch16: While with Index ───────────────────────────────────
# Use a while loop with a manual index variable to print only even-indexed items
# from the log_lines list (index 0, 2, 4…)
log_lines = [
    "INFO: startup",
    "WARNING: high cpu",
    "ERROR: link down",
    "INFO: backup ok",
    "CRITICAL: disk full",
    "INFO: patch applied",
]
print('Challenge 16 answer:')



# Ch17: Bounded Retry with Backoff ────────────────────────
# Simulate retrying a connection — attempt up to max_retries times
# Print "Attempt {n}..." each time, then "Connected!" if attempt < 3 else "Failed"
# (Simulate success on attempt 3)
max_retries = 5
print('Challenge 17 answer:')



# Ch18: Process Until Sentinel ─────────────────────────────
# Process commands from the list until you hit "EXIT"
# Print "Running: {cmd}" for each valid command; stop and print "Session ended" on EXIT
commands = ["SHOW INTERFACES", "SHOW ROUTE", "PING 10.0.0.1", "EXIT", "SHOW VLAN"]
print('Challenge 18 answer:')



# Ch19: Build a Result List ────────────────────────────────
# Use a while loop to build a list of squared values for numbers 1 through 10
# Print the result list
print('Challenge 19 answer:')



# Ch20: Two-Pointer Convergence ────────────────────────────
# Use two index variables (lo and hi) — increment lo and decrement hi each iteration
# Stop when they meet or cross — print "lo={lo}, hi={hi}" each step
lo = 0
hi = 9
print('Challenge 20 answer:')



# Ch21: Simulate a Packet Window ──────────────────────────
# Use a while loop to slide a window of size 3 across packet_log and print each window
# e.g., window 0: [p0, p1, p2], window 1: [p1, p2, p3], ...
packet_log = [100, 200, 150, 300, 250, 180, 220]
print('Challenge 21 answer:')



# Ch22: While with Break and Else ─────────────────────────
# Search devices for hostname "FW-EDGE-01" using a while loop
# Use break when found — use the while/else clause to print "Not found" if the loop completes
devices = ["RTR-01", "SW-01", "AP-01", "FW-CORE-01", "FW-EDGE-01"]
print('Challenge 22 answer:')



# Ch23: WGU Style — Sum to N ───────────────────────────────
# Complete the Python function sum_to_n.
# Accept a positive integer n, use a while loop to sum 1 through n, return the total.
#
# Example: sum_to_n(5) → 15
# Example: sum_to_n(10) → 55
#
def sum_to_n(n):
    pass

print('Challenge 23 answer:')
print(sum_to_n(5))
print(sum_to_n(10))



# Ch24: WGU Style — Collect Even Numbers ──────────────────
# Complete the Python function collect_evens.
# Accept a positive integer limit, use a while loop to collect all even numbers
# from 2 up to and including limit (if even), return them as a list.
#
# Example: collect_evens(10) → [2, 4, 6, 8, 10]
# Example: collect_evens(7)  → [2, 4, 6]
#
def collect_evens(limit):
    pass

print('Challenge 24 answer:')
print(collect_evens(10))
print(collect_evens(7))



# Ch25: WGU Style — Identify High CPU ─────────────────────
# Complete the Python function identify_high_cpu.
# Accept a list of floats representing CPU usage percentages.
# Return a list of INTEGER INDICES where CPU > 90.0. Use a while loop (not for).
#
# Example: identify_high_cpu([85.0, 92.5, 88.0, 95.2]) → [1, 3]
# Example: identify_high_cpu([91.0, 88.8]) → [0]
# Example: identify_high_cpu([80.0, 85.0]) → []
#
def identify_high_cpu(cpu_list):
    pass

print('Challenge 25 answer:')
print(identify_high_cpu([85.0, 92.5, 88.0, 95.2]))
print(identify_high_cpu([91.0, 88.8]))
print(identify_high_cpu([80.0, 85.0]))
