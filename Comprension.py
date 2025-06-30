students = ["Swapnil", "Amit", "Sita", "Ram", "Sneha", "Ravi"]

# Get names that start with S
s_names = [name for name in students if name.startswith("S")]
print("S names:", s_names)

u_names = [student.lower() for student in students]
print("lower_name:", u_names)

marks = [10,11,12,13,14,15,16,17,18]

odd_mark = [mark for mark in marks if mark % 2 != 0]
print(f"marks are :", odd_mark)

g_mark = [mark*0.5 for mark in marks]
print(f"growths are :", g_mark)

# practise comprension for list & dict
