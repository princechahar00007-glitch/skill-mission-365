#==========================================
# PYTHON DAY 8 - MASTER PROGRAM 
#==========================================

print("====================================")
print("     DAY 8 - MASTER PROGRAM")
print("====================================")

text = input("Enter Your Name: ")

print("\nOriginal String : ")
print(text)

#-----------------------------
# INDEXING
#-----------------------------
print("\nFirst Character: ")
print(text[0])

print("\nLast Character: ")
print(text[-1])

#-----------------------------
# SLICING
#-----------------------------
print("\nFirst Three Characters:")
print(text[:3])

print("\nRemaining Characters:")
print(text[3:])

#-----------------------------
# STRING METHODS 
#-----------------------------
print("\nUpper Case:")
print(text.upper())

print("\nLower Case:")
print(text.lower())

print("\nReplace Example:")
print(text.replace("a", "@"))

print("\nFind Letter 'a':")
print(text.find("a"))

print("\nCount Letter 'a':")
print(text.count("a"))

print("\n====================================")
print("   DAY 8 - MASTER PROGRAM COMPLETED")
print("====================================")