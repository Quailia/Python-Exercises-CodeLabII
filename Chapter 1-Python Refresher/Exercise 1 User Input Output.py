name = input("What is your name?\n")
age = int(input("What is your age?\n"))

print(f"Hello, {name.title()}!")

name_length = len(name)
print(f"The length of your name is: {name_length}")

age_next_year = age + 1
print(f"You will be {age_next_year} in a year.")
