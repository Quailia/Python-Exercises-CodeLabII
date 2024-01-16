integer_list = [5, 2, 8, 1, 7, 3, 10, 4, 6, 9]

# Output the list using a for loop
print("Original list:")
for num in integer_list:
    print(num, end=" ")
print()  # Move to the next line

# Output the highest and lowest value
print(f"Highest value: {max(integer_list)}")
print(f"Lowest value: {min(integer_list)}")

# Sorting in descending order
integer_list.sort(reverse=True)
print("Sorted in descending order:", integer_list)

# Sorting in ascending order
integer_list.sort()
print("Sorted in ascending order:", integer_list)

# Appending two numbers
element1 = int(input("Enter first number to append: "))
element2 = int(input("Enter second number to append: "))
integer_list.append(element1)
integer_list.append(element2)

print(f"List after appending {element1} and {element2}:", integer_list)
