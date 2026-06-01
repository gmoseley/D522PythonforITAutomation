# Ch01: The Full Arithmetic Toolkit ─────────────────────────
# Print the result of every arithmetic operator applied to a and b with a label:
# addition, subtraction, multiplication, division, floor division, modulo, exponent
a = 17
b = 5
print('Challenge 1 answer:')



# Ch02: True or False? ──────────────────────────────────────
# Print the result of each comparison between x and y with a label
# ==, !=, >=, <=, >, <
x = 42
y = 100
print('Challenge 2 answer:')



# Ch03: Running Total ───────────────────────────────────────
# Apply +=10, then -=3, then *=2, then //=4 to score one at a time
# Print score after each operation
score = 10
print('Challenge 3 answer:')



# Ch04: Same Object or Just Equal? ──────────────────────────
# Use 'is' and 'is not':
#   - Check if c is a (same object)
#   - Check if b is None
#   - Check if a is not None
#   - Print each result with a label
a = [1, 2, 3]
b = None
c = a
print('Challenge 4 answer:')



# Ch05: Blocked IP Check ────────────────────────────────────
# Use 'in' to check if ip is in the blocked list
# Use 'not in' to check if ip2 is NOT in the blocked list
# Print both results with labels
blocked = ["192.168.1.100", "10.0.0.5", "172.16.0.50"]
ip = "192.168.1.100"
ip2 = "10.0.0.99"
print('Challenge 5 answer:')



# Ch06: Access Rules ────────────────────────────────────────
# Print "Access granted" only if is_admin AND is_active are both True
# Otherwise print "Access denied"
is_admin = True
is_active = False
print('Challenge 6 answer:')



# Ch07: Order of Operations ─────────────────────────────────
# Print both results and explain (in a comment) why they differ
result1 = 2 + 3 * 4
result2 = (2 + 3) * 4
print('Challenge 7 answer:')



# Ch08: Floor vs Float Division ─────────────────────────────
# Print both floor division and regular division of packets by interval
# Label each result
packets = 251
interval = 2
print('Challenge 8 answer:')



# Ch09: Modulo in Practice ──────────────────────────────────
# Use modulo to determine if device_count is even or odd — print "Even" or "Odd"
# Then use it to get the remainder of packets split across 3 interfaces — print it
device_count = 14
packets = 100
print('Challenge 9 answer:')



# Ch10: Exponent ───────────────────────────────────────────
# Calculate the number of usable hosts for a /24 network using exponentiation
# Formula: 2 ** (32 - prefix_length) - 2
# Print the result
prefix_length = 24
print('Challenge 10 answer:')



# Ch11: Augmented Assignment Chain ─────────────────────────
# Start with bandwidth = 100.0
# Apply: += 50, then *= 1.1, then -= 20, then /= 2
# Print the final result rounded to 2 decimal places
bandwidth = 100.0
print('Challenge 11 answer:')



# Ch12: Chained Comparison ─────────────────────────────────
# Use a chained comparison to check if cpu_usage is between 0 and 100 (inclusive)
# Print "Valid" or "Invalid"
cpu_usage = 87.3
print('Challenge 12 answer:')



# Ch13: Bitwise AND for Subnet ─────────────────────────────
# Apply a bitwise AND between ip_octet and mask_octet to find the network octet
# Print the result
# Expected: 192 & 255 = 192,  168 & 255 = 168
ip_octet = 192
mask_octet = 255
print('Challenge 13 answer:')



# Ch14: Bitwise AND Full IP ────────────────────────────────
# Convert both ip and mask strings into lists of ints
# Apply bitwise AND to each pair of octets and print the network address
# Expected: "192.168.1.0"
ip = "192.168.1.105"
mask = "255.255.255.0"
print('Challenge 14 answer:')



# Ch15: Boolean Operators ──────────────────────────────────
# Evaluate and print each expression with a label:
#   - True and False
#   - True or False
#   - not True
#   - (cpu > 80) and (mem > 70)
cpu = 95
mem = 65
print('Challenge 15 answer:')



# Ch16: Compound Access Check ──────────────────────────────
# Print "Full access" if is_admin is True
# Print "Read-only" if is_active and has_vpn are True (but not admin)
# Print "No access" otherwise
is_admin = False
is_active = True
has_vpn = True
print('Challenge 16 answer:')



# Ch17: Priority Queue Score ───────────────────────────────
# Calculate a priority_score = (severity * 10) + (age_days * 2) - (ack * 5)
# Print the result
severity = 3
age_days = 7
ack = 1
print('Challenge 17 answer:')



# Ch18: Walrus Operator Preview ────────────────────────────
# Assign the length of log_line to n, then print "Long line" if n > 60, else "Short"
# Use a normal assignment (not walrus) — this is practice for reading walrus later
log_line = "2024-01-15 10:23:45 ERROR - Core switch unreachable at 10.0.0.254"
print('Challenge 18 answer:')



# Ch19: Safe Division Guard ────────────────────────────────
# Print packets / interval only if interval != 0 (use 'and' short-circuit or if/else)
# Otherwise print "Division by zero"
packets = 1500
interval = 0
print('Challenge 19 answer:')



# Ch20: Bit Shift ──────────────────────────────────────────
# Left-shift 1 by 8 bits to get 256 (one octet of address space) — print it
# Right-shift 65536 by 8 bits — print the result and explain what it represents
value = 1
print('Challenge 20 answer:')



# Ch21: Operator Precedence Puzzle ─────────────────────────
# Predict and then print the result of each expression — add a comment with your prediction
expr1 = 10 - 2 ** 3 + 1
expr2 = (10 - 2) ** 3 + 1
expr3 = 10 - (2 ** 3 + 1)
expr4 = not 0 == 0
print('Challenge 21 answer:')



# Ch22: Build a Subnet Summary ────────────────────────────
# Given prefix_length, calculate and print:
#   - Total addresses: 2 ** (32 - prefix_length)
#   - Usable hosts: total - 2
#   - Network class: "Class C" if prefix_length >= 24, "Class B" if >= 16, else "Class A"
prefix_length = 26
print('Challenge 22 answer:')



# Ch23: WGU Style — Minutes to Hours ──────────────────────
# Complete the Python function minutes_to_hours.
# Accept an integer representing minutes, convert to hours using float division,
# and return the result as a float.
#
# Example: minutes_to_hours(90) → 1.5
# Example: minutes_to_hours(45) → 0.75
#
def minutes_to_hours(minutes):
    pass

print('Challenge 23 answer:')
print(minutes_to_hours(90))
print(minutes_to_hours(45))



# Ch24: WGU Style — Usable Hosts ──────────────────────────
# Complete the Python function usable_hosts.
# Accept an integer prefix_length (e.g., 24 for /24).
# Calculate 2 ** (32 - prefix_length) - 2 and return it as an integer.
#
# Example: usable_hosts(24) → 254
# Example: usable_hosts(30) → 2
#
def usable_hosts(prefix_length):
    pass

print('Challenge 24 answer:')
print(usable_hosts(24))
print(usable_hosts(30))



# Ch25: WGU Style — Same Subnet ────────────────────────────
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

print('Challenge 25 answer:')
print(same_subnet("192.168.1.100", "192.168.1.200", "255.255.255.0"))
print(same_subnet("192.168.1.100", "192.168.2.200", "255.255.255.0"))
