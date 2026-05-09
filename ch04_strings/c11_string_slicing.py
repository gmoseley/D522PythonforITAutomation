# ─── Ch04 | Challenge 1: Extract the Device Type ────────────────────────────
# Slice or split hostname to print just "ROUTER" (everything before the first dash)
hostname = "ROUTER-01-FARGO"
print(hostname.split('-')[0])



# ─── Ch04 | Challenge 2: Extract the Location ────────────────────────────────
# Slice or split hostname to print just "FARGO" (everything after the last dash)
hostname = "ROUTER-01-FARGO"
print(hostname.split('-')[2])


# ─── Ch04 | Challenge 3: Reverse It ──────────────────────────────────────────
# Print hostname backwards using a slice with a step of -1
hostname = "ROUTER-01-FARGO"
print(hostname[::-1])

# ─── Ch04 | Challenge 4: Every Other Character ───────────────────────────────
# Print every other character of hostname using slice step
hostname = "ROUTER-01-FARGO"
print(hostname[::2])


# ─── Ch04 | Challenge 5: First Four Characters ───────────────────────────────
# Print just the first 4 characters of ip using slicing (not split)
ip = "192.168.1.105"
print(ip[:4])


# ─── Ch04 | Challenge 6: Last Octet ──────────────────────────────────────────
# Print just the last 3 characters of ip using a negative slice
ip = "192.168.1.105"
print(ip[:-4:-1])


# ─── Ch04 | Challenge 7: Middle Chunk ────────────────────────────────────────
# Print characters 4 through 10 of log_id using slicing
log_id = "LOG-20240115-CRITICAL-RTR01"
print(log_id[4:10])



# ─── Ch04 | Challenge 8: WGU Style — Get Device Prefix ──────────────────────
# Complete the Python function get_device_prefix.
# The function should accept a hostname string like "RTR-01-FARGO" and return
# just the prefix — everything before the first dash. Use split.
#
# Example: get_device_prefix("RTR-01-FARGO") → "RTR"
# Example: get_device_prefix("SW-CORE-01") → "SW"
#
def get_device_prefix(hostname):
    pass



# ─── Ch04 | Challenge 9: WGU Style — Build Reverse DNS ───────────────────────
# Complete the Python function build_reverse_dns.
# The function should accept an IPv4 address string like "192.168.1.10",
# reverse the order of the octets, append ".in-addr.arpa", and return the result.
# Use split, reverse (or slicing), and join.
#
# Example: build_reverse_dns("192.168.1.10") → "10.1.168.192.in-addr.arpa"
# Example: build_reverse_dns("10.0.0.1") → "1.0.0.10.in-addr.arpa"
#
def build_reverse_dns(ip):
    pass



# ─── Ch04 | Challenge 10: WGU Style — Same Subnet ────────────────────────────
# Complete the Python function same_subnet.
# The function should accept two IP address strings and a subnet mask string.
# Apply the subnet mask to both IPs using bitwise AND: convert each octet to int,
# AND it with the corresponding mask octet, then compare the results.
# Return "ip1 and ip2 are in the same subnet" or "ip1 and ip2 are not in the same subnet".
#
# Example: same_subnet("192.168.1.100", "192.168.1.200", "255.255.255.0")
#          → "192.168.1.100 and 192.168.1.200 are in the same subnet"
# Example: same_subnet("192.168.1.100", "192.168.2.200", "255.255.255.0")
#          → "192.168.1.100 and 192.168.2.200 are not in the same subnet"
#
def same_subnet(ip1, ip2, mask):
    pass

