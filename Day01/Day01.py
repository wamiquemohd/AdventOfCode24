#!/bin/python3

#==================================================================================================================================================
# name:             Day01.py
# Desciprtion:      AOC Day 01 refer Problem Statement
# Dependencies:     -
# Author:           Husain Samani, Mohammad Wamique (TT-S6)
#==========================================================================================

def main():
    locID_1 = []
    locID_2 = []

    retval = getSeperateList(locID_1, locID_2)
    if retval:
        locID_1.sort() #Sort the list of Integers
        locID_2.sort()
        FinalSum = getSumOfDifferences(locID_1, locID_2)
        FinalSimilarity = getSumOfSimilarity(locID_1,locID_2)
    else:
        print("Error with opening file")
        return False
    
    print("Final Sum of Diff", FinalSum)
    print("Final Similarity",FinalSimilarity)
    return True


def getSeperateList(locID_1, locID_2):
    retVal = False
    try:
        with open('Day01Input.txt', 'r') as f:
            for line in f:
                loc_1, loc_2 = line.strip().split()
                locID_1.append(int(loc_1))
                locID_2.append(int(loc_2))
                retVal = True
    except FileNotFoundError:
        return retVal
    
    return retVal

def getSumOfDifferences(locID_1,locID_2):
    sum = 0
    if len(locID_1) != 0 and len(locID_2) !=0:
        for element in range(len(locID_1)):
            sum += abs(locID_1[element] - locID_2[element])
            
#    print("Final sum is", sum)
    return sum

def getSumOfSimilarity(locID_1, locID_2):
    sum = 0
    if len(locID_1) != 0 and len(locID_2) !=0:
        for element in range(len(locID_1)):
            sum += locID_1[element] * locID_2.count(locID_1[element])
        
#    print("Sum of Similarity is: ",sum)
    return sum


if __name__ == '__main__':
    main()