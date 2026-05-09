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



# ─── Ch04 | Challenge 8: WGU Style — Get the Site Code ───────────────────────
# Complete the Python function get_site_code.
# The function should accept a hostname string formatted as "TYPE-##-SITE",
# extract and return the site name (everything after the last dash).
#
# Example: get_site_code("ROUTER-01-FARGO") → "FARGO"
# Example: get_site_code("SW-02-DALLAS") → "DALLAS"
#
def get_site_code(hostname):
    pass



# ─── Ch04 | Challenge 9: WGU Style — Truncate Log ID ─────────────────────────
# Complete the Python function truncate_log_id.
# The function should accept a log_id string and an integer max_length,
# and return only the first max_length characters of the log_id.
#
# Example: truncate_log_id("LOG-20240115-CRITICAL-RTR01", 10) → "LOG-202401"
# Example: truncate_log_id("LOG-20240115-CRITICAL-RTR01", 3) → "LOG"
#
def truncate_log_id(log_id, max_length):
    pass



# ─── Ch04 | Challenge 10: WGU Style — Reverse the Octets ─────────────────────
# Complete the Python function reverse_ip_octets.
# The function should accept an IPv4 address string, split it into octets,
# reverse the order of the octets, and return them joined back with dots.
#
# Example: reverse_ip_octets("192.168.1.105") → "105.1.168.192"
# Example: reverse_ip_octets("10.0.0.254") → "254.0.0.10"
#
def reverse_ip_octets(ip):
    pass

