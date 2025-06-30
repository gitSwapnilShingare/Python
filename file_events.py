# Read entire content
with open('read.csv', 'r') as file:
    content = file.read()
    print(content)

with open('read.csv', 'r') as re:
    content = re.read()
    print(content)

# Overwrites existing file or creates a new one
with open('read.csv', 'w') as file:
    file.write("Hello Swapnil!\nIt time to chase.\n")


# Overwrites existing file or creates a new one
with open('read.csv', 'a') as file:
    file.write("\n Make it count")




