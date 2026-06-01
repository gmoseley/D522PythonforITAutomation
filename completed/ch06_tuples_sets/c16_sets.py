# Ch01: VLAN Registry ───────────────────────────────────────
# Create a set of these VLAN IDs and assign it to vlans, then print it
# 10, 20, 30, 40, 50
print('Challenge 1 answer:')



# Ch02: Add a VLAN, Drop a VLAN ────────────────────────────
# Add VLAN 60 to vlans, then remove VLAN 10 — print the result
vlans = {10, 20, 30, 40, 50}
print('Challenge 2 answer:')



# Ch03: Is This VLAN Active? ────────────────────────────────
# Check if vlan_id is in vlans — print "Active" or "Not found"
vlans = {10, 20, 30, 40, 50}
vlan_id = 30
print('Challenge 3 answer:')



# Ch04: Two Sites, One Network ──────────────────────────────
# Print the union (all VLANs on either site) and intersection (VLANs on both)
site_a = {10, 20, 30, 40}
site_b = {30, 40, 50, 60}
print('Challenge 4 answer:')



# Ch05: No Duplicates Allowed ───────────────────────────────
# Convert dhcp_log to a set to deduplicate — print the unique IPs
dhcp_log = ["10.0.0.5", "10.0.0.12", "10.0.0.5", "10.0.0.8", "10.0.0.12", "10.0.0.5"]
print('Challenge 5 answer:')



# Ch06: Lock It Down ────────────────────────────────────────
# Create a frozenset from core_vlans, try to add 99 — catch the AttributeError and print a message
core_vlans = frozenset({10, 20, 30})
print('Challenge 6 answer:')



# Ch07: Discard vs Remove ───────────────────────────────────
# Try removing vlan 99 from vlans using .remove() — catch the KeyError
# Then try again with .discard() — notice no error this time
vlans = {10, 20, 30, 40, 50}
print('Challenge 7 answer:')



# Ch08: Difference ─────────────────────────────────────────
# Print the VLANs that are in site_a but NOT in site_b (the difference)
# Then print VLANs that are in site_b but NOT in site_a
site_a = {10, 20, 30, 40}
site_b = {30, 40, 50, 60}
print('Challenge 8 answer:')



# Ch09: Symmetric Difference ────────────────────────────────
# Print the VLANs that are on one site but not both (symmetric difference)
site_a = {10, 20, 30, 40}
site_b = {30, 40, 50, 60}
print('Challenge 9 answer:')



# Ch10: Subset Check ───────────────────────────────────────
# Check if required_vlans is a subset of configured_vlans — print True or False
required_vlans = {10, 20, 30}
configured_vlans = {10, 20, 30, 40, 50}
print('Challenge 10 answer:')



# Ch11: Superset Check ─────────────────────────────────────
# Check if configured_vlans is a superset of required_vlans — print True or False
required_vlans = {10, 20, 30}
configured_vlans = {10, 20, 30, 40, 50}
print('Challenge 11 answer:')



# Ch12: Disjoint Check ─────────────────────────────────────
# Check if allowed_ips and blocked_ips share no IPs — print "Clean" or "Conflict"
allowed_ips = {"10.0.0.1", "10.0.0.2", "10.0.0.3"}
blocked_ips = {"192.168.1.1", "172.16.0.1"}
print('Challenge 12 answer:')



# Ch13: Set from String ────────────────────────────────────
# Build a set of unique characters in hostname and print how many unique chars it has
hostname = "ROUTER-01-FARGO"
print('Challenge 13 answer:')



# Ch14: Sorted Set ─────────────────────────────────────────
# Print the vlans set as a sorted list (sets have no order — use sorted())
vlans = {40, 10, 50, 20, 30}
print('Challenge 14 answer:')



# Ch15: Pop an Element ─────────────────────────────────────
# Pop one element from vlans and print what was removed, then print the remaining set
# Note: pop() removes an arbitrary element from a set
vlans = {10, 20, 30, 40, 50}
print('Challenge 15 answer:')



# Ch16: Union Assignment ───────────────────────────────────
# Use |= to add all VLANs from new_vlans into existing_vlans in-place — print the result
existing_vlans = {10, 20, 30}
new_vlans = {30, 40, 50}
print('Challenge 16 answer:')



