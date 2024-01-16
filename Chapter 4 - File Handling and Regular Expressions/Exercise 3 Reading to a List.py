# Opens the file and reads it
with open("resources\\numbers.txt", "r") as file:
    lines = file.readlines()

# Converts each line to an integer and store in a list
numbers = [int(line.strip()) for line in lines]

print(numbers)
