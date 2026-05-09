# ─── Ch06 | Challenge 1: Server Rack ─────────────────────────────────────────
# Create a tuple of these 5 server names and print it
# "web-01", "db-01", "cache-01", "auth-01", "backup-01"



# ─── Ch06 | Challenge 2: First, Last, Middle ─────────────────────────────────
# Using the tuple above, print the first, last, and middle item by index



# ─── Ch06 | Challenge 3: Unpack the Rack ─────────────────────────────────────
# Unpack location into city, country, region — print each with a label
#location = ("Fargo", "USA", "Midwest")



# ─── Ch06 | Challenge 4: You Can't Change This ───────────────────────────────
# Try to change the first item of servers — catch the TypeError and print why tuples are useful
#servers = ("web-01", "db-01", "cache-01")



# ─── Ch06 | Challenge 5: WGU Style — Get Server by Index ────────────────────
# Complete the Python function get_server.
# The function should accept a tuple of server name strings and an integer index,
# and return the server name at that index.
#
# Example: get_server(("web-01", "db-01", "cache-01"), 1) → "db-01"
# Example: get_server(("web-01", "db-01", "cache-01"), 0) → "web-01"
#
def get_server(servers, index):
    pass



# ─── Ch06 | Challenge 6: WGU Style — Unpack Device Record ───────────────────
# Complete the Python function unpack_device_record.
# The function should accept a tuple of exactly 4 items: (hostname, ip, role, status).
# Unpack the tuple and return a formatted string:
# "Device: {hostname} | IP: {ip} | Role: {role} | Status: {status}"
#
# Example: unpack_device_record(("CORE-RTR-01", "10.0.0.1", "Core Router", "UP"))
#          → "Device: CORE-RTR-01 | IP: 10.0.0.1 | Role: Core Router | Status: UP"
#
def unpack_device_record(record):
    pass


