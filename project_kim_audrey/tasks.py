# Audrey Kim, amkim@usc.edu
# ITP 115, Spring 2022
# Section: 32096
# Final Project
# tasks.py
# Description:
# This file defines functions that will be used in another Python file.
# The functions defined are: readParksFile, convertDate, and getLargestPark

# defining the readParksFile function
def readParksFile(fileName="national_parks.csv"):
    fin = open(fileName, "r") # opening the csv file to read it
    header_line = fin.readline()
    header_line = header_line.strip() # getting rid of whitespace in the header line
    header = header_line.split(",") # splitting by commas in header line

    parkList = [] # defining empty list - will be a list of dictionaries, where each park is represented by a dictionary

    # loop for going through each line of the file
    for line in fin:
        line = line.strip() # getting rid of whitespace in each line
        newLine = line.split(",") # splitting by commas in each line
        parkDict = {} # empty dictionary for each park (which is each line)

        # loop for assigning keys and values for each park dictionary
        for item in range(len(header)):
            key = header[item] # assigning key
            value = newLine[item] # assigning value
            if item == len(header) - 1:
                newLineList = newLine[item:]
                value = ",".join(newLineList) # joining if there are commas in description
            parkDict[key] = value # assigning the value to each key
        parkList.append(parkDict) # adding each park dictionary to the list

    fin.close()  # closing the file

    return parkList

# defining the convertDate function
def convertDate(dataStr):

    # getting the year, day, and month from user input
    year = dataStr[0:4]
    day = dataStr[8:]
    month = int(dataStr[5:7])

    # enmpty strings for name of month and for whole date
    monthName = ""
    wholeString = ""

    # list of all months
    monthList = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    monthName = monthList[month-1] # converting the number of month to the name (string) of month

    wholeString = monthName + " " + day + ", " + year # defining the whole date to be returned

    return wholeString

# defining getLargestPark function
def getLargestPark(parksList):

    maxNumAcres = 0 # initializing the maximum number of acres
    code = "" # empty string for code to be returned later

    # going through each line of parksList and comparing value of acres of each park
    for line in parksList:
        numAcres = int(line["Acres"])
        if numAcres > maxNumAcres:
            maxNumAcres = numAcres # setting maxNumAcres to new max
            code = line["Code"] # getting the code of the park with largest number of acres

    return code

