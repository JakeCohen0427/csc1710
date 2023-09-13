#############################################################
#
#File name: Lab3.py
#Programmer: Jake Cohen
#Course: CSC1710
#Date Submitted: September 13, 2023 
#Location: /home/students/jcohen/csc1710/lab3/lab3.py
#Description: Asks the user for a six digit number then creates a checksum for it
#Asisstance: None
#Compile and Execute: Python3 lab3.py
#Additional Files: None
#
#############################################################

for x in range(3):
    print("Enter a six digit number: ")
    sDN = input()
    d1 = int(sDN[0])
    d2 = int(sDN[1])
    d3 = int(sDN[2])
    d4 = int(sDN[3])
    d5 = int(sDN[4])
    d6 = int(sDN[5])
    
    firstPair = d1 + d2
    firstPairRight = firstPair % 10
    secondPair = d3 + d4
    secondPairRight = secondPair % 10
    lastPair = d5 + d6
    lastPairRight = lastPair % 10
    
    checkSumPre = firstPairRight + secondPairRight + lastPairRight
    checkSumFin = checkSumPre % 10
    
    print(checkSumFin)