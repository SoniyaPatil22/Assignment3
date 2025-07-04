def factorial(n):
    """Calculate the factorial of a number using a loop."""
    if n < 0:
        return "Factorial does not exist for negative numbers."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Call the function with a sample number
sample_number = int(input("Enter a number: "))
output = factorial(sample_number)

# Print the result
print(f"The factorial of {sample_number} is: {output}")
