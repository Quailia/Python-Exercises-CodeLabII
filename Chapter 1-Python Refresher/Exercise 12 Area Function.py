# Function to calculate the area of a square
def calculate_square_area():
    side_length = float(input("Enter the side length of the square: "))
    area = side_length ** 2
    print(f"The area of the square is: {area}")

# Calculate the area of a circle
def calculate_circle_area():
    radius = float(input("Enter the radius of the circle: "))
    area = 3.14 * radius ** 2
    print(f"The area of the circle is: {area}")

# Calculate the area of a triangle
def calculate_triangle_area():
    base = float(input("Enter the base length of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print(f"The area of the triangle is: {area}")

# Menu
while True:
    print("\nMenu:")
    print("1: Calculate the area of a square")
    print("2: Calculate the area of a circle")
    print("3: Calculate the area of a triangle")
    print("0: Exit")

    # User choice
    choice = input("Enter your choice (0-3): ")

    # Chosen operation
    if choice == '1':
        calculate_square_area()
    elif choice == '2':
        calculate_circle_area()
    elif choice == '3':
        calculate_triangle_area()
    elif choice == '0':
        print("Terminating program...")
        break
    else:
        print("Invalid choice. Please enter a number between 0 and 3.")
