import random

def jumbler():
    words = ("python", "jumble", "easy", "difficult", "answer", "xylophone",
         "dexter", "christmas")
    word = random.choice(words)
    correct = word
    return(correct, word)

jumble = ""
again = 'y'
while again.lower() == "y":
    correct, word = jumbler()
    while word:
        position = random.randrange(len(word))
        jumble += word[position]
        word = word[:position] + word[position+1:]

    print("******** Welcome to Jumble Word ********")
    print("\nUnscramble the word to win")
    print("The jumbe is ",jumble)
    guess = input("\nYour guess: ")
    while guess != correct and guess !="":
        print("\nSorry, that's not it\nPress enter to stop guessing\n")
        guess = input("Your guess :")
    if guess == correct:
        print("That's correct!\n")

    again = input('Would you like to play again? (y/n)\n >>> ')
    print()
    jumble = ''
print("Thanks for playing!")