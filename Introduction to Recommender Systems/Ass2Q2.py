#Title: Python script for computing answer to Question 2 of Written Assignment 2 (Intro to Recommender Systems)
#Author: Karan J. Thakkar
#Question: Calculate the percentage of ratings for each movie that are 4 or higher. Order with the highest percentage first, and submit the top 5.
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
    
    #variable which stores the total users who rated that movie >= 4
    plusFourCount = [0]*temp
    
    #variable which stores the total users who rated that movie
    plusFourTotal = [0]*temp
    
                        #Iterate to populate the plusFourCount and plusFourTotal variables
    for rowIndex, list in enumerate(newData):
        for columnIndex, x in enumerate(list):
            if rowIndex > 0 and columnIndex > 0 :
                if x:
                    plusFourCount[columnIndex] += 1 if int(x) >= 4 else 0
                    plusFourTotal[columnIndex] += 1
    
    #Calculate the percentage of ratings >=4 for each movie
    for index, tempList in enumerate(plusFourCount):
        if plusFourTotal[index] is not 0:
            plusFourCount[index] = "%.2f" % round(float(plusFourCount[index]) * 100 /plusFourTotal[index], 2)
    
    #Create a dictionary with movie names and the percentages
    newDict = {}
    for mean, name in zip(plusFourCount, newData[0]): 
        newDict[float(mean)] = name
    
    #Sort the dictionary based on the mean rating
    sortedDict = sorted(newDict.items(), key=lambda t: t[0], reverse = True)
    for i in range(0, 5):
        print sortedDict[i][1]