
my_dict = {
    "name": "Swapnil",
    "dream_role": "Data Engineer",
    "location": "India",
    "role" : "Automation Tester"
}

# print(my_dict['role'])
#
# print(my_dict['dr'])

my_dict ['Tools'] = ['automation', 'python']

my_dict ["location"] = ["Pune"]

print(my_dict)

#print(['Tools'][1])

print(my_dict.get('name', 'Swapnil'))

for key, values in my_dict.items():
    print(f"{key} is and value is {values}")