# Ch17: Intersection Assignment ────────────────────────────
# Use &= to keep only VLANs present in both sets — print the result
configured = {10, 20, 30, 40}
required   = {20, 30, 50}
print('Challenge 17 answer:')



# Ch18: Deduplicate and Count ──────────────────────────────
# Convert access_log to a set to find unique IPs, then print the count
access_log = [
    "10.0.0.5", "10.0.0.12", "10.0.0.5",
    "10.0.0.8", "10.0.0.12", "10.0.0.5",
    "172.16.0.1", "10.0.0.8",
]
print('Challenge 18 answer:')



# Ch19: Find Missing VLANs ─────────────────────────────────
# Print the VLANs that are required but missing from configured — sorted
required   = {10, 20, 30, 40, 50}
configured = {10, 30, 50}
print('Challenge 19 answer:')



# Ch20: Set Comprehension ──────────────────────────────────
# Build a set of all unique first octets from the ip_list using a set comprehension
# Split each IP on "." and take the first element
ip_list = ["192.168.1.1", "10.0.0.1", "192.168.2.5", "10.1.0.1", "172.16.0.1"]
print('Challenge 20 answer:')



# Ch21: Membership Test Performance ────────────────────────
# Check whether each IP in to_check is in the allowed set — print "Allowed" or "Blocked"
# (Sets use O(1) lookup — much faster than lists for large data)
allowed = {"10.0.0.1", "10.0.0.2", "192.168.1.100"}
to_check = ["10.0.0.1", "172.16.0.5", "192.168.1.100", "10.0.0.99"]
print('Challenge 21 answer:')



# Ch22: Aggregate Set Operations ───────────────────────────
# Given three site VLAN sets, find:
#   - VLANs present at ALL three sites (intersection of all three)
#   - VLANs present at ANY site (union of all three)
#   - VLANs unique to site_a (difference with the union of the other two)
site_a = {10, 20, 30, 40}
site_b = {20, 30, 50, 60}
site_c = {30, 40, 60, 70}
print('Challenge 22 answer:')



# Ch23: WGU Style — Shared VLANs ──────────────────────────
# Complete the Python function get_shared_vlans.
# Accept two sets of VLAN IDs and return a sorted list of VLANs in both sets.
#
# Example: get_shared_vlans({10, 20, 30}, {20, 30, 40}) → [20, 30]
# Example: get_shared_vlans({10, 20}, {30, 40}) → []
#
def get_shared_vlans(site_a, site_b):
    pass

print('Challenge 23 answer:')
print(get_shared_vlans({10, 20, 30}, {20, 30, 40}))
print(get_shared_vlans({10, 20}, {30, 40}))



# Ch24: WGU Style — Find Unauthorized IPs ─────────────────
# Complete the Python function find_unauthorized_ips.
# Accept a list of IP strings (logged_ips) and a set of allowed IPs.
# Return a sorted, deduplicated list of IPs from logged_ips not in allowed_ips.
#
# Example: find_unauthorized_ips(["10.0.0.5","10.0.0.1","10.0.0.5"], {"10.0.0.1"})
#          → ["10.0.0.5"]
# Example: find_unauthorized_ips(["10.0.0.1"], {"10.0.0.1"}) → []
#
def find_unauthorized_ips(logged_ips, allowed_ips):
    pass

print('Challenge 24 answer:')
print(find_unauthorized_ips(["10.0.0.5", "10.0.0.1", "10.0.0.5"], {"10.0.0.1"}))
print(find_unauthorized_ips(["10.0.0.1"], {"10.0.0.1"}))



# Ch25: WGU Style — Missing VLANs ─────────────────────────
# Complete the Python function missing_vlans.
# Accept a set of required VLAN IDs and a set of configured VLAN IDs.
# Return a sorted list of VLANs that are required but not yet configured.
#
# Example: missing_vlans({10, 20, 30}, {10, 30}) → [20]
# Example: missing_vlans({10, 20}, {10, 20, 30}) → []
#
def missing_vlans(required, configured):
    pass

print('Challenge 25 answer:')
print(missing_vlans({10, 20, 30}, {10, 30}))
print(missing_vlans({10, 20}, {10, 20, 30}))
