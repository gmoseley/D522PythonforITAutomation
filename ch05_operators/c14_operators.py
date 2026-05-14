# ─── Ch05 | Challenge 1: The Full Arithmetic Toolkit ─────────────────────────
# Print the result of every arithmetic operator applied to a and b with a label:
# addition, subtraction, multiplication, division, floor division, modulo, exponent
a = 17
b = 5



# ─── Ch05 | Challenge 2: True or False? ──────────────────────────────────────
# Print the result of each comparison between x and y with a label
# ==, !=, >=, <=, >, <
x = 42
y = 100



# ─── Ch05 | Challenge 3: Running Total ───────────────────────────────────────
# Apply +=10, then -=3, then *=2, then //=4 to score one at a time
# Print score after each operation
score = 10



# ─── Ch05 | Challenge 4: Same Object or Just Equal? ──────────────────────────
# Use 'is' and 'is not':
#   - Check if c is a (same object)
#   - Check if b is None
#   - Check if a is not None
#   - Print each result with a label
a = [1, 2, 3]
b = None
c = a



# ─── Ch05 | Challenge 5: Blocked IP Check ────────────────────────────────────
# Use 'in' to check if ip is in the blocked list
# Use 'not in' to check if ip2 is NOT in the blocked list
# Print both results with labels
blocked = ["192.168.1.100", "10.0.0.5", "172.16.0.50"]
ip = "192.168.1.100"
ip2 = "10.0.0.99"



# ─── Ch05 | Challenge 6: Access Rules ────────────────────────────────────────
# Print "Access granted" only if is_admin AND is_active are both True
# Otherwise print "Access denied"
is_admin = True
is_active = False



# ─── Ch05 | Challenge 7: Order of Operations ─────────────────────────────────
# Print both results and explain (in a comment) why they differ
result1 = 2 + 3 * 4
result2 = (2 + 3) * 4



# ─── Ch05 | Challenge 8: Floor vs Float Division ─────────────────────────────
# Print both floor division and regular division of packets by interval
# Label each result
packets = 251
interval = 2



# ─── Ch05 | Challenge 9: Modulo in Practice ──────────────────────────────────
# Use modulo to determine if device_count is even or odd — print "Even" or "Odd"
# Then use it to get the remainder of packets split across 3 interfaces — print it
device_count = 14
packets = 100



# ─── Ch05 | Challenge 10: Exponent ───────────────────────────────────────────
# Calculate the number of usable hosts for a /24 network using exponentiation
# Formula: 2 ** (32 - prefix_length) - 2
# Print the result
prefix_length = 24



# ─── Ch05 | Challenge 11: Augmented Assignment Chain ─────────────────────────
# Start with bandwidth = 100.0
# Apply: += 50, then *= 1.1, then -= 20, then /= 2
# Print the final result rounded to 2 decimal places
bandwidth = 100.0



# ─── Ch05 | Challenge 12: Chained Comparison ─────────────────────────────────
# Use a chained comparison to check if cpu_usage is between 0 and 100 (inclusive)
# Print "Valid" or "Invalid"
cpu_usage = 87.3



# ─── Ch05 | Challenge 13: Bitwise AND for Subnet ─────────────────────────────
# Apply a bitwise AND between ip_octet and mask_octet to find the network octet
# Print the result
# Expected: 192 & 255 = 192,  168 & 255 = 168
ip_octet = 192
mask_octet = 255



# ─── Ch05 | Challenge 14: Bitwise AND Full IP ────────────────────────────────
# Convert both ip and mask strings into lists of ints
# Apply bitwise AND to each pair of octets and print the network address
# Expected: "192.168.1.0"
ip = "192.168.1.105"
mask = "255.255.255.0"



# ─── Ch05 | Challenge 15: Boolean Operators ──────────────────────────────────
# Evaluate and print each expression with a label:
#   - True and False
#   - True or False
#   - not True
#   - (cpu > 80) and (mem > 70)
cpu = 95
mem = 65



# ─── Ch05 | Challenge 16: Compound Access Check ──────────────────────────────
# Print "Full access" if is_admin is True
# Print "Read-only" if is_active and has_vpn are True (but not admin)
# Print "No access" otherwise
is_admin = False
is_active = True
has_vpn = True



# ─── Ch05 | Challenge 17: Priority Queue Score ───────────────────────────────
# Calculate a priority_score = (severity * 10) + (age_days * 2) - (ack * 5)
# Print the result
severity = 3
age_days = 7
ack = 1



# ─── Ch05 | Challenge 18: Walrus Operator Preview ────────────────────────────
# Assign the length of log_line to n, then print "Long line" if n > 60, else "Short"
# Use a normal assignment (not walrus) — this is practice for reading walrus later
log_line = "2024-01-15 10:23:45 ERROR - Core switch unreachable at 10.0.0.254"



# ─── Ch05 | Challenge 19: Safe Division Guard ────────────────────────────────
# Print packets / interval only if interval != 0 (use 'and' short-circuit or if/else)
# Otherwise print "Division by zero"
packets = 1500
interval = 0



# ─── Ch05 | Challenge 20: Bit Shift ──────────────────────────────────────────
# Left-shift 1 by 8 bits to get 256 (one octet of address space) — print it
# Right-shift 65536 by 8 bits — print the result and explain what it represents
value = 1



# ─── Ch05 | Challenge 21: Operator Precedence Puzzle ─────────────────────────
# Predict and then print the result of each expression — add a comment with your prediction
expr1 = 10 - 2 ** 3 + 1
expr2 = (10 - 2) ** 3 + 1
expr3 = 10 - (2 ** 3 + 1)
expr4 = not 0 == 0



# ─── Ch05 | Challenge 22: Build a Subnet Summary ────────────────────────────
# Given prefix_length, calculate and print:
#   - Total addresses: 2 ** (32 - prefix_length)
#   - Usable hosts: total - 2
#   - Network class: "Class C" if prefix_length >= 24, "Class B" if >= 16, else "Class A"
prefix_length = 26



# ─── Ch05 | Challenge 23: WGU Style — Minutes to Hours ──────────────────────
# Complete the Python function minutes_to_hours.
# Accept an integer representing minutes, convert to hours using float division,
# and return the result as a float.
#
# Example: minutes_to_hours(90) → 1.5
# Example: minutes_to_hours(45) → 0.75
#
def minutes_to_hours(minutes):
    pass



# ─── Ch05 | Challenge 24: WGU Style — Usable Hosts ──────────────────────────
# Complete the Python function usable_hosts.
# Accept an integer prefix_length (e.g., 24 for /24).
# Calculate 2 ** (32 - prefix_length) - 2 and return it as an integer.
#
# Example: usable_hosts(24) → 254
# Example: usable_hosts(30) → 2
#
def usable_hosts(prefix_length):
    pass



# ─── Ch05 | Challenge 25: WGU Style — Same Subnet ────────────────────────────
# Complete the Python function same_subnet.
# Accept two IP strings and a subnet mask string.
# Apply bitwise AND to each pair of octets (convert to int first).
# Return "ip1 and ip2 are in the same subnet" or "ip1 and ip2 are not in the same subnet".
#
# Example: same_subnet("192.168.1.100", "192.168.1.200", "255.255.255.0")
#          → "192.168.1.100 and 192.168.1.200 are in the same subnet"
# Example: same_subnet("192.168.1.100", "192.168.2.200", "255.255.255.0")
#          → "192.168.1.100 and 192.168.2.200 are not in the same subnet"
#
def same_subnet(ip1, ip2, mask):
    pass
