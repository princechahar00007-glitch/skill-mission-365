#===================================
# PYTHON DAY 9 - MASTER PROGRAM 
#===================================

print("===================================")
print("     DAY 9 - MASTER PROGRAM ")
print("===================================")

# --------------------------------
# TUPLE 
# --------------------------------

subjects = ("Python", "DSA", "Maths")

print("\nTuple:")
print(subjects)

print("\nFirst Subject:")
print(subjects[0])

print("\nLast Subject:")
print(subjects[-1])

print("\nTuple Slicing:")
print(subjects[:2])

print("\nCount of Python:")
print(subjects.count("Python"))

print("\nIndex of DSA:")
print(subjects.index("DSA"))

# --------------------------------
# DICTIONARY  
# --------------------------------

student = {
    "name": "Prince",
    "age": 20 ,
    "course": "BCA"
}

print("\nStudent Dictionary:")
print(student)

print("\nStudent Name:")
print(student["name"])

student["age"] = 21
student["city"] = "Pilibanga"

print("\nUpdated Dictionary:")
print(student)

print("\nKeys:")
print(student.keys())

print("\nValues:")
print(student.values())

print("\nItems:")
print(student.items())

print("\nCourse:")
print(student.get("course"))\

print("\n===================================")
print("DAY 9 - MASTER PROGRAM COMPLETED")
print("===================================")