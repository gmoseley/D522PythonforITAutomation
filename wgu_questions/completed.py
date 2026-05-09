# ─── WGU Assessment | Q1: Format RGB ─────────────────────────────────────────
# An outdated design file has stored red, blue, and green (RGB) color values
# as separate integer values within a list. Combine all three color values into
# a single string value properly formatted as an RGB color.
# A formatted RGB color does not contain space characters between values.
#
# Example: format_rgb([255, 165, 13]) → "rgb(255,165,13)"
# Example: format_rgb([0, 0, 0]) → "rgb(0,0,0)"

def format_rgb(rgb):
    rgb = ','.join(str(v) for v in rgb)
    return f'rgb({rgb})'


# ─── WGU Assessment | Q2: Minutes to Hours ───────────────────────────────────
# Complete the Python function minutes_to_hours. The function should accept an
# integer representing the execution time of a process in minutes, convert the
# value from minutes to hours, and return a float. The function should utilize
# float division and not integer division.
#
# Example: minutes_to_hours(90) → 1.5
# Example: minutes_to_hours(45) → 0.75

def minutes_to_hours(minutes):
    return minutes / 60
