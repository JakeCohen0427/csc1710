#############################################################
#
#File name: Lab11.py
#Programmer: Jake Cohen
#Course: CSC1710
#Date Submitted: October 2, 2023 
#Location: /home/students/jcohen/csc1710/lab11/lab11.py
#Description: Creates a "database" of movies along with the year they came out, their rating, and the director. Has a delete function. Has a search function.
    #Has a add function. Has a view function. Has a quit function.
#Asisstance: None
#Compile and Execute: Python3 lab11.py
#Additional Files: None
#
#############################################################

textName = 'lab11TXT.txt'

def viewTable():
    print("Title                         Year     Rating      Director")
    print("--------------------------------------------------------------------")
    fhand = open(textName, 'r')
    for line in fhand:
        line = line.rstrip()
        x = line.split('`')
        print(f"{x[0]:{30}}" + f"{x[1]:{9}}" + f"{x[2]:{12}}" + x[3])
    fhand.close()



conditionLoop = True
while(conditionLoop == True):
    print("(v)iew movies\n(a)dd a movie\n(d)elete a movie\n(s)earch for a movie\n(q)uit")
    option = input()
    if(option == 'q'):
        conditionLoop = False
    elif(option == 'a'):
        print("Title, Year, Rating, Director (seperate using \"`\")")
        TYRD = input()
        fhand = open(textName, 'a')
        fhand.write(TYRD)
        fhand.write("\n")
        fhand.close()
    elif(option == 'v'):
        viewTable()
    elif(option == 'd'):
        viewTable()
        print("Enter title you want to be deleted: ")
        deleteteableTitle = input()
        with open(textName, "r") as f: 
            data = f.readlines() 
        with open(textName, "w") as f: 
            for line in data : 
                x = line.split('`')
                if x[0].find(deleteteableTitle) == -1:  
                    f.write(line)
    elif(option == 's'):
        print("What would you like to search for?: ")
        searchParam = input()
        print("Title                         Year     Rating      Director")
        print("--------------------------------------------------------------------")
        fhand = open(textName, 'r')
        for line in fhand:
            x = line.split('`')
            searchFunc = x[0].find(searchParam)
            if(searchFunc != -1):
                line = line.rstrip()
                x = line.split('`')
                print(f"{x[0]:{30}}" + f"{x[1]:{9}}" + f"{x[2]:{12}}" + x[3])
        fhand.close()