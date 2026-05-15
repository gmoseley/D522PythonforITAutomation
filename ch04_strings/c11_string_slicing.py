# ─── Ch04 | Challenge 1: First Character ───────────────────── ### Grade: A+
# Print just the first character of hostname using an index
hostname = "ROUTER-01-FARGO"
print(hostname[0])



# ─── Ch04 | Challenge 2: Last Character ────────────────────── ### Grade: A+
# Print just the last character of hostname using a negative index
hostname = "ROUTER-01-FARGO"
print(hostname[-1])



# ─── Ch04 | Challenge 3: First Six Characters ──────────────── ### Grade: A+
# Print the first 6 characters of hostname using a slice
hostname = "ROUTER-01-FARGO"
print(hostname[:6])


# ─── Ch04 | Challenge 4: Extract the Device Type ───────────── ### Grade: A+
# Slice or split hostname to print just "ROUTER" (everything before the first dash)
hostname = "ROUTER-01-FARGO"
print(hostname[0:6])
print((hostname.split('-')[0]))



# ─── Ch04 | Challenge 5: Extract the Location ──────────────── ### Grade: A+
# Slice or split hostname to print just "FARGO" (everything after the last dash)
hostname = "ROUTER-01-FARGO"
print(hostname[10:])
print((hostname.split('-')[2]))



# ─── Ch04 | Challenge 6: Reverse It ────────────────────────── ### Grade: A+
# Print hostname backwards using a slice with a step of -1
hostname = "ROUTER-01-FARGO"
print(hostname[::-1])



# ─── Ch04 | Challenge 7: Every Other Character ─────────────── ### Grade: A+
# Print every other character of hostname using slice step
hostname = "ROUTER-01-FARGO"
print(hostname[::2])



# ─── Ch04 | Challenge 8: First Four of IP ──────────────────── ### Grade: A+
# Print just the first 4 characters of ip using slicing (not split)
ip = "192.168.1.105"
print(ip[:4])



# ─── Ch04 | Challenge 9: Last Octet ────────────────────────── ### Grade: A+
# Split ip on "." and print the last element (the last octet)
ip = "192.168.1.105"
print((ip.split('.')[-1]))



# ─── Ch04 | Challenge 10: Middle Chunk ─────────────────────── ### Grade: A+
# Print characters 4 through 10 of log_id using slicing
log_id = "LOG-20240115-CRITICAL-RTR01"
print(log_id[3:10])



# ─── Ch04 | Challenge 11: Skip the Prefix ──────────────────── ### Grade: A+
# Print log_id starting from character 4 (skip "LOG-") using a slice
log_id = "LOG-20240115-CRITICAL-RTR01"
print(log_id[4:])


# ─── Ch04 | Challenge 12: Is Last Char a Digit? ────────────── ### Grade: A+
# Use [-1] to get the last character of hostname — print True if it's a digit, False otherwise
hostname = "RTR-CORE-01"
if hostname[-1].isdigit():
    print('True')
else:
    print('False')



# ─── Ch04 | Challenge 13: Extract Prefix Length ────────────── ### Grade: A+
# Split cidr on "/" and print just the prefix length (e.g., "24")
cidr = "192.168.1.0/24"
print(cidr.split('/')[1])



# ─── Ch04 | Challenge 14: First Three Octets ───────────────── ### Grade: A+
# Split ip on ".", take the first three elements, rejoin with "." and print
# Expected: "192.168.1"
ip = "192.168.1.105"
print(".".join((ip.split('.'))[0:3]))



# ─── Ch04 | Challenge 15: Even-Index Characters ────────────── ### Grade: A+
# Print every character at an even index (0, 2, 4…) of hostname using a step slice
hostname = "SWITCH-CORE-02"
print(hostname[0::2])



# ─── Ch04 | Challenge 16: Reverse the Octets ───────────────── ### Grade: A+
# Split ip into octets, reverse the list, rejoin with "." and print
# Expected: "105.1.168.192"
ip = "192.168.1.105"
print(".".join(ip.split('.')[::-1]))



# ─── Ch04 | Challenge 17: Truncate Long Name ───────────────── ### Grade: B-
# If device_name is longer than 10 chars, print the first 10 chars + "..."
# Otherwise print as-is
device_name = "CORE-DISTRIBUTION-RTR-01"
print(device_name.count(''))
if device_name.count('') > 10:
    print(device_name[0:10])
else:
    print(device_name)



# ─── Ch04 | Challenge 18: Build Short ID ───────────────────── ### Grade: A+
# Build a short_id from hostname: first 3 chars + "-" + last 2 chars
# Expected: "RTR-01" for "RTR-EDGE-01"
hostname = "RTR-EDGE-01"
print("-".join(hostname.split('-')[0::2]))



# ─── Ch04 | Challenge 19: Extract the Asset Serial ─────────── ### Grade: A+
# The serial number is everything after the second dash.
# Split on "-", skip the first two parts, rejoin the rest with "-" and print.
# Expected: "SN-00482-A"
asset_tag = "DC-01-SN-00482-A"
print("-".join(asset_tag.split('-')[2::]))



# ─── Ch04 | Challenge 20: Mask the Last Octet ──────────────── ### Grade: A+
# Split ip, replace the last octet with "xxx", rejoin with "." and print
# Expected: "192.168.1.xxx"
ip = "192.168.1.105"
ipsplit = ip.split('.')
ipsplit[3] = "xxx"
print(".".join(ipsplit))


# ─── Ch04 | Challenge 21: Log Timestamp ──────────────────────────────────────
# Print just the date portion of log_line — the first 10 characters
# Expected: "2024-01-15"
log_line = "2024-01-15 10:23:45 ERROR - Device unreachable"



# ─── Ch04 | Challenge 22: Build PTR Record ───────────────────────────────────
# Split ip into octets, reverse them, append ".in-addr.arpa", join with "." and print
# Expected: "105.1.168.192.in-addr.arpa"
ip = "192.168.1.105"



# ─── Ch04 | Challenge 23: WGU Style — Get Device Prefix ─────────────────────
# Complete the Python function get_device_prefix.
# The function should accept a hostname string like "RTR-01-FARGO" and return
# just the prefix — everything before the first dash. Use split.
#
# Example: get_device_prefix("RTR-01-FARGO") → "RTR"
# Example: get_device_prefix("SW-CORE-01") → "SW"
#
def get_device_prefix(hostname):
    pass



# ─── Ch04 | Challenge 24: WGU Style — Build Reverse DNS ─────────────────────
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



# ─── Ch04 | Challenge 25: WGU Style — Same Subnet ────────────────────────────
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