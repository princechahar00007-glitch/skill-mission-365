# ===========================================
# PROJECT 7 : STUDENT RESULT ANALYZER
# ===========================================

print("================================")
print("   STUDENT RESULT ANALYZER")
print("================================")

# ---------------------------------
# SET 
# ---------------------------------
subject = {"Python", "DSA", "Maths", "AI"}

print("\nSubject:")
print(subject)

subject.add("Networking")
subject.discard("Maths")

print("\nUpdate subject:")
print(subject)

# ---------------------------------------
# FUNCTIONS
# ---------------------------------------
def welcome(name):
    print("\nWelcome", name)

def student_detalis(name, course):
    print("Name :", name)
    print("Course :", course)

def total_marks(m1,m2,m3):
    return m1 + m2 + m3

def percentage(total):
    return total / 3

def result(percent):
    if percent >= 40:
        return "PASS"
    else:
        return "FAIL"

# --------------------------------------
# INPUT
# --------------------------------------
name = input("\nEnter Student Name : ")
course = input("Enter Course : ")

m1 = int(input("Python Marks : "))
m2 = int(input("DSA Marks : "))
m3 = int(input("Maths Marks : "))

# ---------------------------------------
# OUTPUT 
# ---------------------------------------
welcome(name)

student_detalis(name,course)

total = total_marks(m1 , m2 , m3)
percent = percentage(total)

print("\nTotal Marks :", total)
print("Percentage :", percent)
print("Result :", result(percent))

print("=====================================")
print("PROJECT COMPLETED")
print("=====================================")