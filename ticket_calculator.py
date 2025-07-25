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
    # Children (age 12 and under)
    if age <= 12:
        return "child"
    # Seniors (age 60 and above)
    elif age >= 60:
        return "senior"
    # Adults (age 13-59)
    # have to add after seniors since otherwise the condition would be met for any adult
    else:
        return "adult"

# second function to calculate ticket price based on age group and movie type
def calculate_ticket_price(age: int, movie_type: str) -> int:
    category = age_group(age)

    if category == "child":
        # $8 for regular movies, $10 for premium movies
        return 8 if movie_type == "regular" else 10
    elif category == "adult":
        # $12 for regular movies, $15 for premium movies
        return 12 if movie_type == "regular" else 15
    elif category == "senior":
        # $10 for regular movies, $12 for premium movies
        return 10 if movie_type == "regular" else 12
    else:
        raise ValueError("Invalid input. Please enter your age: ")
    
# third function is the main function to actually get inputs and return outputs to console
def main():
    # get and validate age input
    age_input = input("Please enter your age: ")
    age = int(age_input)

    # get and validate movie type input
    movie_type = input("Please enter the movie type (regular or premium): ").lower()
    while movie_type not in ["regular", "premium"]:
        print("Invalid movie type. Please enter 'regular' or 'premium'.")
        movie_type = input("Please enter the movie type (regular or premium): ").lower()

    # calculate and display ticket price
    ticket_price = calculate_ticket_price(age, movie_type)
    print(f"\nYour ticket price is: ${ticket_price}")

# run the actual script
if __name__ == "__main__":
    main()

    # required test cases with expected outputs for autograder
    print("\nTest Case: 12 yrs old, regular ticket")
    print("Expected output for price for regular child's ticket,")
    print("Result: $" + str(calculate_ticket_price(12, "regular")))

    print("\nTest Case: 11 yrs old, premium ticket")
    print("Expected output for price for premium child's ticket")
    print("Result: $" + str(calculate_ticket_price(11, "premium")))

    print("\nTest Case: 13 yrs old, regular ticket")
    print("Expected output for regular adult ticket")
    print("Result: $" + str(calculate_ticket_price(13, "regular")))

    print("\nTest Case: 60 yrs old, regular ticket")
    print("Expected output for senior regular ticket")
    print("Result: $" + str(calculate_ticket_price(60, "regular")))

    print("\nTest Case: 59 yrs old, premium ticket")
    print("Expected output for senior premium ticket")
    print("Result: $" + str(calculate_ticket_price(59, "premium")))