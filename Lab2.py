#############################################################
#
#File name: Lab2.py
#Programmer: Jake Cohen
#Course: CSC1710
#Date Submitted: August 30, 2023
#Location: /home/students/jcohen/csc1710/lab2/lab2.py
#Description: Gets information on wage, hours worked, rent, and food cost
    #Then the program outputs the monthly budget information
#Asisstance: None
#Compile and Execute: Python3 lab2.py
#Additional Files: None
#
#############################################################

#Gets user input and converts it to float
print("*** Hello, I'm a Budget Planner Program ***")
print("How many hours do you work a week: ")
hoursPerWeek = input()
hoursPerWeek = float(hoursPerWeek)
print("What is your hourly wage: ")
hourlyWage = input()
hourlyWage = float(hourlyWage)
print("How much is your montly rent: ")
monthlyRent = input()
monthlyRent = float(monthlyRent)
print("How much do you spend on food per month: ")
monthlyFoodCost = input()
monthlyFoodCost = float(monthlyFoodCost)
#Calculate values
grossPay = hoursPerWeek * hourlyWage * 4
grossPay = float(grossPay)
netPay = grossPay - (grossPay * 0.2)
netPay = str(netPay)
spendingMoney = grossPay - monthlyRent - monthlyFoodCost
spendingMoney = str(spendingMoney)
grossPay = str(grossPay)
#prints
print("Your gross pay is: " + grossPay)
print("Your net pay for the month (after taxes and benefits) is: " + netPay)
print("After expenses, you have: " + spendingMoney)
