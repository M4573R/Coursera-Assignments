#Title: Python script for computing answer to Question 2 of Programming Assignment 1 (Intro to Recommender Systems)
#Author: Karan J. Thakkar
#Question: Advanced formula
#Output: Provides the top 5 movie ID's
#Usage: python ProgAss1Q2.py movie1 movie2 movie3

#Package for reading CSV file
from __future__ import division
import csv
import sys

#Global Variable
movieId = [sys.argv[1], sys.argv[2], sys.argv[3]]
fieldnames = ['userId', 'movieId', 'rating']
testMovieList = {}
newTemp = {}
userList = []
solution = {}

#open and read the CSV file and put it into a dictionary
data = csv.DictReader(open('data.csv', 'rU'), fieldnames=fieldnames, delimiter=',')
for line in data:
    
    #Holds the list of ALL users
    userList.append(line['userId'])
    
    #Parse all the data and put it in a dictionary with keys as
    #movie ID's and values as list of user ID's who rated the movie
    if line['movieId'] not in newTemp:
        newTemp[line['movieId']] = [line['userId']]
    else:
        newTemp[line['movieId']].append(line['userId'])
            
#Find out the user ID's who have rated the movies we want 
for movie in movieId:
    testMovieList[movie] = newTemp[movie]

#Iterate the loop for the 3 movie ID's
for i in range(0,3):
    #Holds the final result string to be displayed
    a = movieId[i] + ""
    
    #Find how many intersecting user ID's are there for each of the movies and then compute the ratio
    for movie, allusers in newTemp.items():
        numerator = len(list(set(testMovieList[movieId[i]]) & set(newTemp[movie])))/len(testMovieList[movieId[i]])
        denominator = len(list(set(newTemp[movie]) & set(list(set(userList) ^ set(testMovieList[movieId[i]])))))/len(list(set(userList) ^ set(testMovieList[movieId[i]])))
        solution[movie] = numerator/denominator if denominator != 0 else 0 #This last condition avoid the target movie being on top of the recommeended list
    
    #Sorted version of the solution
    sortedDict = sorted(solution.items(), key=lambda k: k[1], reverse = True)
    
    #Generate the final output string
    j = 0
    for key, value in sortedDict:
        #Print only top 5 movieID's and their scores AND avoid being receommended the target movie itself
        if j < 5 and key not in movieId:
            a += "," + str(key) + "," + str(float("%.2f" % round(solution[key], 2)))
        j += 1
    
    print a