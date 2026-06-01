# Ch01: Server Rack ─────────────────────────────────────────
# Create a tuple of these 5 server names and assign it to servers, then print it
# "web-01", "db-01", "cache-01", "auth-01", "backup-01"
print('Challenge 1 answer:')



# Ch02: First, Last, Middle ─────────────────────────────────
# Using the servers tuple from above, print the first, last, and middle item by index
servers = ("web-01", "db-01", "cache-01", "auth-01", "backup-01")
print('Challenge 2 answer:')



# Ch03: Unpack the Rack ─────────────────────────────────────
# Unpack location into city, country, region — print each with a label
location = ("Fargo", "USA", "Midwest")
print('Challenge 3 answer:')



# Ch04: You Can't Change This ───────────────────────────────
# Try to change the first item of servers — catch the TypeError and print why tuples are useful
servers = ("web-01", "db-01", "cache-01")
print('Challenge 4 answer:')



# Ch05: Tuple Length ────────────────────────────────────────
# Print the number of items in the rack tuple using len()
rack = ("RTR-01", "SW-01", "SW-02", "FW-01", "AP-01", "AP-02")
print('Challenge 5 answer:')



# Ch06: In Operator ─────────────────────────────────────────
# Check if "db-01" is in servers — print "Found" or "Not found"
servers = ("web-01", "db-01", "cache-01", "auth-01", "backup-01")
print('Challenge 6 answer:')



# Ch07: Negative Indexing ───────────────────────────────────
# Print the second-to-last item in rack using a negative index
rack = ("RTR-01", "SW-01", "SW-02", "FW-01", "AP-01", "AP-02")
print('Challenge 7 answer:')



# Ch08: Tuple Slicing ───────────────────────────────────────
# Print only the first three items of rack using a slice
rack = ("RTR-01", "SW-01", "SW-02", "FW-01", "AP-01", "AP-02")
print('Challenge 8 answer:')



# Ch09: Count and Index ─────────────────────────────────────
# Use .count() to find how many times "UP" appears in statuses
# Use .index() to find where "DOWN" first appears — print both
statuses = ("UP", "UP", "DOWN", "UP", "DOWN", "UP")
print('Challenge 9 answer:')



# Ch10: Concatenate Tuples ─────────────────────────────────
# Combine site_a and site_b into one tuple called all_devices — print it
site_a = ("RTR-01", "SW-01")
site_b = ("RTR-02", "SW-02", "FW-01")
print('Challenge 10 answer:')



# Ch11: Loop Over Tuple ────────────────────────────────────
# Loop through rack and print each device name on its own line
rack = ("RTR-01", "SW-01", "SW-02", "FW-01", "AP-01")
print('Challenge 11 answer:')



# Ch12: Enumerate a Tuple ──────────────────────────────────
# Use enumerate() to print each device with its slot number starting at 1
# Format: "Slot 1: RTR-01"
rack = ("RTR-01", "SW-01", "SW-02", "FW-01", "AP-01")
print('Challenge 12 answer:')



# Ch13: Tuple of Tuples ────────────────────────────────────
# Print the IP of "SW-01" by indexing into device_table
device_table = (
    ("RTR-01", "10.0.0.1"),
    ("SW-01",  "10.0.0.2"),
    ("FW-01",  "10.0.0.3"),
)
print('Challenge 13 answer:')



# Ch14: Unpack in a Loop ───────────────────────────────────
# Loop through device_table and unpack each tuple into name and ip — print both with a label
device_table = (
    ("RTR-01", "10.0.0.1"),
    ("SW-01",  "10.0.0.2"),
    ("FW-01",  "10.0.0.3"),
)
print('Challenge 14 answer:')



# Ch15: Convert List to Tuple ──────────────────────────────
# Convert device_list to a tuple, print it, then verify it's a tuple with type()
device_list = ["RTR-01", "SW-01", "FW-01"]
print('Challenge 15 answer:')



# Ch16: Convert Tuple to List, Modify, Convert Back ────────
# Convert rack to a list, replace "OLD-SW" with "NEW-SW", convert back to tuple and print
rack = ("RTR-01", "OLD-SW", "FW-01")
print('Challenge 16 answer:')



