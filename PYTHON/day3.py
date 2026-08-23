# User Input 
name = input("Enter Your Name: ")
age = int(input("Enter Your Age: "))

print("\nHello", name)

#-----------------------------
#Comparison Operators
#-----------------------------
print("\n===== COMPARISON OPERATORS =====")

print("Age == 18 :", age == 18)
print("Age != 18 :", age != 18)
print("Age > 18  :", age > 18)
print("Age < 18  :", age <18)
print("Age >= 18 :", age >= 18)
print("Age <= 18 :", age <= 18)

#-----------------------------
#Boolean
#-----------------------------
print("\n===== BOOLEAN =====")

is_adult  = age >= 18 

print("Is Adult :", is_adult)
print("Data Type:", type(is_adult))

#-----------------------------
#if - else 
#-----------------------------
print("\n===== IF ELSE =====")

if age >= 18: 
    print("You Can Vote")
else:
    print("You Cannot Vote")

#-----------------------------
#elif
#-----------------------------
print("\n==== elif =====")

if age >= 60:
    print("Senior Citizen")

elif age >=18:
    print("Adult")

else:
    print("Minor")

#-----------------------------
#AND Operator 
#-----------------------------
print("\n===== AND =====")

has_id  =True

if age >= 18 and has_id:
    print("Entry Allowed")
else:
    print("Entry Not Allowed")

#-----------------------------
#OR Operator
#-----------------------------
print("\n===== OR =====")

is_student = False 

if is_student or age < 18: 
    print("Student Discount Available")
else:
    print("No Discount")

#-----------------------------
#NOT Operator 
#-----------------------------
print("\n===== NOT =====")

is_logged_in = False

if not is_logged_in:
    print("Please Login")

print("\n===== PROGRAM FINISHED =====")