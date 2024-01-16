# Pre-set
def calculate_product(input_list):
    product = 1
    for value in input_list:
        product *= value
    return product

numbers = [2, 3, 4, 5]
result = calculate_product(numbers)

print(f"The product of the list {numbers} is: {result}")

# ==========================================================

""" User-set
def calculate_product(input_list):
    product = 1
    for value in input_list:
        product *= value
    return product

# User input
user_input = input("Enter a list of numbers separated by spaces: ")
numbers = [int(num) for num in user_input.split()]

# Check
if not numbers:
    print("No numbers entered. Exiting.")
else:
    result = calculate_product(numbers)
    print(f"The product of the list {numbers} is: {result}") """
