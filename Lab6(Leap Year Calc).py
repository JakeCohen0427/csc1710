#############################################################
#
#File name: Lab6.py
#Programmer: Jake Cohen
#Course: CSC1710
#Date Submitted: October 2, 2023 
#Location: /home/students/jcohen/csc1710/lab6/lab6.py
#Description: Calculates whether or not a user submitted year is a leap year or not
#Asisstance: None
#Compile and Execute: python3 lab6.py
#Additional Files: None
#
#############################################################


x = 0
currentYear = 2023
pastTensePos = " was a leap year"
presentTensePos = " is a leap year"
futureTensePos = " will be a leap year"
pastTenseNeg = " was not a leap year"
presentTenseNeg = " is not a leap year"
futureTenseNeg = " will not be a leap year"
tense = ""

while(x != 5):
    print("Enter year: ")
    year = int(input())
    yearP = str(year)
    
    
    if (year % 400 == 0) and (year % 100 == 0):
        #Leap year
        if(year == currentYear):
            print(yearP + presentTensePos)
        elif(year < currentYear):
            print(yearP + pastTensePos)
        else:
            print(yearP + futureTensePos)
    elif (year % 4 ==0) and (year % 100 != 0):
        if(year == currentYear):
            print(yearP + presentTensePos)
        elif(year < currentYear):
            print(yearP + pastTensePos)
        else:
            print(yearP + futureTensePos)

    else:
        if(year == currentYear):
            print(yearP + presentTenseNeg)
        elif(year < currentYear):
            print(yearP + pastTenseNeg)
        else:
            print(yearP + futureTenseNeg)
        
    x += 1
