username = input("Enter username: ")
password = input("Enter password: ")

if username == "Soulnim" and password == "Luqm@n2004":
    print("Welcome "+ username + "\nYou are good to go!")
    print("--------\nMain Menu\n--------\n(a) Profile\n(b) Notes\n(c) Expenses")
elif username == "Soulnim" and password != "Luqm@n2004":
    print("Invalid passwords")
elif username != "Soulnim" and password == "Luqm@n2004":
    print("Invalid username")
else:
    print("Invalid username and password")

from classes import userProfile
from classes import noteLists
from classes import expensesLists

Profile = userProfile("Luqman Hanis Daniel bin Khailmi", "Soulnim", "18", "Computer Science")
if username == "Soulnim" and password == "Luqm@n2004":
    userInput = input("Please input: ")
    if userInput == "a":
        print("Name: "+Profile.name+"\nUsername: "+Profile.userName+"\nAge: "+Profile.age+"\nMajor: "+Profile.major)
    elif userInput == "b":
        print(noteLists)
    elif userInput == "c":
        print(expensesLists)
    else:
        print("Invalid input")