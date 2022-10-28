#!/usr/bin/env python3

# Created by: Joanne Santhosh
# Created on: Oct 2022
# This program uses a compound boolean statement


def main():
    # this function uses a compound boolean statement

    # input
    age = int(input("Enter your age: "))
    print("")

    # process & output
    if age >= 25 or age <= 50:
        print("You passed the course.")
    else:
        print("You did not pass the course.")


if __name__ == "__main__":
    main()