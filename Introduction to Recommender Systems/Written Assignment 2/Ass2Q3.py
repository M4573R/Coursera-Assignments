#Title: Python script for computing answer to Question 3 of Written Assignment 2 (Intro to Recommender Systems)
#Author: Karan J. Thakkar
#Question: Count the number of ratings for each movie, order with the most number of ratings first, and submit the top 5.
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
    
    #variable which stores the total users who rated that movie
    totalRatingCount = [0]*temp
    
    #Iterate to populate the totalRatingCount variable
    for rowIndex, list in enumerate(newData):
        for columnIndex, x in enumerate(list):
            if rowIndex > 0 and columnIndex > 0 :
                if x:
                    totalRatingCount[columnIndex] += 1
    
    #Create a dictionary with movie names and the percentages
    newDict = {}
    for mean, name in zip(totalRatingCount, newData[0]): 
        newDict[mean] = name
    
    #Sort the dictionary based on the mean rating
    sortedDict = sorted(newDict.items(), key=lambda t: t[0], reverse = True)
    for i in range(0, 5):
        print sortedDict[i][1]