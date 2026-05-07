# ─── Ch04 | Challenge 1: Shout It Out ────────────────────────────────────────
# Print device_name in all uppercase, then all lowercase
device_name = "Core-Router-01"
print(device_name.upper())
print(device_name.lower())


# ─── Ch04 | Challenge 2: Clean User Input ────────────────────────────────────
# Strip the whitespace from messy_input and print the cleaned result
messy_input = '   192.168.1.1   '
print(messy_input.replace(' ',''))



# ─── Ch04 | Challenge 3: Find and Replace ────────────────────────────────────
# Replace "failed" with "timed out" in the error message and print it
error_msg = "Connection to 192.168.1.1 has failed"
print(error_msg.replace('failed','timed out'))


# ─── Ch04 | Challenge 4: Word by Word ────────────────────────────────────────
# Split sentence into a list of words and print each word on its own line
sentence = "The firewall denied access to the internal subnet"
print(sentence.split())


# ─── Ch04 | Challenge 5: Rejoin the Crew ─────────────────────────────────────
# Join the hostnames list into a single comma-separated string and print it
hostnames = ["RTR-01", "SW-02", "FW-03", "AP-04"]
print(", ".join(hostnames))



# ─── Ch04 | Challenge 6: How Many A's? ───────────────────────────────────────
# Count how many times the letter 'a' appears in log_line (case-insensitive)
log_line = "authentication failure at 192.168.1.100 - invalid password attempt"
print(log_line.count('a'))



# ─── Ch04 | Challenge 7: Does It Match? ──────────────────────────────────────
# Check if filename starts with "log" AND ends with ".txt" — print True or False
filename = "log_2024_01_15.txt"
print(filename.startswith('log') and filename.endswith('.txt'))

