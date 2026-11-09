#!/usr/bin/env python3
"""One Job at a Time: see DataChallengeOverview&Steps.md for the steps."""

import json

DATA_FILE = "../data/pantry_donations.csv"  # edit the filepath with the data


# ===== Day 1 =====

# Step 1: Write the Read-and-Validate Pair, Each With a Docstring
def read_donations(path):
    """Return a verdict and a reason for one record."""
    records = []
    with open(path) as f:
        for line in f.read().splitlines()[1:]:
            if line.strip():
                records.append(line)
    return records


def validate_donation(record):
    """CHeck if a donation record is valid."""
    parts = record.split(",")
    if len(parts) != 5:
        return False, "wrong field count"
    if parts[2].strip() == "":
        return False, "missing category"
    try:
        float(parts[3])
    except ValueError:
        return False, "pounds is not a number"
    return True, ""

   
records = read_donations(DATA_FILE)
valid = []
for record in records:
    ok, reason = validate_donation(record)
    if ok:
        valid.append(record)
    else:
        print("rejected", record.split(",")[0] + ":", reason)

print(len(valid), "usable records out of", len(records))

# Step 1, answer 1:
# One record holds a donation ID, item, category, pounds, and date. D009, D013, and D017 have errors. 
# Step 1, answer 2:
# Each valid record has 5 fields, a category that is not blank and a pounds value that can be converted to a number. 


# Step 2: Write `summarize_donations()` for the Category Breakdown Only
def summarize_donations(valid_records):
    """One loop and one dict that totals pounds per category."""
    by_category = {}
    total_pounds = 0.0
    for record in valid_records:
        parts = record.split(",")
        category = parts[2]
        pounds = float(parts[3])

        if category not in by_category:
            by_category[category] = {"donations": 0, "pounds": 0.0}
        by_category[category]["donations"] += 1
        by_category[category]["pounds"] += pounds
        total_pounds += pounds
    return {
        "records": len(valid_records),
        "total_pounds": total_pounds, 
        "by_category": by_category
    }

summary = summarize_donations(valid)
print("records:", summary["records"], "| total pounds:",
      summary["total_pounds"])
for category, stats in summary["by_category"].items():
    print(category, stats["donations"], "donations,", stats["pounds"],
          "lbs")

# Step 2, answer 1:
# I counted the grains category and got 80 pounds. This matches the grains total printed by my program. 


# ===== Day 2 =====

# Step 3: Add `export_summary()` and `run_pipeline()`, Then Print Docstrings
def export_summary(summary, path):
    """Write the summary to a JSON file."""
    with open(path, "w") as f:
        json.dump(summary, f, indent=2)
    return path 


def run_pipeline(in_path, out_path, summarize):
    """Run_pipeline that calls the others in order, the summarizeris one of its parameters."""
    kept = []
    for record in read_donations(in_path):
        ok, reason = validate_donation(record)
        if ok: 
            kept.append(record)
    return export_summary(summarize(kept), out_path)


written = run_pipeline(DATA_FILE, "donation_summary.json",
                       summarize_donations)
print("wrote", written)
for func in [read_donations, validate_donation, summarize_donations,
             export_summary]:
    print(func.__name__ + ":", func.__doc__.splitlines()[0])

# Step 3, answer 1:
# print(len) shows the built in len function, while print(len("abc")) prints 3. The parantheses call the fucntion and pass in a value. 
# Step 3, answer 2:
# No, each docstring describes one job for its fucntion. None of them needs "and" twice. 


# Step 4: Swap In `summarize_by_day()` and Count the Functions You Edited
def summarize_by_day(valid_records):
    """Summarize donations by day."""
    by_day = {}
    total_pounds = 0.0

    for record in valid_records:
            parts = record.split(",")
            day = parts[4]
            pounds = float(parts[3])

            if day not in by_day:
                by_day[day] = {"donations": 0, "pounds": 0.0}
            by_day[day]["donations"] += 1
            by_day[day]["pounds"] += pounds
            total_pounds += pounds
    return {
        "records": len(valid_records), 
        "total_pounds": total_pounds,
        "by_day": by_day
    }

run_pipeline(DATA_FILE, "donation_summary.json", summarize_by_day)
with open("donation_summary.json") as f:
    reloaded = json.load(f)

print("records:", reloaded["records"], "| total pounds:",
      reloaded["total_pounds"])
for day, stats in sorted(reloaded["by_day"].items()):
    print(day, stats["donations"], "donations,", stats["pounds"], "lbs")

# Step 4, answer 1:
# I did not have to edit any other function. I only changed which summarizer was passed into run_pipeline(). 
# Step 4, answer 2:
# Three dates have only 1 donation because some records were rejcted for misisng or incorrect information. The coordinator should see only valid donations. 
