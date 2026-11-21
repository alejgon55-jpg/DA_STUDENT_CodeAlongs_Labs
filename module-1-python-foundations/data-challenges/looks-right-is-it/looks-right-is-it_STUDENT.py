#!/usr/bin/env python3
"""Looks Right. Is It?: see DataChallengeOverview&Steps.md for the steps."""

DATA_FILE = "../data/timesheet_hours.csv"  # edit the filepath with the data

with open(DATA_FILE) as f:
    lines = f.read().splitlines()


# ===== Day 1 =====

# Step 1: Follow the TypeError in `weekly_hours()` Back to Its Cause

def add_hours(total, hours):
    return total + hours


def weekly_hours(lines, emp_id):
    total = 0
    for row in lines[1:]:
        parts = row.split(",")
        if parts[0] == emp_id:
            total = add_hours(total, int(parts[3]))
    return total


print("Rosa Alvarez, weekly hours:", weekly_hours(lines, "E101"))

# Step 1, answer 1:
# Rosa worked 40 hours 
# Step 1, answer 2:
# The last line tells me the error, and the lines above show which functions were called and where it happened. 
# Step 1, answer 3:
# The error happend in add_hours(), but the actual bug was in weekly_hours() because it read the wronjg column. 


# Step 2: Trace the ZeroDivisionError Back to the Hand-Typed Staff List

def days_worked(lines, emp_id):
    days = 0
    for row in lines[1:]:
        if row.split(",")[0] == emp_id:
            days = days + 1
    return days


staff = []

for row in lines[1:]:
    emp_id = row.split(",")[0]
    if emp_id not in staff:
        staff.append(emp_id)
print("employess in the files:", len(staff))

for emp_id in staff:
    hours = weekly_hours(lines, emp_id)
    days = days_worked(lines, emp_id)
    print(emp_id, "| hours:", hours, "| days:", days,
          "| average per day:", hours / days)

# Step 2, answer 1:
# There are 5 employees in the csv
# Step 2, answer 2:
# Three employee lines printed before the crash. It stopped at E106.
# Step 2, answer 3:
# The bug was in the staff list because E106 was not in the CSV, causing divisons by zero. 


# ===== Day 2 =====

# Step 3: Find Why Four of the Five Weekly Hour Totals Are Wrong

records = []
for row in lines[1:]:
    emp_id, name, day, hours, rate = row.split(",")
    records.append({"id": emp_id, "name": name, "day": day,
                    "hours": int(hours), "rate": float(rate)})

employee_ids = []
for r in records:
    if r["id"] not in employee_ids:
        employee_ids.append(r["id"])

for emp in employee_ids:
    total = 0
    name = ""
    for r in records:
        if r["id"] == emp:
            name = r["name"]
            total = total + r["hours"]
    print(emp, name, "| weekly hours:", total)

# Step 3, answer 1:
# Rosa worked 40 hours and Mei worked 32 hours.
# Step 3, answer 2:
# Total kept adding the previous employees's hours because total = 0 was outside the loop. 
# Step 3, answer 3:
# Rosa was correct because she started at 0. The other employees had previous hours added. 


# Step 4: Fix Two Overtime Bugs That Overpay the Firm by $1,810 a Week

def weekly_pay(hours, rate):
    if hours > 40:
        return 40 * rate + (hours - 40) * rate * 1.5
    return hours * rate


owed_overtime = 0
payroll = 0.0
for emp in employee_ids:
    total = 0
    name = ""
    rate = 0.0
    for r in records:
        if r["id"] == emp:
            name = r["name"]
            rate = r["rate"]
            total = total + r["hours"]
    if total > 40:
        owed_overtime = owed_overtime + 1
    pay = weekly_pay(total, rate)
    payroll = payroll + pay
    print(f"{name:16} {total:3} hrs  ${pay:>9,.2f}")

print("employees owed overtime:", owed_overtime)
print(f"TOTAL PAYROLL: ${payroll:,.2f}")

# Step 4, answer 1:
# Rosa: $960, Darnell: $1543.50, Mei: $896
# Step 4, answer 2:
# I fixed weekly_pay so only hours over 40 get overtime pay. I also changed >= to > on line 122. 
# Step 4, answer 3:
# Rosa worked exactly 40 hours, so she should only get regular pay and not count as overtime. 
