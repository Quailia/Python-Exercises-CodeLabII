num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

sum_result = num1 + num2
diff_result = num1 - num2
product_result = num1 * num2

# Checks if the second number is not zero before performing division and modulus
if num2 != 0:
    quotient_result = num1 / num2
    remainder_result = num1 % num2
else:
    quotient_result = "Undefined (division by zero)"
    remainder_result = "Undefined (division by zero)"

print(f"Sum: {sum_result}")
print(f"Difference: {diff_result}")
print(f"Product: {product_result}")
print(f"Quotient: {quotient_result}")
print(f"Remainder: {remainder_result}")
