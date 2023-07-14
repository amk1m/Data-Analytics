# Audrey Kim, amkim@usc.edu
# ITP 115, Spring 2022
# Section: 32096
# Final Project
# interface.py
# Description:
# This file creates functions that are to be used by other Python files.
# The functions defined in this file are getMenuDict, displayMenu, getUserChoice, printAllParks, getStateAbbr, printParksInState,
# printLargestPark, printParksForSearch

# importing the tasks.py so the functions can be called
import tasks

# defining the getMenuDict function
def getMenuDict():
    # creating dictionary that has all the choices
    menuDict = {"A":"All national parks", "B":"Parks in a particular state", "C":"The largest park", "D":"Search for a park", "Q":"Quit"}

    return menuDict

# defining the displayMenu function
def displayMenu(menuDict):
    print()
    # printing out the menu by looping through the menu dictionary
    for item in menuDict:
        print(item + " -> " + menuDict[item])

# defining the getUserChoice function
def getUserChoice(menuDict):
    # getting user input for menu choice
    userChoice = "z" # initializing userChoice variable (for do-while loop)
    while userChoice not in "ABCDQ":
        userChoice = input("Choice: ").upper() # asking user input if they do not enter a valid option
    return userChoice

# defining printAllParks function
def printAllParks(parksList):
    # looping through each line of parksList and printing out the information of each park
    for line in parksList:
        print(line["Name"] + " (" + line["Code"] + ")")
        print("\tLocation: " + line["State"])
        print("\tArea: " + line["Acres"] + " acres")
        print("\tDate Established: " + tasks.convertDate(line["Date"]))

# defining getStateAbbr function
def getStateAbbr():
    # getting user input
    userInput = input("Enter a state: ")

    # checking if user input is valid; if not, keep asking the user to enter a state
    while len(userInput) != 2 or (userInput.isalpha() == False):
        print("Need the two letter abbreviation")
        userInput = input("Enter a state: ")

    return userInput.upper()

# defining the printParksInState function
def printParksInState(parksList):
    state = getStateAbbr() # calling the getStateAbbr to get state from user
    num = 0 # number for checking if there is a such park that exists or not in the state the user inputted

    # looping through each line in parksList and printing out information if the park is in the user state
    for line in parksList:
        if state in line["State"]:
            print(line["Name"] + " (" + line["Code"] + ")")
            print("\tLocation: " + line["State"])
            print("\tArea: " + line["Acres"] + " acres")
            print("\tDate Established: " + tasks.convertDate(line["Date"]))
            num = 1

    if num == 0: # if there are no national parks in the user state
        print("There are no national parks in", state, "or it is not a valid state.")

# defining the printLargestPark function
def printLargestPark(parksList):
    # calling tasks.getLargestPark function to get park code
    code = tasks.getLargestPark(parksList)

    # looping through parksList to find the park with the code of largest park
    for line in parksList:
        if line["Code"] == code: # printing out information of largest park
            print(line["Name"] + " (" + line["Code"] + ")")
            print("\tLocation: " + line["State"])
            print("\tArea: " + line["Acres"] + " acres")
            print("\tDate Established: " + tasks.convertDate(line["Date"]))
            print("\tDescription: " + line["Description"])

# defining printParksForSearch function
def printParksForSearch(parksList):
    # getting input from user for search text
    userInput = input("Enter text for searching: ")

    # converting user inputted text to lower, title, and upper
    wordLower = userInput.lower()
    wordTitle = userInput.title()
    wordUpper = userInput.upper()

    num = 0 # number for checking if the search text exists in any of the parks

    # looping through each park in parksList
    for line in parksList:

        # checking if lowercase user word is in any park's code, name or description
        if wordLower in line["Code"] or wordLower in line["Name"] or wordLower in line["Description"]:
            print(line["Name"] + " (" + line["Code"] + ")")
            print("\tLocation: " + line["State"])
            print("\tArea: " + line["Acres"] + " acres")
            print("\tDate Established: " + tasks.convertDate(line["Date"]))
            print("\tDescription: " + line["Description"])
            print()
            num = 1

        # checking if title user word is in any park's code, name or description
        elif wordTitle in line["Code"] or wordLower in line["Name"] or wordLower in line["Description"]:
            print(line["Name"] + " (" + line["Code"] + ")")
            print("\tLocation: " + line["State"])
            print("\tArea: " + line["Acres"] + " acres")
            print("\tDate Established: " + tasks.convertDate(line["Date"]))
            print("\tDescription: " + line["Description"])
            print()
            num = 1

        # checking if uppercase user word is in any park's code, name or description
        elif wordUpper in line["Code"] or wordLower in line["Name"] or wordLower in line["Description"]:
            print(line["Name"] + " (" + line["Code"] + ")")
            print("\tLocation: " + line["State"])
            print("\tArea: " + line["Acres"] + " acres")
            print("\tDate Established: " + tasks.convertDate(line["Date"]))
            print("\tDescription: " + line["Description"])
            print()
            num = 1

    if num == 0: # if the search text doesn't exist in any park
        print("There are no national parks for the search text of \'" + userInput + "\'.")




