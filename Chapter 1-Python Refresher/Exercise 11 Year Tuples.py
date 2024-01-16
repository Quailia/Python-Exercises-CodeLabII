# Tuple
year = (2017, 2003, 2011, 2005, 1987, 2009, 2020, 2018, 2009)

# Access -3
value_at_minus_3 = year[-3]
print(f"Value at index -3: {value_at_minus_3}")

# Reverse
reversed_year = tuple(reversed(year))
print(f"Original tuple: {year}")
print(f"Reversed tuple: {reversed_year}")

# Count 2009
count_2009 = year.count(2009)
print(f"Number of times 2009 is in the tuple: {count_2009}")

# Get index
index_2018 = year.index(2018)
print(f"Index value of 2018: {index_2018}")

# Find length
tuple_length = len(year)
print(f"Length of the tuple: {tuple_length}")
