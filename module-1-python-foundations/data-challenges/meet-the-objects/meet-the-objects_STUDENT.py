#!/usr/bin/env python3
"""Meet the Objects: see DataChallengeOverview&Steps.md for the steps."""

import json

DATA_FILE = "../data/bike_stations.json"  # edit the filepath with the data

with open(DATA_FILE) as f:
    stations = json.load(f)


# ===== Day 1 =====

# Step 1: Reproduce the Parallel-List Bug and Name the Wrong Stations

names = []
bikes = []

for station in stations: 
    names.append(station["name"])
    bikes.append(station["bikes_available"])

names.pop(2)
print("stations in the file:", len(stations))
for i in range(len(names)):
    print(names[i], "|", bikes[i], "bikes")

# Step 1, answer 1:
#
# Step 1, answer 2:
#
# Step 1, answer 3:
#


# Step 2: Define the Station Class and Prove Two Instances Are Independent
class Station:
    def __init__(self, station_id, name, capacity, bikes_available, needs_maintenance=False):
        self.station_id = station_id
        self.name = name
        self.capacity = capacity
        self.bikes_available = bikes_available
        self.needs_maintenance = needs_maintenance
    def needs_restock(self):
        return self.bikes_available < self.capacity / 4

fleet = []
for s in stations:
    fleet.append(Station(s["station_id"], s["name"], s["capacity"], s["bikes_available"], s["needs_maintenance"]))

busy = fleet[1]
quiet = fleet[-1]
print("Before:", busy.needs_restock(), quiet.needs_restock()) 
busy.bikes_available = 0
print("After:", busy.needs_restock(), quiet.needs_restock())

# Step 2, answer 1:
#
# Step 2, answer 2:
#
# Step 2, answer 3:
#
# Step 2, answer 4:
#


# ===== Day 2 =====

# Step 3: Add `__str__` and Find Out Which of Four Prints It Changes
print(fleet[0])
print(fleet[:2])

class Station:
    def __init__(self, station_id, name, capacity, bikes_available, needs_maintenance=False):
        self.station_id = station_id
        self.name = name
        self.capacity = capacity
        self.bikes_available = bikes_available
        self.needs_maintenance = needs_maintenance
    def needs_restock(self):
        return self.bikes_available < self.capacity / 4
    def __str__(self):
        return f"{self.name}: {self.bikes_available} of {self.capacity} bikes"

fleet = []
for s in stations:
    fleet.append(Station(s["station_id"], s["name"], s["capacity"], s["bikes_available"], s["needs_maintenance"]))

print(fleet[0])
print(fleet[:2])

# Step 3, answer 1:
#
# Step 3, answer 2:
#


# Step 4: Add `__repr__` and Print the Van List for You and the Dispatcher
class Station:
    def __init__(self, station_id, name, capacity, bikes_available, needs_maintenance=False):
        self.station_id = station_id
        self.name = name
        self.capacity = capacity
        self.bikes_available = bikes_available
        self.needs_maintenance = needs_maintenance
    def needs_restock(self):
        return self.bikes_available < self.capacity / 4
    def __str__(self):
        return f"{self.name}: {self.bikes_available} of {self.capacity} bikes"
    def __repr__(self):
        return f"Station({self.name!r}, {self.bikes_available})"

fleet = []
for s in stations:
    fleet.append(Station(s["station_id"], s["name"], s["capacity"], s["bikes_available"], s["needs_maintenance"]))
van_list = []
for station in fleet:
    if station.needs_restock():
        van_list.append(station)
print(van_list)
for station in van_list:
    print(station)


# Step 4, answer 1:
#
# Step 4, answer 2:
#
# Step 4, answer 3:
#
