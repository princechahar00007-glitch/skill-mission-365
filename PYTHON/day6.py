# ========================================
# Python Day 6 - Master Program 
# ========================================


print(" ========================================")
print(" Python Day 6 - Master Program ")
print(" ========================================")

# ========================================
# For Loop 
# ========================================
print("\n1. For Loop")

for i in range(1,6):
    print("Welecome Bro", i)

# ========================================
# Range()
# ========================================
print("\n2. Range")

print("1 to 10")
for i in range (1, 11):
    print(i)

print("\n Even Numbers")
for i in range (2 , 21 ,2):
    print(i)

print("\nCountdown")
for i in range(10 , 0 ,-1):
    print(i)

# ========================================
# While Loop 
# ========================================
print("\n3. While Loop")

i = 1 

while i <= 5:
    print("count :", i)
    i += 1

# ========================================
# Break 
# ========================================
print("\n4. Break")

for i in range(1,11):

    if i == 6:
        break

    print(i)

# ========================================
# Continue
# ========================================
print("\n5. Continue")

for i in range (1, 11):

    if i == 5:
        continue

    print(i)

# ========================================
# Nested Loop 
# ========================================
print("\n6. Nested Loop")

for i in range(3):

    for j in range(3):

        print(i , j)

# ========================================
# Star Pattern 
# ========================================
print("\n7. Star Pattern")

for i in range(3):
        for j in range (5):
            print("*", end="")
        print()

# ========================================
# Table Generator
# ========================================
print("\n8. Table Generator")

num = int(input("Enter Number: "))

for i in range(1,11):
    print(num, "x", i, "=", num * i)

print("\n======================================")
print("Day 6 Program Completed")
print("=====================================")