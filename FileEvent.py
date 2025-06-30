import csv

# Read and filter

filter_row = []
with open ('users.csv', 'r') as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        if row['state'] == 'Maharashtra':
            filter_row.append(row)


# filtered_rows = []
# with open('users.csv', 'r') as infile:
#     reader = csv.DictReader(infile)
#     for row in reader:
#         if row['state'] == 'Maharashtra':
#             filtered_rows.append(row)

# Write filtered rows to new file
# with open('filtered_users.csv', 'w', newline='') as outfile:
#     writer = csv.DictWriter(outfile, fieldnames=['id', 'name', 'state'])
#     writer.writeheader()
#     writer.writerows(filtered_rows)

with open('maharastra.csv', 'w', newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=['id', 'name', 'state'])
    writer.writeheader()
    writer.writerows(filter_row)

