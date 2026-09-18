# =========================================
# PROJECT 8 : LUCKY NUMBER GAME 
# =========================================

import random
import math

print("======================================")
print("         LUCKY NUMMBER GAME")
print("======================================")

# ---------------------------------
#FUNCTION 
# ---------------------------------
def welcome(name):
    print("\nWelcome", name)
    print("Let's Play!")

# ---------------------------------
# INPUT  
# ---------------------------------
name = input("Enter Your Name : ")

welcome(name)

guess = int(input("\nGuess a number (1-10): "))

# ---------------------------------
# RANDOM NUMBER
# ---------------------------------
lucky = random.randint(1,10)

print("\nLucky Number :", lucky)

# ---------------------------------
# RESULT
# ---------------------------------
if guess == lucky:
    print("Congratulations! You Won!")
else:
    print("Better Luck Next Time!")

# ---------------------------------
# MATH MODULE 
# ---------------------------------
print("\nSquare Root of Lucky Number:")
print(math.sqrt(lucky))

print("\nFactorial of 5:")
print(math.factorial(5))

print("\nValue of Pi:")
print(math.pi)

print("\n==========================================")
print("PROJECT COMPLETED")
print("==========================================")
