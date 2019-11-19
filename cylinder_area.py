#!/usr/bin/env python3

# Created by: Ben Lapuhapo
# Created on: Nov 2019
# This program claculates the area of a cylinder

import math


def calculate_area(radius, height):
    # calculate area

    # process
    area = 2 * math.pi * radius * height + 2 * math.pi * radius**2

    # output
    print("Area is {:.2f} cm²".format(area))


def main():
    # this function gets radius and height
    while True:
        # input
        radius_user_input = input("Enter the Radius of The Cylinder (cm): ")
        height_user_input = input("Enter the Height of The Cylinder(cm): ")
        print("")

        # process
        try:
            radius_from_user_int = int(radius_user_input)
            height_from_user_int = int(height_user_input)
            print("You Entered A Number Correctly")
            # call functions
            calculate_area(radius_from_user_int, height_from_user_int)

        # Prevents the program from crashing
        except ValueError:
            print("Not An Integer")
            continue

        else:
            break


if __name__ == "__main__":
    main()
