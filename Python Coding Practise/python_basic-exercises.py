#  1. Formatted Twinkle Poem

# Write a Python program to print the following string in a specific format (see the output).
# Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
# Output :

# Twinkle, twinkle, little star,
# 	How I wonder what you are! 
# 		Up above the world so high,   		
# 		Like a diamond in the sky. 
# Twinkle, twinkle, little star, 
# 	How I wonder what you are

s_tr = "Twinkle, twinkle, little star,How I wonder what you are! Up above the world so high,Like a diamond in the sky.Twinkle, twinkle, little star,How I wonder what you are"

def print_twinkle_lyrics():
    print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\t\t Up above the world so high,\n\t\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are")

print_twinkle_lyrics()

# 2. Python Version Checker

# Write a Python program to find out what version of Python you are using.

import sys
python_version = sys.version
print(python_version)


# 3. Current DateTime Display

# Write a Python program to display the current date and time.
# Sample Output :
# Current date and time :
# 2014-07-05 14:34:14

from datetime import datetime

current_date= datetime.now()
print(current_date)


# 4. Circle Area Calculator

# Write a Python program that calculates the area of a circle based on the radius entered by the user.
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504

radius = float(input("Please provide the radius to calculate area of the circle ."))
area = 3.14 * radius ** 2
print(area)


# 5. Reverse Full Name

# Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.

first_name = input("Please enter your first name")
last_name = input("Please enter your last name")

print(f"{last_name} {first_name}")
