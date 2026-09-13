#====================================
# PROJECT 5 : SMART STRING ANALYZER 
#====================================

print("====================================")
print("        SMART STRING ANALYZER")
print("====================================")

name = input("Enter Your Name: ")

print("\nOriginal Name:")
print(name)

print("\nFirst Character:")
print(name[0])

print("\nLast Character:")
print(name[-1])

print("\nFirst Three Character:")
print(name[:3])

print("\nRemaining Character:")
print(name[3:])

print("\nUpper Case:")
print(name.upper())

print("\nLower Case:")
print(name.lower())

print("\nReplace 'a' with '@':")
print(name.replace("a", "@"))

print("\nCount of 'a':")
print(name.count("a"))

print("\nFind 'a':")
print(name.find("a"))

print("\n====================================")
print("     PROJECT COMPLETED")
print("====================================")