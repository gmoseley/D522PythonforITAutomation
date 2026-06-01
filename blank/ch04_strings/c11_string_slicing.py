# Ch01: First Character ──────────────────────── ###
# Print just the first character of hostname using an index
hostname = "ROUTER-01-FARGO"
print('Challenge 1 answer:')



# Ch02: Last Character ───────────────────────── ###
# Print just the last character of hostname using a negative index
hostname = "ROUTER-01-FARGO"
print('Challenge 2 answer:')



# Ch03: First Six Characters ─────────────────── ###
# Print the first 6 characters of hostname using a slice
hostname = "ROUTER-01-FARGO"
print('Challenge 3 answer:')



# Ch04: Extract the Device Type ──────────────── ###
# Slice or split hostname to print just "ROUTER" (everything before the first dash)
hostname = "ROUTER-01-FARGO"
print('Challenge 4 answer:')



# Ch05: Extract the Location ─────────────────── ###
# Slice or split hostname to print just "FARGO" (everything after the last dash)
hostname = "ROUTER-01-FARGO"
print('Challenge 5 answer:')



# Ch06: Reverse It ───────────────────────────── ###
# Print hostname backwards using a slice with a step of -1
hostname = "ROUTER-01-FARGO"
print('Challenge 6 answer:')



# Ch07: Every Other Character ────────────────── ###
# Print every other character of hostname using slice step
hostname = "ROUTER-01-FARGO"
print('Challenge 7 answer:')



# Ch08: First Four of IP ─────────────────────── ###
# Print just the first 4 characters of ip using slicing (not split)
ip = "192.168.1.105"
print('Challenge 8 answer:')



# Ch09: Last Octet ───────────────────────────── ###
# Split ip on "." and print the last element (the last octet)
ip = "192.168.1.105"
print('Challenge 9 answer:')



# Ch10: Middle Chunk ────────────────────────── ###
# Print characters 4 through 10 of log_id using slicing
log_id = "LOG-20240115-CRITICAL-RTR01"
print('Challenge 10 answer:')



# Ch11: Skip the Prefix ─────────────────────── ###
# Print log_id starting from character 4 (skip "LOG-") using a slice
log_id = "LOG-20240115-CRITICAL-RTR01"
print('Challenge 11 answer:')



# Ch12: Is Last Char a Digit? ───────────────── ###
# Use [-1] to get the last character of hostname — print True if it's a digit, False otherwise
hostname = "RTR-CORE-01"
print('Challenge 12 answer:')



# Ch13: Extract Prefix Length ───────────────── ###
# Split cidr on "/" and print just the prefix length (e.g., "24")
cidr = "192.168.1.0/24"
print('Challenge 13 answer:')



# Ch14: First Three Octets ──────────────────── ###
# Split ip on ".", take the first three elements, rejoin with "." and print
# Expected: "192.168.1"
ip = "192.168.1.105"
print('Challenge 14 answer:')



# Ch15: Even-Index Characters ───────────────── ###
# Print every character at an even index (0, 2, 4…) of hostname using a step slice
hostname = "SWITCH-CORE-02"
print('Challenge 15 answer:')



# Ch16: Reverse the Octets ──────────────────── ###
# Split ip into octets, reverse the list, rejoin with "." and print
# Expected: "105.1.168.192"
ip = "192.168.1.105"
print('Challenge 16 answer:')



# Ch17: Truncate Long Name ──────────────────── ###
# If device_name is longer than 10 chars, print the first 10 chars + "..."
# Otherwise print as-is
device_name = "CORE-DISTRIBUTION-RTR-01"
print('Challenge 17 answer:')



# Ch18: Build Short ID ──────────────────────── ###
# Build a short_id from hostname: first 3 chars + "-" + last 2 chars
# Expected: "RTR-01" for "RTR-EDGE-01"
hostname = "RTR-EDGE-01"
print('Challenge 18 answer:')



# Ch19: Extract the Asset Serial ───────────────────────────
# The serial number is everything after the second dash.
# Split on "-", skip the first two parts, rejoin the rest with "-" and print.
# Expected: "SN-00482-A"
asset_tag = "DC-01-SN-00482-A"
print('Challenge 19 answer:')



# Ch20: Mask the Last Octet ────────────────────────────────
# Split ip, replace the last octet with "xxx", rejoin with "." and print
# Expected: "192.168.1.xxx"
ip = "192.168.1.105"
print('Challenge 20 answer:')



# Ch21: Log Timestamp ──────────────────────────────────────
# Print just the date portion of log_line — the first 10 characters
# Expected: "2024-01-15"
log_line = "2024-01-15 10:23:45 ERROR - Device unreachable"
print('Challenge 21 answer:')



# Ch22: Build PTR Record ───────────────────────────────────
# Split ip into octets, reverse them, append ".in-addr.arpa", join with "." and print
# Expected: "105.1.168.192.in-addr.arpa"
ip = "192.168.1.105"
print('Challenge 22 answer:')



# Ch23: WGU Style — Get Device Prefix ─────────────────────
# Complete the Python function get_device_prefix.
# The function should accept a hostname string like "RTR-01-FARGO" and return
# just the prefix — everything before the first dash. Use split.
#
# Example: get_device_prefix("RTR-01-FARGO") → "RTR"
# Example: get_device_prefix("SW-CORE-01") → "SW"
#
def get_device_prefix(hostname):
    pass

hostname1 = "RTR-01-FARGO"
hostname2 = "SW-CORE-01"
print('Challenge 23 answer:')
print(get_device_prefix(hostname1))
print(get_device_prefix(hostname2))



# Ch24: WGU Style — Build Reverse DNS ─────────────────────
# The function should accept an IPv4 address string like "192.168.1.10",
# reverse the order of the octets, append ".in-addr.arpa", and return the result.
# Use split, reverse (or slicing), and join.
#
# Example: build_reverse_dns("192.168.1.10") → "10.1.168.192.in-addr.arpa"
# Example: build_reverse_dns("10.0.0.1") → "1.0.0.10.in-addr.arpa"
#
def build_reverse_dns(ip):
    pass

ip1 = "192.168.1.10"
ip2 = "10.0.0.1"
print('Challenge 24 answer:')
print(build_reverse_dns(ip1))
print(build_reverse_dns(ip2))



# Ch25: WGU Style — Same Network ──────────────────────────
# Complete the Python function same_network.
# The function should accept two IP address strings and a prefix length integer (8, 16, or 24).
# Split both IPs into octets and compare the first (prefix_length // 8) octets.
# Return "ip1 and ip2 are on the same network" or "ip1 and ip2 are on different networks".
#
# Example: same_network("192.168.1.100", "192.168.1.200", 24)
#          → "192.168.1.100 and 192.168.1.200 are on the same network"
# Example: same_network("192.168.1.100", "192.168.2.200", 24)
#          → "192.168.1.100 and 192.168.2.200 are on different networks"
# Example: same_network("10.0.0.1", "10.1.0.1", 8)
#          → "10.0.0.1 and 10.1.0.1 are on the same network"
#
def same_network(ip1, ip2, prefix_length):
    pass

ip_a = "192.168.1.100"
ip_b = "192.168.1.200"
ip_c = "192.168.2.200"
print('Challenge 25 answer:')
print(same_network(ip_a, ip_b, 24))
print(same_network(ip_a, ip_c, 24))
print(same_network(ip_a, ip_c, 16))
