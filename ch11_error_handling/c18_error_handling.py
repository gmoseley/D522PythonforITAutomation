# ─── Ch11 | Challenge 1: Bad Input Recovery ──────────────────────────────────
# Ask the user for a number — catch ValueError if they type something non-numeric



# ─── Ch11 | Challenge 2: Catch Them All ──────────────────────────────────────
# Divide 100 by user input — handle both ValueError and ZeroDivisionError separately
#numerator = 100



# ─── Ch11 | Challenge 3: The Else Clause ─────────────────────────────────────
# Try to convert input to int — use else to print "Conversion successful!" only if no error



# ─── Ch11 | Challenge 4: Always Clean Up ─────────────────────────────────────
# Open "network_log.txt" in a try block — use finally to always print "Operation complete"



# ─── Ch11 | Challenge 5: Raise Your Own ──────────────────────────────────────
# Ask for a port number — raise ValueError with a message if it's outside 1-65535
#valid_range = (1, 65535)



# ─── Ch11 | Challenge 6: Nested Try ──────────────────────────────────────────
# Loop through filenames — use nested try/except to handle each missing file gracefully
#filenames = ["network_log.txt", "missing_file.txt", "audit_log.txt"]



# ─── Ch11 | Challenge 7: Retry with Error Handling ───────────────────────────
# Simulate 3 connection attempts — raise a ConnectionError on each, catch it,
# print the attempt number, and after 3 failures print "Connection failed"



# ─── Ch11 | Challenge 8: Validate Before You Act ─────────────────────────────
# Validate that ip is a string, port is an int, and port is in range —
# raise appropriate errors for each violation
#ip = "10.0.0.1"
#port = 99999



# ─── Ch11 | Challenge 9: Log the Exception ───────────────────────────────────
# Wrap a risky operation in try/except — write the error message to error_log.txt
# instead of printing it, so the script doesn't crash visibly


