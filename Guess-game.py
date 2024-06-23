import random

correctGuess = random.randint(1,10)

GameOn = True
guessUsed = 0

while guessUsed < 5:
    playerGuess = int (input("Enter a number from 1 to 10: "))
    guessUsed = guessUsed + 1

    if playerGuess == correctGuess:
        print("Congrates")
        GameOn = False

    elif playerGuess > correctGuess:
        print("sorry your guess is high ")
        

    elif playerGuess < correctGuess:
        print("sorry your guess is low ")            
if playerGuess!= correctGuess and guessUsed == 5:
    print("Start over!!!!")

