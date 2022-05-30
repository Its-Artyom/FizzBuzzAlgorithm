###
# This is a fizzbuzz algorithm that will print out:
# Multiples of 3 as Fizz, multiples of 5 as Buzz and multiples of 5 and 3 as FizzBuzz.
# Made by @its-artyom
# Algorithm originated in sometime by Imran Ghory.
###

list_input = int(input("How many numbers would you like to input into the algorithm: "))
for number in range(0, list_input + 1):
    if number == 3:
        print(str(number) + " is Fizz!")
    elif number == 5:
        print(str(number) + " is Buzz!")
    elif number == 15:
        print(str(number) + " is FizzBuzz!")
    else:
        print(number)