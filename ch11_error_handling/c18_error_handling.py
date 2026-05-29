# ─── Ch11 | Challenge 1: Bad Input Recovery ──────────────────────────────────
# Ask the user for a number — catch ValueError if they type something non-numeric
# Print the number doubled, or "Invalid: not a number"
print('Challenge 1 answer:')



# ─── Ch11 | Challenge 2: Catch Them All ──────────────────────────────────────
# Divide numerator by user input — handle ValueError and ZeroDivisionError separately
# Print a specific message for each error type
numerator = 100
print('Challenge 2 answer:')



# ─── Ch11 | Challenge 3: The Else Clause ─────────────────────────────────────
# Try to convert input_val to int — use else to print "Conversion successful: {n}"
# only if no error occurred; use except to print "Invalid input"
input_val = "42"
print('Challenge 3 answer:')



# ─── Ch11 | Challenge 4: Always Clean Up ─────────────────────────────────────
# Open "network_log.txt" in a try block — use finally to always print "Operation complete"
# If the file doesn't exist, print "File not found" in the except block
print('Challenge 4 answer:')



# ─── Ch11 | Challenge 5: Raise Your Own ──────────────────────────────────────
# Ask for a port number — raise ValueError with "Port out of range: {port}"
# if port is outside 1–65535; otherwise print "Port {port} accepted"
port = 70000
print('Challenge 5 answer:')



# ─── Ch11 | Challenge 6: Nested Try ──────────────────────────────────────────
# Loop through filenames — use nested try/except to handle each missing file gracefully
# Print the first line of each file, or "Missing: {filename}" if not found
filenames = ["network_log.txt", "missing_file.txt", "audit_log.txt"]
print('Challenge 6 answer:')



# ─── Ch11 | Challenge 7: Retry with Error Handling ───────────────────────────
# Simulate 3 connection attempts — raise ConnectionError on each attempt,
# catch it, print "Attempt {n} failed", and after 3 failures print "Connection failed"
print('Challenge 7 answer:')



# ─── Ch11 | Challenge 8: Validate Before You Act ─────────────────────────────
# Validate that ip is a string and port is an int in range 1–65535
# Raise TypeError if ip is not a string; raise ValueError if port is out of range
# Print "Config valid" if both pass
ip = "10.0.0.1"
port = 99999
print('Challenge 8 answer:')



# ─── Ch11 | Challenge 9: Log the Exception ───────────────────────────────────
# Wrap a risky division in try/except — write the error message to "error_log.txt"
# using append mode instead of printing, so the script keeps running silently
numerator = 10
denominator = 0
print('Challenge 9 answer:')



# ─── Ch11 | Challenge 10: Multiple Except Blocks ─────────────────────────────
# Try to: 1) convert input_str to int, 2) index into a list at that position
# Handle ValueError, IndexError, and a bare Exception separately
input_str = "abc"
data = [10, 20, 30]
print('Challenge 10 answer:')



# ─── Ch11 | Challenge 11: Re-Raise ───────────────────────────────────────────
# Catch the ValueError from int("bad"), print "Caught it", then re-raise it
# Wrap the whole thing in an outer try/except to catch the re-raised error and print "Outer caught"
print('Challenge 11 answer:')



# ─── Ch11 | Challenge 12: Custom Exception Class ─────────────────────────────
# Define a custom exception class InvalidHostnameError that inherits from ValueError
# Raise it if hostname doesn't start with "RTR", "SW", or "FW"
# Catch it and print the error message
hostname = "LAPTOP-01"
print('Challenge 12 answer:')



# ─── Ch11 | Challenge 13: Try/Except/Else/Finally ────────────────────────────
# Open "network_log.txt" — in else, count and print the number of lines
# In except, print "Could not open file"
# In finally, print "Done"
print('Challenge 13 answer:')



# ─── Ch11 | Challenge 14: Suppress Specific Errors ───────────────────────────
# Use contextlib.suppress(FileNotFoundError) to silently skip missing files
# Print the content of each file that exists; skip those that don't
from contextlib import suppress
files = ["network_log.txt", "ghost.txt", "audit_log.txt"]
print('Challenge 14 answer:')



