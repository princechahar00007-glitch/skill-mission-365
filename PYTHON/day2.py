# pyhton day 2 practice 

#string input 
name = input(" Enter your name: ")

#integer input 
age = int(input("Enter your age: "))

#float input 
height = float(input("Enter your heigth (in feet): "))

print("\n-----OUTPUT-----")

print("name:",name)
print("age:",age)
print("height:",height)

print("\n-----DATA TYPE-----")

print(type(name))
print(type(age))
print(type(height))

# integer to string conversion
age_text = str(age)

print("\nafter converting age into string:")
print(age_text)
print(type(age_text))

print("\nafter 5 years your age will be:", age + 5)


#arithmetic operators

num1 = int(input("Enter first nummber: "))
num2 = int(input("Enter second nummber: "))

print("\n--------RESULTS-------")

print("addition =", num1 +  num2)
print("subtraction=", num1 - num2)
print("multiplication=", num1  * num2)
print("division=", num1 /  num2)
print("modulus=", num1  % num2)
print("floor division=", num1  // num2)
print("power =", num1  ** num2)