# Task 1
'''lst = [10,20,30,40,50]
lst.append(30)
print(lst)
lst.pop()
print(lst)'''
# =======================================
# Task 2
'''details = {"name":"Saurav","age":20,"Marks":90,"Course":"BCA"}
print(details)
details["Marks"] = 75
print(details)
print(details.keys())
print(details.values())'''
# ================================================
# Task 3
'''st1 = {2,3,4,5,6,7}
st2 = {3,4,5,9,10,11}
union_set = st1.union(st2)

intersection = st1.intersection(st2)
print(st1)
print(st2)
print(f"After union {union_set}")
print(f"After intersection{intersection}")'''
# =====================================================
# Task 4
'''studnt = [
    {"name":"Saurav","marks":80},
    {"name":"Anjali","marks":85},
    {"name":"Priyam","marks":80}
]
print("Student names: ")
for student in studnt:
    print(student["name"])

highest = studnt[0]
for student in studnt:
    if student["marks"]>highest["marks"]:
        highest = student

print(f"Highest Marks")
print(f"Name : {highest["name"]}")
print(f"Marks : {highest["marks"]}")'''
# ========================================================
# Task 5
