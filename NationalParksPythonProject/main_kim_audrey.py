# Audrey Kim, amkim@usc.edu
# ITP 115, Spring 2022
# Section: 32096
# Final Project
# main_kim_audrey.py
# Description:
# This file calls various functions from the tasks and interface Python files.
# The user is able to get information from the national_parks csv file using the different menu options.

import tasks
import interface

def main():

    print("National Parks")

    parksList = tasks.readParksFile() # getting parksList by calling readParksFile function in tasks

    menuDict = interface.getMenuDict() # getting menuDict by calling getMenuDict in interface

    userChoice = ""
    while userChoice.upper() != "Q":
        interface.displayMenu(menuDict)
        userChoice = interface.getUserChoice(menuDict) # getting userChoice by calling the interface function
        # branching statements for each menu option
        if userChoice.upper() == "A":
            interface.printAllParks(parksList)
        elif userChoice.upper() == "B":
            interface.printParksInState(parksList)
        elif userChoice.upper() == "C":
            interface.printLargestPark(parksList)
        elif userChoice.upper() == "D":
            interface.printParksForSearch(parksList)
        elif userChoice.upper() == "Q":
            print("")
        else:
            userChoice = interface.getUserChoice(menuDict)

main()