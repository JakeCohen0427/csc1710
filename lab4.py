#############################################################
#
#File name: Lab4.py
#Programmer: Jake Cohen
#Course: CSC1710
#Date Submitted: August 25, 2023 
#Location: /home/students/jcohen/csc1710/lab4/lab4.py
#Description: This program asks the user to input dimensions and information
# -on paint then outputs how much paint you will need to paint the HPU logo on     
# -a flag and tells you the total cost of the paint
#Asisstance: None
#Compile and Execute: Python3 lab4.py
#Additional Files: None
#
#############################################################

print("Enter the height of the wall in feet: ")
wallHeight = float(input())
print("Enter the width of the wall in feet: ")
wallWidth = float(input())
print("Enter the radius of the circle in feet: ")
circleRad = float(input())
print("How much area can a gallon of paint cover in square feet: ")
galAreaCover = float(input())
print("What is the price per gallon of paint in USD: ")
pricePerGal = float(input())

circleArea = 3.14 * (circleRad * circleRad)
wallArea = wallHeight * wallWidth

goldArea = wallArea - circleArea
whiteArea = circleArea * 2
purpleArea = whiteArea * 0.15

goldPaint = goldArea / galAreaCover
whitePaint = whiteArea / galAreaCover
purplePaint = purpleArea / galAreaCover

goldCost = goldPaint * pricePerGal
whiteCost = whitePaint * pricePerGal
purpleCost = purplePaint * pricePerGal
totalCost = goldCost + whiteCost + purpleCost

print("Color      Gal   Cost")
print("---------------------")
print("Gold      " + str(round(goldPaint,1)) + "   " + str(round(goldCost,2)))
print("White     " + str(round(whitePaint,1)) + "   " + str(round(whiteCost,2)))
print("Purple    " + str(round(purplePaint,1)) + "   " + str(round(purpleCost,2)))
print("---------------------")
print("             Total:   " + str(round(totalCost,2)))