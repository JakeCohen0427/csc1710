#############################################################
#
#File name: Lab7.py
#Programmer: Jake Cohen
#Course: CSC1710
#Date Submitted: October 18, 2023 
#Location: /home/students/jcohen/csc1710/lab6/lab6.py
#Description: Plays a dice game
#Asisstance: None
#Compile and Execute: Python3 lab7.py
#Additional Files: None
#
#############################################################
import random






def diceGameOneDie():
    x = True
    gameWins = 0
    gameLosses = 0
    gamePlays = 0
    gameTies = 0

    while(x == True):
        print("Would you like to play Dice? y/n:")
        playD = input()
        if(playD == "y"):
            gamePlays += 1
            d1 = random.randint(1,6)
            d2 = random.randint(1,6)
            print("")
            print("You rolled a " + str(d1) + " and I rolled a " + str(d2))
            if(d1 > d2):
                print("You won!!")
                gameWins += 1
            elif(d1 < d2):
                print("I won!")
                gameLosses +=1
            elif(d1 == d2):
                print("Aww it's a tie")
                gameTies += 1
            
            print("")
            print("Wins: " + str(gameWins))
            print("Losses: " + str(gameLosses))
            print("Ties: " + str(gameTies))
            print("Games: " + str(gamePlays))
            print("")
        elif(playD == "n"):
            print("Hope you had fun!")
            print("Your final score was " + str(gameWins) + " wins, " + str(gameLosses) + " losses, and " + str(gameTies) + " ties")
            print("")
            x = False
        else:
            print("Please only type \"y\" or \"n\"")
def diceGameTwoDie():
    x = True
    gameWins = 0
    gameLosses = 0
    gamePlays = 0
    gameTies = 0

    while(x == True):
        print("Would you like to play Dice? y/n:")
        playD = input()
        if(playD == "y"):
            gamePlays += 1
            doubleRoll = False
            d1P = random.randint(1,6)
            d2P = random.randint(1,6)
            d1C = random.randint(1,6)
            d2C = random.randint(1,6)
            print("")
            print("You rolled a " + str(d1P) + " and " + str(d2P))
            print("I rolled a " + str(d1C) + " and " + str(d2C))
            
            #Checks winner if doubles
            if(d1P == d2P):
                doubleRoll = True
                if(d1C == d2C):
                    if(d1P > d1C):
                        print("You won!!")
                        gameWins += 1
                    elif(d1P < d1C):
                        print("I won!")
                        gameLosses += 1
                    else:
                        print("It's a tie!")
                        gameTies += 1
                else:
                    print("You won!")
                    gameWins += 1
            elif(d1C == d2C):
                doubleRoll = True
                print("I won!")
                gameLosses += 1
                
            #Checks winner if no doubles
            pHigh = 0
            pLow = 0
            cHigh = 0
            cLow = 0
            
            if(doubleRoll == False):
                if(d1P > d2P):
                    pHigh = d1P
                    pLow = d2P
                else:
                    pHigh = d2P
                    pLow = d1P
                    
                if(d1C > d2C):
                    cHigh = d1C
                    cLow = d2C
                else:
                    cHigh = d2C
                    cLow = d1C
                    
                if(pHigh > cHigh):
                    print("You won!")
                    gameWins += 1
                elif(pHigh < cHigh):
                    print("I won!!")
                    gameLosses += 1
                elif(pHigh == cHigh):
                    if(pLow > cLow):
                        print("You won!")
                        gameWins += 1
                    elif(pLow < cLow):
                        print("I won!")
                        gameLosses += 1
                    elif(pLow == cLow):
                        print("It's a tie!")
                        gameTies += 1
                    else:
                        print("Error")
            
            print("")
            print("Wins: " + str(gameWins))
            print("Losses: " + str(gameLosses))
            print("Ties: " + str(gameTies))
            print("Games: " + str(gamePlays))
            print("")
        elif(playD == "n"):
            print("Hope you had fun!")
            print("Your final score was " + str(gameWins) + " wins, " + str(gameLosses) + " losses, and " + str(gameTies) + " ties")
            print("")
            x = False
        else:
            print("Please only type \"y\" or \"n\"")
            
            
            
            
            
print("")
print("------------------------")
print("Welcome to my dice game!")
print("------------------------")
print("")
print("The rules for one die are:")
print("     • Highest roll wins")
print("     • If both rolls are the same it is a tie")
print("")
print("The rules for two die are:")
print("     • Doubles always beats singles")
print("     • If both rolls are doubles, the higher value wins (two 5's beats two 4's)")
print("     • If both rolls are singles, the highest number wins (6 and 1 beats 5 and 4)")
print("     • If all die are the same number it is a tie")
print("")
print("Would you like to play with one die or two?: ")
oOrT = input()
if(oOrT == "1" or oOrT == "one" or oOrT == "One"):
    diceGameOneDie()
elif(oOrT == "2" or oOrT == "two" or oOrT == "Two"):
    diceGameTwoDie()
