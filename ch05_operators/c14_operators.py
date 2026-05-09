# ─── Ch05 | Challenge 1: The Full Toolkit ────────────────────────────────────
# Print the result of every arithmetic operator applied to a and b with a label
# Expected: addition, subtraction, multiply, divide, floor divide, modulo, exponent
a = 17
b = 5
print(f'Multiplication: {a} * {b} = {a * b}')
print(f'Addition: {a} + {b} = {a + b}')
print(f'Subtraction: {a} - {b} = {a - b}')
print(f'Division: {a} % {b} = {a % b}')



# ─── Ch05 | Challenge 2: True or False? ──────────────────────────────────────
# Print the result of each comparison between x and y
x = 42
y = 100
print(f'{x == y}')
print(f'{x != y}')
print(f'{x >= y}')
print(f'{x <= y}')
print(f'{x > y}')
print(f'{x < y}')



# ─── Ch05 | Challenge 3: Running Total ───────────────────────────────────────
# Apply +=10, -=3, *=2, //=4 to score one at a time — print score after each
score = 10
score = score += 10

# ─── Ch05 | Challenge 4: Same Object or Just Equal? ─────────────────────────
# Use 'is' and 'is not' — check if c is a, if b is None, if a is not None
#a = [1, 2, 3]
#b = None
#c = a



# ─── Ch05 | Challenge 5: Blocked IP Check ────────────────────────────────────
# Use 'in' to check if ip is blocked — use 'not in' to check if ip2 is clear
#blocked = ["192.168.1.100", "10.0.0.5", "172.16.0.50"]
#ip = "192.168.1.100"
#ip2 = "10.0.0.99"



# ─── Ch05 | Challenge 6: Access Rules ────────────────────────────────────────
# Print "Access granted" only if is_admin AND is_active — test all combinations
#is_admin = True
#is_active = False
#has_vpn = True



# ─── Ch05 | Challenge 7: Order of Operations ─────────────────────────────────
# Print both results and explain why they differ
#result1 = 2 + 3 * 4      # no parens
#result2 = (2 + 3) * 4    # with parens



# ─── Ch05 | Challenge 8: WGU Style — Minutes to Hours ────────────────────────
# Complete the Python function minutes_to_hours.
# The function should accept an integer representing minutes,
# convert to hours using float division, and return the result as a float.
#
# Example: minutes_to_hours(90) → 1.5
# Example: minutes_to_hours(45) → 0.75
#
def minutes_to_hours(minutes):
    pass



# ─── Ch05 | Challenge 9: WGU Style — Usable Hosts ────────────────────────────
# Complete the Python function usable_hosts.
# The function should accept an integer prefix_length (like 24 for /24),
# calculate the number of usable host addresses (2^(32 - prefix_length) - 2),
# and return the result as an integer.
#
# Example: usable_hosts(24) → 254
# Example: usable_hosts(30) → 2
#
def usable_hosts(prefix_length):
    pass



# ─── Ch05 | Challenge 10: WGU Style — Same Subnet ────────────────────────────
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
