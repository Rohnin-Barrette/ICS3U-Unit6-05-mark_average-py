#!/usr/bin/env python3

# Created by: Mr. Coxall
# Created on: Dec 2019
# This program uses a list


def average_finder(marks):
    # this function finds the average all the elements in  a 2D array

    total = 0

    for single_element in marks:
        total += single_element

    average = total / len(marks)

    return average


def main():
    # this function uses a list

    marks = []
    temp_int = None

    # input
    print("Please enter 1 mark at a time. Enter -1 to end.")

    while True:
        try:
            temp_number = input("What is your mark (as %): ")
            temp_int = int(temp_number)
            if temp_int <= 100 and temp_int >= 0:
                marks.append(temp_int)
            elif temp_int == -1:
                average = average_finder(marks)
                print("The average is {0}%".format(average))
                break
            else:
                print("Invalid input.")
                continue
            temp_int = int(temp_number)
            marks.append(temp_int)
        except Exception:
            print("Invalid Input")
            continue


if __name__ == "__main__":
    main()
