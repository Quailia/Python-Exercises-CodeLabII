side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))


if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
    print("These side lengths form a valid triangle.")
else:
    print("These side lengths do not form a valid triangle.")
