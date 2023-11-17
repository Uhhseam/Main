import random
words = ("python", "jumble", "easy", "difficult", "answer", "xylophone",
         "dexter", "christmas")
word = random.choice(words)
correct = word
jumble = ""

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[position+1:]

print("******** Welcome to Jumble Word ********")
print("\nUnscramble the word to win")
print("The jumbe is ",jumble)
guess = input("\nYour guess: ")
while guess != correct and guess !="":
    print("Sorry, that's not it")
    guess = input("Your guess :")
print("Thanks for playing")

input("\n\nPress enter key to exit")