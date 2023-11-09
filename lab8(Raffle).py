#############################################################
#
#File name: Lab8(Raffle).py
#Programmer: Jake Cohen
#Course: CSC1710
#Date Submitted: October 29, 2023 
#Location: /home/students/jcohen/csc1710/lab8/lab8(Raffle).py
#Description: Creates a list of names from user input chooses a winner and outputs the winners and profit
#Asisstance: None
#Compile and Execute: Python3 lab8.py
#Additional Files: None
#
#############################################################

import random



#puts all the names into a list
listOfNames = []
x = True
amtOfNames = 0
while(x == True):
    print("Enter name: ")
    name = input()
    if(name == "done"):
        x = False
    else:
        listOfNames.append(name)
        amtOfNames += 1
        
#function for picking a name
def pickAName():
    x = random.randint(0,amtOfNames)
    return listOfNames[x]
    
#picks name and checks if it is a repeat
firstPlace = pickAName()
secondPlace = pickAName()
thirdPlace = pickAName()

z = True
while(z == True):
    if(firstPlace == secondPlace):
        secondPlace = pickAName()
    if(secondPlace == thirdPlace):
        thirdPlace == pickAName()
        
    if(firstPlace != secondPlace and secondPlace != thirdPlace):
        z = False

#prints answers
print("First prize winner is " + firstPlace)
print("Second prize winner is " + secondPlace)
print("Third prize winner is " + thirdPlace)
print("We sold " + str(amtOfNames) + " tickets")
amtOfMoneyMade = amtOfNames * 5
print("We collected $" + str(amtOfMoneyMade))
profit = amtOfMoneyMade - 175
print("Our profit was $" + str(profit))
    
    
