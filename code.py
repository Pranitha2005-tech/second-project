# Function to subtract three numbers
def subtract_numbers(num1, num2 , num3):
    return num1 - num2 - num3

# Input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform subtraction
result = subtract_numbers(num1, num2)

# Display the result
print(f"The result of {num1} - {num2} is: {result}")
