# ======================================
# PYHTON DAY 10 - MASTER PROGRAM 
# ======================================

print("=====================================")
print("     Day 10 Master Program")
print("=====================================")

# ----------------------------------
# SET 
# ----------------------------------

subjects = {"Python", "DSA", "Maths", "AI"}

print("\nSubjects:")
print(subjects)

subjects.add("Networking")
print("\nAfter add():")
print(subjects)

subjects.discard("Maths")
print("\nAfter discard():")
print(subjects)

# ----------------------------------
# FUNCTIONS
# ----------------------------------
def welcome(name):
    print("\nWelcome", name)

welcome("Prince")

# ----------------------------------
# PARAMETERS
# ----------------------------------
def student(name, course):
    print(name, "is studying", course)

student("Prince", "BCA")

# ----------------------------------
# RETURN
# ----------------------------------
def add(a,b):
    return a + b

result = add(15, 25)

print("\nAddition Result:")
print(result)

def square(number):
    return number * number

print("\nSquare of 8:")
print(square(8))

print("\n=====================================")
print("Day 10 Master Program Completed")
print("=====================================")