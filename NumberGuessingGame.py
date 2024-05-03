import math
import random

def main():
    lower = int(input("Enter Lower bound: "))
    upper = int(input("Enter Upper bound: "))

    x = random.randint(lower, upper)
    print("\n\tYou've only ",
            round(math.log(upper - lower + 1,2)),
            "chances to guess the integer! \n")

    count = 0

    while count < math.log(upper - lower + 1,2):
        count += 1
        guess = int(input("Guess a number: "))

        if x == guess:
            print("Congratulations you did it in ",
                count, " try")
            break
        elif x > guess:
            print("You guessed to small!")
        elif x < guess:
            print("You guessed too high!")

    if count >= math.log(upper - lower + 1,2):
        print("\nThe number is %d" % x)
        print("\tBetter Luck Next Time!")

def loop():
    again = "y"
    while again == "y":
        main()
        again = input("Enter 'y' to play again or 'n' to quit: ")

loop()