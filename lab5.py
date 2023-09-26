#############################################################
#
#File name: Lab5.py
#Programmer: Jake Cohen
#Course: CSC1710
#Date Submitted: August 26, 2023 
#Location: /home/students/jcohen/csc1710/lab5/lab5.py
#Description: This program will take the number of sales an employee at a paper company made and will
#   - output the bonus pay for that amount of sales, as well as calculates the employees paycheck
#Asisstance: None
#Compile and Execute: Python3 lab5.py
#Additional Files: None
#
#############################################################

print("How many sales did you make this month? :")
salesAmt = float(input())
bonus = 0
basepay = salesAmt
federalTax = 0.15
print(F"Your base pay is ${salesAmt:.2f}")
if(salesAmt < 2000):
    bonus = 0
    print("You get a 0% bonus")
if(salesAmt >= 2000 and salesAmt <= 3999):
    bonus = 0.06
    print("You get a 6% bonus")
if(salesAmt >= 4000 and salesAmt <= 4999):
    bonus = 0.08
    print("You get a 8% bonus")
if(salesAmt >= 5000):
    bonus = 0.1
    print("You get a 10% bonus")
    
bonusPay = salesAmt * bonus
print(F"Your bonus pay is ${bonusPay:.2f}")

grossPay = salesAmt + bonusPay
print(F"Your gross pay is ${grossPay:.2f}")

taxedMoney = grossPay * federalTax
print(F"Your federal income tax is ${taxedMoney:.2f}")

netPay = grossPay - taxedMoney
print(F"Your paycheck is ${netPay:.2f}")