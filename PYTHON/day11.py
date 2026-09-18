# =============================================
# PYTHON DAY 11 - MASTER PROGRAM 
# =============================================

print("=======================================")
print("     DAY 11 MASTER PROGRAM")
print("=======================================")

# --------------------------
# MATH MOODULE
# --------------------------
import math 

print("\nSquare Root of 144:")
print(math.sqrt(144))

print("\nFactorial of 5:")
print(math.factorial(5))

print("\nCeil of 8.2:")
print(math.ceil(8.2))

print("\nFloor of 8.9:")
print(math.floor(8.9))

print("\nValue of Pi:")
print(math.pi)

# ------------------------------
# RANDOM MODULE
# ------------------------------
import random

print("\nRandom Number (1-10):")
print(random.randint(1, 10))

colors  = ["Red", "Blue", "Green", "Black"]

print("\nRandom Color:")
print(random.choice(colors))

print("\nRandom Decimal:")
print(random.random())

print("\nRandom Range (10 - 20):")
print(random.randrange(10,20))

# ------------------------------
# IMPORT STYLES 
# ------------------------------
from math import sqrt

print("\nUsing from import:")
print(sqrt(81))

import math as m 

print("\nUsing Alias:")
print(m.sqrt(100))

print("\n===============================================")
print("DAY 11 MASTER PROGRAM COMPPLETED")
print("===============================================")