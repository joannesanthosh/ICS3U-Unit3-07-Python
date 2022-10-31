#!/usr/bin/env python3

# Created by: Joanne Santhosh
# Created on: Oct 2022
# This program uses a compound boolean statement


def main():
    # this function uses a compound boolean statement

    # input
    user_age_as_string = input("Enter your age: ")
    print("")

    # process & output
    try:
        user_age_as_number = int(user_age_as_string)
        if user_age_as_number >= 25 and user_age_as_number <= 40:
            print("You are eligible to date my grand-daughter.")
        else:
            print("You are not eligible to date my grand-daughter.")
    except ValueError:
        print("{0} is not an integer".format(user_age_as_string))
    finally:
        print("Done.")


if __name__ == "__main__":
    main()
