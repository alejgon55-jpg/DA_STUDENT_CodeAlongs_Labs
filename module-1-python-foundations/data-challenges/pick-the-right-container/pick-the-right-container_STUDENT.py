#!/usr/bin/env python3
"""Pick the Right Container: see DataChallengeOverview&Steps.md."""

import json

DATA_FILE = "station_taps.csv"  # edit the filepath with the data

with open(DATA_FILE) as f:
    rows = [line.split(",") for line in f.read().splitlines() if line]

header = rows[0]
taps = rows[1:]


# ===== Day 1 =====

# Step 1: Write `scan_for()` and Count Its Comparisons for Three Tap IDs
def scan_for(tap_id, records):
    comparisons = 0 

    for record in records: 
        comparisons += 1

        if record[0] == tap_id:
            return comparisons

    return comparisons 
       


print("columns:", header)
print("rows in the log:", len(taps))
print("comparisons to find T001:", scan_for("T001", taps))
print("comparisons to find T040:", scan_for("T040", taps))
print("comparisons to find T999:", scan_for("T999", taps))

# Step 1, answer 1:
# T001 = 1 comparion, T040 = 40 compariosns and T999 = 40 comparisons. 
# T001 is first, T040 is last, and T999 is not in the file so it checks all 40 rows 
# Step 1, answer 2:
# I would plan around 40 comparisons because that is the worst case. 


# Step 2: Print Scan Cost at 5 to 40 Rows, Then Count a Nested Pair Loop
for size in [5, 10, 20, 40]:
    worst = scan_for("T999", taps[:size])
    print("rows:", size, "| worst-case comparisons:", worst)

pairs = 0

for x in taps:
    for tap in taps:
        pairs += 1

print(len(taps), pairs)

big = len(taps) * 10

print("worst case:", big, "pair loop:", big * big)

# Step 2, answer 1:
# 5 rows = 5 compariosns
# 10 rows = 10 compariosns
# 20 rows = 20 compariosns
# 40 rows = 40 compariosns
# 400 rows = 400 compariosns
# Pair loop: 5x5 = 25, 10x10 = 100, 20x20 = 400, 40x40 = 1600, and 400x400 = 160000.
# Step 2, answer 2:
# The scan grows by the same amount as the number of rows.
# The pair loop grows much faster because every row is compared with every row


# ===== Day 2 =====

# Step 3: Count Taps Per Card With Two Parallel Lists, and Their Comparisons

card_ids = []
tap_counts = []
comparisons = 0 
for row in taps:
    card = row[1]
    found = False
    for i in range(len(card_ids)):
        comparisons += 1
        if card_ids[i] == card:
            tap_counts[i] += 1
            found = True
            break
    if not found:
        card_ids.append(card)
        tap_counts.append(1)
busiest = tap_counts.index(max(tap_counts))
print("distinct cards:", len(card_ids))
print("comparisons the two parallel lists needed:", comparisons)
print("busiest card:", card_ids[busiest], "with", max(tap_counts), "taps")

# Step 3, answer 1:
# I expect a lot of comparisons because each card may have to search through card_ids
# Step 3, answer 2:
# The comaprion count is bigger than the number of rows because some cards have to be checked against several card IDs before a match is found.  


# Step 4: Count Taps Per Card With a Dictionary, and Stations With a Set

taps_by_card = {}
lookups = 0 

for row in taps:
    lookups += 1 
    card_ids = row[1]
    if row[1] in taps_by_card:
        taps_by_card[row[1]] += 1 
    else:
        taps_by_card[row[1]] = 1
stations = set()
for row in taps:
    stations.add(row[2])
repeat_riders = 0 
for row in taps_by_card.values():
    if row > 1:
        repeat_riders += 1 

print("distinct cards:", len(taps_by_card))
print("lookups the dictionary needed:", lookups)
print("unique stations:", len(stations), sorted(stations))
print("cards that tapped more than once:", repeat_riders)
print("taps for C001:", taps_by_card["C001"])

# Step 4, answer 1:
# I predict 40 lookups because there are 40 rows 
# Step 4, answer 2:
# Parallel lists need more searching. A dictionary goes straight to the key
# Step 4, answer 3:
# A dictionary stores card counts. A set stores unique stations. 
# Step 4, answer 4:
# The dictionary shows each acrd and how mnay times it tapped. 


# ===== Day 3 =====

# Step 5: Save the Summary as JSON and Read the TypeError a Set Causes

summary = {
    "service_day": "2026-03-02",
    "total_taps": len(taps),
    "distinct_cards": len(taps_by_card),
    "stations": stations,
    "taps_by_card": taps_by_card,
}

print("about to serialize", len(summary), "keys")

#text = json.dumps(summary, indent=2)
#print(text)

# Step 5, answer 1:
# TypeError: Object of type set is not JSON serializable
# Step 5, answer 2:
# The stations key caused it because staions is a set
# Step 5, answer 3:
# Sets cannot be saved directly as JSON


# Step 6: Write `tap_summary.json`, Reload It, and Check Which Types Survived

summary["stations"] = sorted(stations)
with open("tap_summary.json", "w") as f:
    json.dump(summary, f)

with open("tap_summary.json", "r") as f:
    reloaded = json.load(f)

print("total_taps came back as:", reloaded["total_taps"])
print("taps_by_card came back as a", type(reloaded["taps_by_card"]).__name__)
print("C001 straight out of the file:", reloaded["taps_by_card"]["C001"])
print("stations came back as a", type(reloaded["stations"]).__name__)
print("round trip identical:", reloaded["taps_by_card"] == taps_by_card)

# Step 6, answer 1:
# Yes, the file has each card and its tap count. 
# Step 6, answer 2:
# The dictionary stayed a dictionary, but stations came back as a list. 
