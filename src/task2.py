#!/usr/bin/env python3
############################################################
# Developed by: Baruch 
# Description: 
## Task 2
# Create python script file where you:
# - Create variable for holding your name 
# - Create variable for holding your age 
# - Create variable for holding your pets name - use print() function to print them all.
# - Save the file and run it
# Date:07/03/2025                                                                                                                                   #
# Version: 1.0.0
############################################################
from datetime import date

delta = date.today() - date(1968, 12, 11) 
#-----------------------------------

my_name = "Baruch Gudesblat"
my_age  = delta.days//365
my_chield = "Dudi"
print(f"Shalom, My name is {my_name}. I am {my_age} yers old. I have a children {my_chield}.")
