# ─── Ch06 | Challenge 1: VLAN Registry ───────────────────────────────────────
# Create a set of these VLAN IDs and print it: 10, 20, 30, 40, 50



# ─── Ch06 | Challenge 2: Add a VLAN, Drop a VLAN ────────────────────────────
# Add VLAN 60 to the set, then remove VLAN 10 — print the result



# ─── Ch06 | Challenge 3: Is This VLAN Active? ────────────────────────────────
# Check if vlan_id is in the set — print "Active" or "Not found"
#vlan_id = 30



# ─── Ch06 | Challenge 4: Two Sites, One Network ──────────────────────────────
# Print the union (all VLANs combined) and intersection (VLANs on both sites)
#site_a = {10, 20, 30, 40}
#site_b = {30, 40, 50, 60}



# ─── Ch06 | Challenge 5: No Duplicates Allowed ───────────────────────────────
# Convert dhcp_log to a set to remove duplicate IPs, then print the unique ones
#dhcp_log = ["10.0.0.5", "10.0.0.12", "10.0.0.5", "10.0.0.8", "10.0.0.12", "10.0.0.5"]



# ─── Ch06 | Challenge 6: Lock It Down ────────────────────────────────────────
# Create a frozenset from core_vlans, try to add 99 — catch the error and print a message
#core_vlans = frozenset({10, 20, 30})



# ─── Ch06 | Challenge 7: WGU Style — Shared VLANs ───────────────────────────
# Complete the Python function get_shared_vlans.
# The function should accept two sets of VLAN IDs, return a sorted list
# of VLANs that appear in both sets (the intersection).
#
# Example: get_shared_vlans({10, 20, 30}, {20, 30, 40}) → [20, 30]
# Example: get_shared_vlans({10, 20}, {30, 40}) → []
#
def get_shared_vlans(site_a, site_b):
    pass



# ─── Ch06 | Challenge 8: WGU Style — Deduplicate IPs ────────────────────────
# Complete the Python function deduplicate_ips.
# The function should accept a list of IP address strings that may contain
# duplicates, and return a sorted list of unique IPs.
#
# Example: deduplicate_ips(["10.0.0.5", "10.0.0.1", "10.0.0.5"]) → ["10.0.0.1", "10.0.0.5"]
# Example: deduplicate_ips(["192.168.1.1"]) → ["192.168.1.1"]
#
def deduplicate_ips(ip_list):
    pass


