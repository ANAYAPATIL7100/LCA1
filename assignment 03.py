def is_right_triangle(side1, side2, side3):
    # Sort the sides to identify the hypotenuse
    sides = sorted([side1, side2, side3])
    # Check if the triangle is a right triangle using the Pythagorean theorem
    return sides[0]**2 + sides[1]**2 == sides[2]**2   
def main():
    # Get user input for the sides of the triangle
    side1 = float(input("Enter the length of the first side: "))
    side2 = float(input("Enter the length of the second side: "))
    side3 = float(input("Enter the length of the third side: "))

    # Check if the triangle is a right triangle
    if is_right_triangle(side1, side2, side3):
        print("The triangle is a right triangle.")
    else:
        print("The triangle is not a right triangle.")
if __name__ == "__main__":
    main()                  