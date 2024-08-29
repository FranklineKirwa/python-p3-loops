#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    count=10
    while count > 0:
        print(count)
        count -=1
    print("Happy New Year!")
def square_integers(int_list):
    # code goes here!
    return[numbers **2 for numbers in int_list]

def fizzbuzz():
    # code goes here!
    for numbers in range (1, 101):
        if numbers % 3 == 0 and numbers % 5 == 0:
            print("FizzBuzz")
        elif numbers % 3 == 0:
            print("Fizz")
        elif numbers % 5 == 0:
            print("Buzz")
        else:
            print(numbers)

