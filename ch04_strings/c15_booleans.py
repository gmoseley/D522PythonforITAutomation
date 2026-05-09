# ─── Ch04 | Challenge 1: Is It a Number? ─────────────────────────────────────
# Use .isdigit() to check user_input — if valid, convert and print x2, else warn
user_input = '67' #input('Please input a value: ')
if user_input.isdigit():
    print(int(user_input) * 2)
else:
    print('Invalid input!')



# ─── Ch04 | Challenge 2: Letters Only ────────────────────────────────────────
# Use .isalpha() to check if username is letters only — print pass or fail
username = "admin123"
if username.isalpha():
    print('pass')
else:
    print('fail')


# ─── Ch04 | Challenge 3: Upper or Lower? ─────────────────────────────────────
# Check alert_code with .isupper() and .islower() — print what it is
alert_code = "CRITICAL"
if alert_code.isupper():
    print('The alert code is uppercase')
elif alert_code.islower():
    print('The alert code is lowercase')
else:
    print('The error code is not only upper or lower case')


# ─── Ch04 | Challenge 4: Valid Hostname ──────────────────────────────────────
# Use .startswith() to check if hostname starts with "RTR" or "SW" — print valid/invalid
hostname = "SW-CORE-01"
if hostname.startswith('RTR'):
    print('The host is a router')
elif hostname.startswith('SW'):
    print('The host is a switch')
else:
    print('There are no valid hostnames in the variable')


# ─── Ch04 | Challenge 5: Store the Result ────────────────────────────────────
# Store the result of (port == 443) in a variable, use it in an if to print "Secure" or "Insecure"
port = '443'

if '443' == port:
    print('This host is secured with HTTPS')
elif '80' == port:
    print('This host is not secure')
else:
    print('The host port is not documented and may be insecure. Please refer to vendor documentation')

# ─── Ch04 | Challenge 6: Truthy or Falsy? ────────────────────────────────────
# For each value below, print whether it's truthy or falsy using an if/else
values = [0, "", "hello", [], [1], None, 42]
for value in values:
    if value:
        print('truthy')
    else:
        print('falsy')


# ─── Ch04 | Challenge 7: WGU Style — Validate IP Segment ─────────────────────
# Complete the Python function is_valid_segment.
# The function should accept a string representing one octet of an IP address,
# return True if it is a digit string AND its integer value is between 0 and 255,
# otherwise return False.
#
# Example: is_valid_segment("192") → True
# Example: is_valid_segment("256") → False
# Example: is_valid_segment("abc") → False
#
def is_valid_segment(segment):
    pass



# ─── Ch04 | Challenge 8: WGU Style — Validate Hostname Prefix ────────────────
# Complete the Python function is_valid_hostname.
# The function should accept a hostname string and return True if it starts with
# "RTR", "SW", "FW", or "AP" — otherwise return False.
#
# Example: is_valid_hostname("RTR-01-FARGO") → True
# Example: is_valid_hostname("SERVER-01") → False
#
def is_valid_hostname(hostname):
    pass

