#!/usr/bin/env python3

# Created by: Huzaifa Khalid
# Created on: April 2022
# This program is the final version of the guessing game


import random


def main():
    # This program is the final version of the guessing game

    # input
    random_number = random.randint(0, 9)
    counter = 0

    # process and output
    while True:
        user_guess_as_string = input("Enter a random number between 0-9(integer): ")
        print("")

        try:
            user_guess_as_integer = int(user_guess_as_string)
            counter = counter + 1
            if user_guess_as_integer == random_number:
                print(
                    "Hooray, you guessed correctly :), and it only took you {0} tries:)".format(
                        counter
                    )
                )
                break
            elif user_guess_as_integer > random_number:
                print("The number is too high enter a lower number.")
            else:
                print("The number is too low, enter a higher number.")

        except Exception:
            print(
                "{0} is invalid input, enter a number you numbskull.".format(
                    user_guess_as_string
                )
            )
        finally:
            print("\nDone.")


if __name__ == "__main__":
    main()
