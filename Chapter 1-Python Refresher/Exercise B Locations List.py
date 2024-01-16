locations = ["Dubai", "paris", "switzerland", "London", "Amsterdam", "New York"]

# List and length
print("Original list:", locations)
print("Length of the list:", len(locations))

# Using sorted, this will order uppercase words first before lowercase ones, and wont change the original order
print("List in alphabetical order:", sorted(locations))

# List is still original
print("Original list after sorted():", locations)

# Reverse
print("List in reverse alphabetical order:", sorted(locations, reverse=True))

# List is original
print("Original list after sorted() with reverse=True:", locations)

# Reversing and altering the original order and showing it
locations.reverse()
print("List after reverse():", locations)

# Sorting in alphabetical, case sensitive order, then prenting, to show change
locations.sort()
print("List after sort():", locations)

# Same as the above, except reversed
locations.sort(reverse=True)
print("List after sort() with reverse=True:", locations)
