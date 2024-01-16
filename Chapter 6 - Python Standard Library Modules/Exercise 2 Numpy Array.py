import numpy as np

# The array
a = np.array([20, 23, 82, 40, 32, 15, 67, 52])

# Even numbers
even_indices = np.where(a % 2 == 0)[0]  # Indices of even numbers
even_indices_list = even_indices.tolist()  # Convert numpy array to list
print(f"indices of even numbers are {even_indices_list}")  # Print indices

# Sorted
sorted_a = np.sort(a)
print(f"sorted array is {sorted_a}")

# From 3 to end
sliced_a = a[3:]
print(f"sliced array from index 3 to thhe end is {sliced_a}")

# From start to 4
sliced_a = a[:4]
print(f"sliced array from index 0 to index 4 is {sliced_a}")

# Negatively sliced array
negative_sliced_a = a[-4:-1]
print(f"array [32, 15, 67] using negative slicing is {negative_sliced_a}")
