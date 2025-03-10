#!/usr/bin/env python3
############################################################
# Developed by: Baruch 
# Description: practice the string variables methods
## Task 3
# Create python script file where you:
# - Create variable for holding your spouse (wife/husband) name
# - Check and print the type of that variable.
# - Create variable for holding your spouses age
# - Convert age variable to type string
# - Create variable to hold your credit card details (if you wish, you can send them over the email to me: Joking....) 
# - print() them away
# - Save the file and run it
# Date:09/03/2025                                                                                                                                   #
# Version: 1.0.0
############################################################
from datetime import date

delta = date.today() - date(1973, 1, 14) 

my_wife = "Genia Gudesblat"
her_age = str(delta.days//365)
my_card = dict(
   id    = "112233445566",
   valid = "12/2025",
   icv   = "010",
)
print(f"Shalom.\n\nMy wife's name is {my_wife}. She is {her_age} years old.")
print(f"My credit card is:")
for key, value in my_card.items():
    print(f"\t{key}: {value}")
