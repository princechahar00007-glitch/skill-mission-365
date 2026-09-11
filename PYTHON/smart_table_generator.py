# ========================================
# PROJECT 3 : SMART TABLE GENERATOR 
# ========================================

print("====================================")
print("      Smart Table Generator")
print("====================================")

#User Input 
name = input("Enter Your Name: ")
number = int(input("Enter a Number : "))
limit = int(input("Enter Table Limit:"))

print("\n==================================")
print("Hello", name)
print("Multipliction Table Of", number)
print("==================================\n")

for i in range(1 , limit + 1):
    print(number , "x", i, "=" , number * i)

choice = input("\n Do you want another table? (yes/no): ").lower()

if choice == "yes":
    print("Run the program again.")
else:
    print("Good Bye", name)

print("\n==================================")
print("THANK YOU FOR USING")
print("SMART TABLE GENERATOR")
print("==================================")