# Ch17: Tuple as Dictionary Key ────────────────────────────
# Use the (site, role) tuple as a dictionary key — look up the IP for ("HQ", "Core")
network_map = {
    ("HQ", "Core"):  "10.0.0.1",
    ("HQ", "Edge"):  "10.0.0.2",
    ("DR", "Core"):  "10.1.0.1",
}
lookup = ("HQ", "Core")
print('Challenge 17 answer:')



# Ch18: Zip Two Tuples ─────────────────────────────────────
# Zip hostnames and ips together — print each pair as "RTR-01 → 10.0.0.1"
hostnames = ("RTR-01", "SW-01", "FW-01")
ips       = ("10.0.0.1", "10.0.0.2", "10.0.0.3")
print('Challenge 18 answer:')



# Ch19: Sort a Tuple ───────────────────────────────────────
# Sort the scores tuple in descending order — print as a list (sorted() returns a list)
scores = (72, 95, 88, 61, 100, 77)
print('Challenge 19 answer:')



# Ch20: Swap Values ────────────────────────────────────────
# Use tuple unpacking to swap the values of primary and backup — print both after swapping
primary = "10.0.0.1"
backup  = "10.0.0.2"
print('Challenge 20 answer:')



# Ch21: Star Unpack ────────────────────────────────────────
# Unpack record so that first gets the first item, last gets the last,
# and middle gets everything in between as a list
record = ("CORE-RTR-01", "10.0.0.1", "router", "HQ", "UP")
print('Challenge 21 answer:')



# Ch22: Named Tuple ────────────────────────────────────────
# Use collections.namedtuple to create a Device type with fields: hostname, ip, role, status
# Create one device and access its fields by name — print a summary line
from collections import namedtuple
print('Challenge 22 answer:')



# Ch23: WGU Style — Get Server by Index ───────────────────
# Complete the Python function get_server.
# Accept a tuple of server name strings and an integer index.
# Return the server name at that index.
#
# Example: get_server(("web-01", "db-01", "cache-01"), 1) → "db-01"
# Example: get_server(("web-01", "db-01", "cache-01"), 0) → "web-01"
#
def get_server(servers, index):
    pass

servers1 = ("web-01", "db-01", "cache-01")
print('Challenge 23 answer:')
print(get_server(servers1, 1))
print(get_server(servers1, 0))



# Ch24: WGU Style — Unpack Device Record ──────────────────
# Complete the Python function unpack_device_record.
# Accept a tuple of exactly 4 items: (hostname, ip, role, status).
# Unpack it and return a formatted string:
# "Device: {hostname} | IP: {ip} | Role: {role} | Status: {status}"
#
# Example: unpack_device_record(("CORE-RTR-01", "10.0.0.1", "Core Router", "UP"))
#          → "Device: CORE-RTR-01 | IP: 10.0.0.1 | Role: Core Router | Status: UP"
#
def unpack_device_record(record):
    pass

r1 = ("CORE-RTR-01", "10.0.0.1", "Core Router", "UP")
r2 = ("SW-DIST-01", "10.0.0.2", "Distribution Switch", "DOWN")
print('Challenge 24 answer:')
print(unpack_device_record(r1))
print(unpack_device_record(r2))



# Ch25: WGU Style — Find Device by Role ───────────────────
# Complete the Python function find_device_by_role.
# Accept a tuple of (hostname, ip, role) tuples and a role string.
# Return the first hostname whose role matches (case-insensitive), or None if not found.
#
# Example: find_device_by_role((("RTR-01","10.0.0.1","router"),("SW-01","10.0.0.2","switch")), "router")
#          → "RTR-01"
# Example: find_device_by_role((("RTR-01","10.0.0.1","router"),), "firewall") → None
#
def find_device_by_role(devices, role):
    pass

devices1 = (("RTR-01", "10.0.0.1", "router"), ("SW-01", "10.0.0.2", "switch"), ("FW-01", "10.0.0.3", "firewall"))
print('Challenge 25 answer:')
print(find_device_by_role(devices1, "router"))
print(find_device_by_role(devices1, "firewall"))
print(find_device_by_role(devices1, "access point"))
