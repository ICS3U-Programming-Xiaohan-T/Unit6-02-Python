#!/usr/bin/env python3
# Created by: Xiaohan
# Created on: May 26, 2025
# This program finds the maximum value of 10 random numbers in a range and prints it
import random


# define a function
def max_value(numbers):
    # Set a range for the arrays
    for num in range(10):
        # Initialize max_value to the first element of the list
        max_value = 0
        # Check if the current number is greater than max_value
        if numbers[num] > max_value:
            # Return the current number as max_value
            return max_value


def main():
    # Generate 10 random numbers and find the maximum value
    numbers = []
    # For counter in the range of 10
    for counter in range(10):
        # Generate a random number between 1 and 100
        random_number = random.randint(1, 100)
        # Append the random number to the list
        numbers.append(random_number)
        # Print the random numbers
    print("The random numbers are:", numbers)
    # Call the max_value(numbers) function
    max_value = max(numbers)
    # Print the maximum value
    print("The maximum value is:", max_value)


if __name__ == "__main__":
    main()
