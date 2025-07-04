import math

# Ask the user for a number as input
number = int(input("Enter a number: "))

# Perform calculations using the math module
if number > 0:
    square_root = math.sqrt(number)
    natural_log = math.log(number)
    sine_value = math.sin(number)

    # Display the results
    print(f"Square root: {square_root}")
    print(f"Logarithm: {natural_log}")
    print(f"Sine: {sine_value}")
else:
    print("Please enter a positive number for these calculations.")
