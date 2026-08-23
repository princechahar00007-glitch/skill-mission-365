#-----------------------------
#PORJECT 2 : SMART AGE CHECKER
#-----------------------------

print("=====  SMART AGE CHECKER  =====")

#User Input 
name = input("Enter Your Name : ")
age =  int(input("Enter Your Age: "))
has_id  = input("Do you have an ID Card? (yes/no): ").lower()
is_student = input("Are you a Student? (yes/no): ").lower()

print("\n======================================")
print("hello", name)
print("======================================")

# Adult / Minor 
if age >= 18: 
    print("Status : Adult")
else:
    print("Status : Minor")

# Voting
if age >= 18: 
    print("Voting : Eligible")
else:
    print("Voting : Not Eligible")

#Driving License
if age >= 18:
    print("Driving License : Eligible")
else:
    print("Driving License : Not Eligible")

# Age Category 
if age >= 60: 
    print("Category : Senior Citizen")
elif age >= 18: 
    print("Category : Adult")
else: 
    print("Category : Child / Teen")

# AND Operator 
print("\n----- Entry Check -----")

if age >= 18 and has_id == "yes":
    print("Entry Allowed")
else:
    print("Entry Not Allowed")

#OR Operator 
print("\n-----  Discount Check -----")

if is_student == "yes" or age < 18: 
    print("Student Discount Available")
else:
    print("No Student Discount")

#NOT Operator 
print("\n----- Login Check -----")

is_logged_in = False

if not is_logged_in:
    print("Please Login")

print("\n=====================================")
print("THANK YOU FOR USING")
print("SMART AGE CHECKER")
print("=====================================")