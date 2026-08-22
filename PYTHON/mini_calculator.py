# ------------------------------
# Mini Calculator Project 
# ------------------------------

print("===== MINI CALCULATOR =====")

num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

print("\n------ Result -------")

print("Addition =", num1 + num2)
print("Subtraction =", num1 - num2)
print("Multiplication =", num1 * num2)

if num2 != 0: 
    print("Division =", num1 / num2)
    print("Modulus =", num1 % num2)
    print("Floor Division =", num1 // num2)

else:
    print("Division = Not Possible (Cannot divide by zero)")
    print("Modulus = Not Possible")
    print("Floor Division = Not Possible")        

print("Power =", num1 ** num2)

print("\nThank You For Using Mini Calculator!")