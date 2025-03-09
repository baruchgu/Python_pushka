#!/usr/bin/env python3
############################################################
# Developed by: Baruch 
# Description: pracice 
## Task 4
# Create python script file where you:
# - Create variable for wifi/eth/network that you are connected to, and put in it that name
# - Create variable for your laptop hostname and save the name in it
# - Concatenate the variable above with new variable named my_con
# - print() the variable
# - add id (or any number) of your connection to my_con variable and re-print it,
#
# Date:09/03/2025                                                                                                                                   #
# Version: 1.0.0
############################################################

wifi_name = "wifi3337"
server_name = "homePC"
my_con = f"{wifi_name}@{server_name}"
print("Connection:", my_con)

wifi_name += "_x04FF"
my_con = f"{wifi_name}@{server_name}"
print("ID Connection:", my_con)
