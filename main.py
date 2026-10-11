#rock paper scissors
#idk guys I'm just learning python
#this definitely isn't anything advanced

import random
winTracker = 0
lossTracker = 0
tieTracker = 0
gameNum = random.randint(0,2)
gameRoll = ""

def display_stats():
    print("Wins:"+ str(winTracker))
    print("Losses:" + str(lossTracker))
    print("Ties:" + str(tieTracker))

def play_again():
    playAgain = input("Do you want to play again? (y/n): ")
    if playAgain.lower() == "y":
        play_game()
    else:
        print("Thanks for playing!")
        display_stats()

def play_game():
    gameNum = random.randint(0,2)
    global lossTracker
    global winTracker
    global tieTracker
    userInput = input("enter rock(r), paper(p), or scissors(s):")
    if gameNum == 0:
        gameRoll = "r"
    elif gameNum == 1:
        gameRoll = "p"
    elif gameNum == 2:
        gameRoll = "s"
    if gameNum == userInput:
        tieTracker += 1
        print("It's a tie!")
        play_again()
    elif (userInput == "r" and gameRoll == "s") or (userInput == "p" and gameRoll == "r") or (userInput == "s" and gameRoll == "p"):
        winTracker += 1
        print("You win!")
        display_stats()
        play_again()
    else:
        lossTracker += 1
        print("You lose!")
        display_stats()
        play_again()

play_game()