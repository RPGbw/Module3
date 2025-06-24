"""
Author: Brennan Whiting
Date:06/19/2025
Program: GPA-Testing.py 
Description: This program will accept student's last names and GPA to test to see where they land in Dean or honor role class
"""

while True:
    L_name = input("Please put in your last name (or 'ZZZ' to quit): ")
    if L_name == "ZZZ":
        break
    
    F_name = input("Please enter your first name: ")
    
    try:
        GPA = float(input("Now Please enter your GPA: "))
    except ValueError:
        print("Please enter a valid number for GPA")
        continue

    if GPA < 0.0 or GPA > 4.0:
        print("Not Possible. GPA must be between 0.0 and 4.0. Try again.")
        continue

    if GPA >= 3.5:
        print(f"{F_name} {L_name} has made Dean's List")
    elif GPA >= 3.25:
        print(f"{F_name} {L_name} has made the Honor Roll")