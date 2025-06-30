import csv
import os
from collections import defaultdict

# Step 1: Read & group rows by state
state_data = defaultdict(list)

with open('users.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        state = row['state']
        state_data[state].append(row)

# Step 2: Write a file for each state
for state, rows in state_data.items():
    os.makedirs("states", exist_ok=True)
    filename = f"states/{state.replace(' ', '_')}.csv"
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['id', 'name', 'state'])
        writer.writeheader()
        writer.writerows(rows)
