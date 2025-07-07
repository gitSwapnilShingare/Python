my_tuple = (1,2,3)

print(my_tuple)

print(my_tuple[1])

 #my_tuple[1] = 22


# data = ('Swapnil', 'Maharashtra', 404)
#
# name, state, code = data
#
# name, _, code = data
#
# print(data)

for items in my_tuple:
    print(items)

for idx, val in enumerate(my_tuple):
    print(f"{idx} :{val}")

dataa = (('swapnil', 25), ('pratap', 27), ('vaibhav', 26))

for name, age in dataa:
    print(f"Name is {name} and age is {age}")

my_tuple = [x*x for x in range(5)]
print(my_tuple)