# ─── Ch11 | Challenge 15: Assert Statement ────────────────────────────────────
# Use assert to verify that ip_list is not empty before processing it
# Catch the AssertionError and print "Cannot process empty list"
ip_list = []
print('Challenge 15 answer:')



# ─── Ch11 | Challenge 16: Exception Chaining ─────────────────────────────────
# Catch a ValueError and raise a new RuntimeError from it using "raise X from e"
# Catch the RuntimeError in an outer block and print both messages
print('Challenge 16 answer:')



# ─── Ch11 | Challenge 17: Validate a Config Dict ─────────────────────────────
# Raise KeyError if "hostname" key is missing from config
# Raise TypeError if config["port"] is not an int
# Raise ValueError if config["port"] is not in range 1–65535
# Print "Config OK" if all pass
config = {"hostname": "RTR-01", "port": "8080"}
print('Challenge 17 answer:')



# ─── Ch11 | Challenge 18: Catch and Count ────────────────────────────────────
# Process each item in data — try to convert to int and square it
# Count and print how many conversions succeeded and how many failed
data = ["10", "abc", "20", "3.5", "7", "bad", "99"]
print('Challenge 18 answer:')



# ─── Ch11 | Challenge 19: Timeout Simulation ─────────────────────────────────
# Loop through hosts and "connect" — raise TimeoutError if the host ends with "99"
# Catch it, print "Timeout: {host}", and continue to the next host
# Print "Done" after all hosts are processed
hosts = ["10.0.0.1", "10.0.0.99", "10.0.0.2", "10.0.0.99", "10.0.0.3"]
print('Challenge 19 answer:')



# ─── Ch11 | Challenge 20: Context Manager (with statement) ───────────────────
# Open "network_log.txt" using a with statement — print each line stripped of whitespace
# The with statement handles closing automatically (no explicit close needed)
print('Challenge 20 answer:')



# ─── Ch11 | Challenge 21: Graceful Degradation ───────────────────────────────
# Try to import the 'ujson' module — if it's not installed, fall back to 'json'
# Print which module is being used: "Using ujson" or "Falling back to json"
print('Challenge 21 answer:')



# ─── Ch11 | Challenge 22: Nested Validation Chain ────────────────────────────
# Validate all three: cidr must contain "/", prefix must be digit, prefix 0–32
# Raise ValueError with a descriptive message for each failure
# Print "Valid CIDR" if all pass
cidr = "192.168.1.0/33"
print('Challenge 22 answer:')



# ─── Ch11 | Challenge 23: WGU Style — Safe Divide ───────────────────────────
# Complete the Python function safe_divide.
# Accept two numbers a and b. Return a / b as a float.
# If b is zero, catch ZeroDivisionError and return None.
#
# Example: safe_divide(10, 2) → 5.0
# Example: safe_divide(10, 0) → None
#
def safe_divide(a, b):
    pass

print('Challenge 23 answer:')
print(safe_divide(10, 2))
print(safe_divide(10, 0))



# ─── Ch11 | Challenge 24: WGU Style — Safe Int Convert ──────────────────────
# Complete the Python function safe_int_convert.
# Accept a string value, attempt to convert it to int, return the int.
# If conversion fails (ValueError), return -1.
#
# Example: safe_int_convert("42") → 42
# Example: safe_int_convert("abc") → -1
#
def safe_int_convert(value):
    pass

print('Challenge 24 answer:')
print(safe_int_convert("42"))
print(safe_int_convert("abc"))



# ─── Ch11 | Challenge 25: WGU Style — Validate Port ─────────────────────────
# Complete the Python function validate_port.
# Accept an integer port number.
# If the port is outside 1–65535, raise ValueError("Invalid port: {port}").
# If valid, return True.
#
# Example: validate_port(443) → True
# Example: validate_port(99999) → raises ValueError: "Invalid port: 99999"
#
def validate_port(port):
    pass

print('Challenge 25 answer:')
print(validate_port(443))
try:
    print(validate_port(99999))
except ValueError as e:
    print(e)
