#Title: Python script for computing answer to Question 1 of Written Assignment 2 (Intro to Recommender Systems)
#Author: Karan J. Thakkar
#Question: Calculate the mean rating for each movie, order with the highest rating listed first, and submit the top 5.
#Output: Provides the top 5 movie names. You have to strip the MovieID from it and submit the solution

#Package for reading CSV file
import csv

#Variable for storing the CSV file data in the form of lists
newData = []
temp = 0

#open and read the CSV file
with open('data.csv', 'rU') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    for row in data:
        newData.append(row)
        temp = len(row)
    
    #variable which stores the total ratings for that movie
    meanList = [0]*temp
    
    #variable which stores the total users who rated that movie
    meanCount = [0]*temp
    
    #Iterate to populate the meanList and meanCount variables
    for rowIndex, list in enumerate(newData):
        for columnIndex, x in enumerate(list):
            if rowIndex > 0 and columnIndex > 0 and x:
                meanList[columnIndex] += int(x)
                meanCount[columnIndex] += 1
                
    #Calculate the mean rating for each movie
    for index, tempList in enumerate(meanList):
        if meanCount[index] is not 0:
            meanList[index] = "%.2f" % round(float(meanList[index])/meanCount[index], 2)
    
    #Create a dictionary with movie names and the mean rating
    newDict = {}
    for mean, name in zip(meanList, newData[0]): 
        newDict[float(mean)] = name
    
    #Sort the dictionary based on the mean rating
    sortedDict = sorted(newDict.items(), key=lambda t: t[0], reverse = True)
    for i in range(0, 5):
        print sortedDict[i][1]