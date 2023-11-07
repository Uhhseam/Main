import random
points = 0

dict = {"name":input("Enter your name: "),"title":input("Enter your title: ")}
print("\nHello",dict['title'],dict['name'])
#constants
words = ("overused","calm","guam","end of semester","prom","homework")
hangman = (
    """     
     -------
    |       |
    |       |
    |       O
    |       
    |      
    |      
    |      
    |      
    |      
    |
    |
    |
    ---------""",
    """     
     -------
    |       |
    |       |
    |       O
    |       
    |      
    |      
    |      
    |      
    |      
    |
    |
    |
    ---------""",
    """     
     -------
    |       |
    |       |
    |       O
    |   ----+----
    |      
    |      
    |      
    |      
    |      
    |
    |
    |
    ---------""",
    """     
     -------
    |       |
    |       |
    |       O
    |  /----+----\\
    |       |
    |       |
    |      
    |      
    |      
    |
    |
    |
    ---------""",
    """     
     -------
    |       |
    |       |
    |       O
    |  /----+----\\
    |       |
    |       |
    |      | |
    |      | |
    |      | |
    |
    |
    |
    ---------""",
    """     
     -------
    |       |
    |       |
    |       O
    | //----+----\\\\
    |       |
    |       |
    |      | |
    |      | |
    |      | |
    |
    |
    |
    ---------""")


goOn = 'y'
pts = 0
while goOn.lower() != 'n':

    word = random.choice(words)
    maxWrong = len(hangman) -1
    soFar = '_' * len(word)
    used = []

    print("Welcome to Hangman. Best of luck, Human")
    wrong = 0
    numTries = 0
    while wrong < maxWrong and soFar != word:
        print(soFar)
        #print(word)
        guess = input("\nEnter your guess: ")
        numTries += 1
        guess = guess.lower()
        used.append(guess)
        if guess in word:
            print("\nYes!",guess,"is in the word!")
            new = ""
            for i in range(len(word)):
                if guess == word[i]:
                    new += guess
                else:
                    new += soFar[i]
            soFar = new
            print(soFar)
            print("\nUsed:",used)
        else:
            print("Guess not in word")
            print("\nUsed:",used)
            print("\n",hangman[wrong])
            wrong += 1
            print("You have ",wrong,'/6 mistakes remaning.')


        if wrong == maxWrong:
            print(hangman[wrong])
            print("You've been hanged!")
            print("Word was",word)
        else:
            trial = input("Would you like to guess the word? (y/n): ")
        if trial.lower() == "y":
            answer = input("Guess is: ")
            if answer.lower() == word:
                pts += 30
                print("\nCongratulations! you guessed the word in", 
                    str(numTries),"tries. \nYou have earned 30 points.",
                    "Here is your total points",pts)
                break
            else:
                print("Incorrect guess...")
                wrong += 1
                print("You have ",wrong,'/ 6 mistakes remaning.')

    goOn = input("Would you like to play again? (y/n): ")
input("\nPress any key to exit\n")
