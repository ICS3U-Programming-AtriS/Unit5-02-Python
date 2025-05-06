#!/usr/bin/env python3
# Created By: Atri Sarker
# Date: May 6, 2025
# Program that calculates and displays
# the area of a triangle,
# with user-provided dimensions


# Function that calculates and displays the area of a triangle,
# given base and length
def calc_area(base: float, height: float) -> float:
    # Calculate area
    area = base * height * (0.5)
    # Display area [\u00b2 is the unicode sequence for superscript 2]
    print(f"The area of the triangle is {area:.2f}cm\u00b2")


def main():
    # Initialize variables for base and height
    base = 0
    height = 0
    # Get base input as string
    base_string = input("Enter the base of the triangle (cm): ")
    # [ I am sorry for using a nested try-catch ]
    try:
        # Convert the user's input to a float
        base = float(base_string)
        # Get height input as string
        height_string = input("Enter the base of the triangle (cm): ")
        try:
            # Convert the user's input to a float
            height = float(height_string)
            # Check if height and base are positive
            if (base > 0) and (height > 0):
                # CALL calc_area()
                calc_area(base, height)
            else:
                # Tell the user that the dimensions must be positive
                print(f"Base and Height must be greater than 0.")
        except ValueError:
            # Tell the user that their input wasn't a number
            print(f"{height_string} is not a valid number.")
        pass
    except ValueError:
        # Tell the user that their input wasn't a number
        print(f"{base_string} is not a valid number.")


if __name__ == "__main__":
    main()
