# -----------------------------------
# PROJECT 4 : STUDENT RECORD MANAGER 
# -----------------------------------

print("===============================")
print("   Student Record Manager")
print("===============================")

students = ["Prince", "Rahul", "Amit", "Rohan"]

print("\nOriginal List")
print(students)


#First Student
print("\nFirst Student:")
print(students[0])

#Last Student 
print("\nLast Student:")
print(students[-1])

#Slicing 
print("\nFirst Three Students:")
print(students[:3])

#Append 
new_student = input("\nEnter New Student Name: ")
students.append(new_student)

print("\nAfter append")
print(students)

#Insert 
students.insert(1, "Mohit")

print("\nAfter insert():")
print(students)

#Remove 
students.remove("Rahul")

print("\nAfter remove():")
print(students)

#Pop
students.pop()

print("\nAfter pop():")
print(students)

print("\n==================================")
print("FINAL STUDENT LIST")
print("==================================")
print(students)