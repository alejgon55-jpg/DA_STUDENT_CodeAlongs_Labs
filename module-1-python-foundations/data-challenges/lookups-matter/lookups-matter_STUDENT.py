#!/usr/bin/env python3
"""Lookups Matter: see DataChallengeOverview&Steps.md for the steps."""

import csv

DATA_FILE = "member_directory.csv"  # edit the filepath with the data
CHECKINS_FILE = "door_checkins.txt"  # edit the filepath with the data

with open(DATA_FILE, newline="") as f:
    members = list(csv.DictReader(f))


# Step 1: Write `find_linear()` to Return the Member and Its Comparisons
def find_linear(members, member_id):
    comparisons = 0 
    for row in members:
        comparisons += 1
        if row["member_id"] == member_id:
            return row, comparisons 
    return None, comparisons 


row, count = find_linear(members, "M1150")
print("members in the directory:", len(members))
print("found:", row["name"], "at", row["home_branch"])
print("comparisons:", count)

# Step 1, answer 1:
# I predict 150 comparisons because M1150 is the 150th member in the list. 


# Step 2: Total the Comparisons for All 20 Swipes in `door_checkins.txt`

with open(CHECKINS_FILE) as f:
    swipes = f.read().splitlines()

linear_total = 0 
not_members = 0

for member_id in swipes:
    row, count = find_linear(members, member_id)
    if row is None:
        print(member_id, "| NOT A MEMBER | comparisons:", count)
        not_members += 1
    else:
        print(member_id, "|", row["name"], "| comparisons:", count)
    linear_total += count

print("swipes:", len(swipes), "| not members:", not_members)
print("linear total comparisons:", linear_total)

# Step 2, answer 1:
# The first three swipes cost 4, 12, and 27 comparisons. Their total is 43 comparisons. A non-member cost 312 comparions. 
# Step 2, answer 2:
# The non-member cost more because the program checks all 312 members without finding a match. 


# Step 3: Build `members_by_id` and Find the Swipe Where It Pays Off

members_by_id = {}
build_steps = 0 

for row in members:
    members_by_id[row["member_id"]] = row
    build_steps += 1
def find_dict(members_by_id, member_id):
    return members_by_id.get(member_id), 1

print("build cost:", build_steps, "| keys in the dict:", len(members_by_id))


linear_running = 0 
dict_running = build_steps
pays_off_at = None
swipe_number = 0 
for member_id in swipes:

    _, linear_count = find_linear(members, member_id)
    _, dict_count = find_dict(members_by_id, member_id)
    swipe_number += 1
    linear_running += linear_count
    dict_running += dict_count
    print("swipe", swipe_number, member_id, "| linear so far:", linear_running, "| dict so far:", dict_running)
    if pays_off_at is None and dict_running < linear_running: 
        pays_off_at = swipe_number

print("dict pays off at swipe:", pays_off_at)
print("morning totals | linear:", linear_running, "| dict:", dict_running)

# Step 3, answer 1:
# I predict swipe 6 because the dict will have fewer comparions than the linear search. 
# Step 3, answer 2:
# I used member_id because each member has their own ID, making them easier to find. The dict pulled ahead at swipe 6. 
# Step 3, answer 3:
# A list would be better if there were only a few swipes because building a dicttakes extra work. 


# Step 4: Test an AI Speed Claim Against Your Totals and Write a Verdict
ai_claim = "For 20 lookups in a list of 312 members, a dictonary can be about 146 times faster than a linear search if we compare the total number of steps, including building the dictonary."
print("AI CLAIM:", ai_claim)

_, front_count = find_linear(members, swipes[0])
_, absent_count = find_linear(members, "M1313")
ratio = round(linear_running / dict_running, 1)

print("one front-of-file swipe | linear:", front_count, "| dict: 1")
print("one non-member swipe | linear:", absent_count, "| dict: 1")
print("whole morning | linear:", linear_running, "| dict:", dict_running,
      "| ratio:", ratio)

verdict = "The dictonary was about 8.8 times faster for the whole morning, including the build cost. Linear search was faster for the first swipe, but the dictonary was better after swipe 6"
print("VERDICT:", verdict)

# Step 4, answer 1:
# The AI's claim didn't match my results. It said 146 times faster, but my total was 8.8 times faster 
# Step 4, answer 2:
# The AI said it included the build cost, but its number didn't match. After seeing my totals, the correct ratio is 8.8 
