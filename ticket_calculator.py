#!/usr/bin/python3

# psuedocode
'''
This script takes in two user inputs
- age group: integer
- movie type : (regular / premium) string

Then calculate...
- the base cost of the age using conditional statements
- the base cost of the movie type using conditional statements

Sum up the total cost
Display the result using an f-string
'''

# makes more sense to use functions for this one to make testing easier

# first function to determine which age group the user falls in
def age_group(age: int) -> str:
    if age <= 12:
        return "child"
    elif age >= 60:
        return "senior"
    else:
        return "adult"

