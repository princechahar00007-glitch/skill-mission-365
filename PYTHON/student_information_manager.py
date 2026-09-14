#===========================================
#   PROJECT 6 - STUDENT INFORMATION MANAGER
#===========================================


print("===================================")
print("     STUDENT INFORMATION MANAGER")
print("===================================")

# -----------------------------------------
# TUPLE
# -----------------------------------------

subjects = ("Python", "DSA", "Maths", "AI",)

print("\nSubjects:")
print(subjects)

print("\nFirst Subject:")
print(subjects[0])

print("\nLast Subject:")
print(subjects[-1])

print("\nFirst Three Subject:")
print(subjects[:3])

print("\nPython Count:")
print(subjects.count("Python"))

print("\nIndex of DSA:")
print(subjects.index("DSA"))

# -----------------------------------------
# DICTIONARY 
# -----------------------------------------
student = {
    "name" : input("\nEnter Student Name: "),
    "age" : int(input("Enter Age: ")),

    "course" : input("Enter Course: ")
}
print("\nStudent Information:")
print(student)

print("\nStudent Name:")
print(student["name"])

#Update Age
student["age"] = student["age"] + 1

#Add City 
student["city"] = input("\nEnter City: ")

print("\nUpdate Student Information: ")
print(student)

print("\nKeys:")
print(student.keys())

print("\nValues:")
print(student.values())

print("\nItems:")
print(student.items())

print("\nCourse:")
print(student.get("course"))

print("\n=====================================")
print("PROJECT COMPLETED")
print("=====================================")