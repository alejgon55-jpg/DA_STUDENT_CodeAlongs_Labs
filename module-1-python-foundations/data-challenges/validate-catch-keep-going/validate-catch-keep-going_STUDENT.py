#!/usr/bin/env python3
"""Validate, Catch, Keep Going: see DataChallengeOverview&Steps.md."""

DATA_FILE = "service_requests.csv"  # edit the filepath with the data

with open(DATA_FILE) as f:
    lines = f.read().splitlines()

header = lines[0]
rows = [line for line in lines[1:] if line]


# ===== Day 1 =====

# Step 1: Write `validate_request()` to Return a Verdict and a Reason

EXPECTED_FIELDS = 5
ALLOWED_STATUS = ["Open", "In Progress", "Closed"]

def validate_request(row):
    fields = row.split(",")
    if len(fields) != EXPECTED_FIELDS:
        return False, "wrong field count: " + str(len(fields))

    request_id, complaint_type, borough, days_open, status = fields

    if borough == (""):
        return False, "borough is empty"
    elif not status in ALLOWED_STATUS:
        return False, "status not allowed: " + status
    else:
        return True, "ok"

print(validate_request("SR-1001,Noise - Residential,Brooklyn,3,Closed"))
print(validate_request("SR-1004,Rodent,,6,Closed"))
print(validate_request("SR-1009,Water System,Queens,4,Escalated"))

# Step 1, answer 1:
# Each row represents one 311 service request. Some rows have missing information or invalid values. 
# Step 1, answer 2:
# The caller uses ok, reason = validate_request(row) to separte the two returned values. The functions returns a tuple with a Boolean and a reason 


# Step 2: Run All 15 Rows Through the Validator and Report Each Rejection

valid = 0
for row in rows:
    ok, reason = validate_request(row)
    if ok: 
        valid += 1
    else:
        print(row.split(",")[0], "REJECTED -", reason)

print("header:", header)
print("rows read:", len(rows))
print("passed Day 1 validation:", valid)

# Step 2, answer 1:
# 3 rows fail validation. SR-1004, SR-1009, SR-1011
# Step 2, answer 2:
# Sr - 1007 and SR-1013 passed even though their days_open values are invalid.  


# ===== Day 2 =====

# Step 3: Build the Days-Open Report With No Protection and Watch It Crash

#total_days = 0 
#counted = 0 

#for row in rows:
#   ok, reason = validate_request(row)
#    if not ok:
#        continue

#    fields = row.split(",")
#    days_open = int(fields[3])

#   total_days += days_open
#   counted += 1 

#   print(fields[0], days_open)

# print("average days open:", total_days / counted)

# Step 3, answer 1:
# 5 report lines print before the program crashes. SR-1007 causes the crash because "3 days" cannot be converted into an interger. 
# Step 3, answer 2:
# ValueError: invalid literal for int() with base 10: '3 days'. 5 rows were counted before the crash. 
# Step 3, answer 3:
# The loop stops at SR-1007, so the remaining rows are never checked or counted.  


# Step 4: Rebuild the Report So Every Row Is Counted or Skipped
def check_days_open(value):
    try:
        days = int(value)
    except ValueError:
        return False, "days_open is not a number: " + value

    if days < 0:
        return False, "days_open is negative: " + value 

    return True, "ok"

total_days = 0 
counted = 0
skipped = 0 

for row in rows: 
    ok, reason = validate_request(row)

    if ok:
        fields = row.split(",")
        ok, reason = check_days_open(fields[3])
    if ok:
        total_days += int(fields[3])
        counted += 1
    else:
        skipped += 1
        print(row.split(",")[0], "SKIPPED -", reason)

print("counted:", counted, "| skipped:", skipped)
print("average days open:", round(total_days / counted, 1))

# Step 4, answer 1:
# 6 rows are skipped.  SR-1007 and SR-1013 passed Day 1 validation 
# Step 4, answer 2:
# "3 days" is caught by try/except because it causes a ValueError. -3 is caught by if because it is negative.
# Step 4, answer 3:
# 10 counted + 5 skipped = 15 total rows. 
