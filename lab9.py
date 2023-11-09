#############################################################
#
#File name: Lab9.py
#Programmer: Jake Cohen
#Course: CSC1710
#Date Submitted: November 12, 2023 
#Location: /home/students/jcohen/csc1710/lab9/lab9.py
#Description: Gets user input on a product name then its price, prints it as a table in three
#---different formats. As inputed, sorted alphebetically, and the sorted by price(low to high)
#Asisstance: None
#Compile and Execute: Python3 lab9.py
#Additional Files: None
#
#############################################################

x = True
prodName = []
prodPrice = []
while(x==True):
    print("What is the product name")
    name = input()
    if(name == "done"):
        x = False
        
    if(x != False):
        print("What is the product price")
        price = float(input())
    
        prodName.append(name)
        prodPrice.append(price)
def printer():
    count = 0
    length = len(prodName)
    print("")
    print("Product                Price")
    print("----------------------------")
    while(count != length):
        spacing = 27 - len(prodName[count])
        print(prodName[count] + f"{prodPrice[count]:{spacing}}")
        count += 1
        
def alphSort(prodName, prodPrice):
    n = len(prodName)
    for i in range(n):
        for j in range(0, n-i-1):
            if prodName[j] > prodName[j+1]:
                prodName[j], prodName[j+1] = prodName[j+1], prodName[j]
                prodPrice[j], prodPrice[j+1] = prodPrice[j+1], prodPrice[j]
    printer()

def numSort(prodName, prodPrice):
    n = len(prodPrice)
    for i in range(n):
        for j in range(0, n-i-1):
            if prodPrice[j] > prodPrice[j+1]:
                prodPrice[j], prodPrice[j+1] = prodPrice[j+1], prodPrice[j]
                prodName[j], prodName[j+1] = prodName[j+1], prodName[j]
    printer()
                
printer()    
alphSort(prodName, prodPrice)
numSort(prodName, prodPrice)        
