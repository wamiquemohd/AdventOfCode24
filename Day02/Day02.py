#!/bin/python3

#==================================================================================================================================================
# name:             Day02.py
# Desciprtion:      AOC Day 02 refer Problem Statement
# Dependencies:     -
# Author:           Husain Samani, Mohammad Wamique (TT-S6)
#==========================================================================================

def main(filepath):
    report_list = readDataFromFile(filepath)
    safe_report = getNumberOfSafeReports(report_list)
    safe_report_without_damper = getNumberOfSafeReportsWithoutDamper(report_list)
    print("Safe reports are: ", safe_report)
    print("Safe reports w\o Damper: ", safe_report_without_damper)
    return True

def readDataFromFile(filepath):
    list_val= []
    report_list = []
    try:
        with open(filepath, 'r') as f:
            list_val = [list(map(int, line.strip().split(' '))) for line in f]
            report_list.append(list_val)
    except FileNotFoundError:
        print("Error opening File")

    return report_list 

def getNumberOfSafeReports(report_list):
    sum = 0
    for sub_report in report_list:
        for report in sub_report:
            sum = sum + checkForSafeReport(report)
#    print("Sum:", sum)
    return sum

def getNumberOfSafeReportsWithoutDamper(report_list):
    sum = 0
    for sub_report in report_list:
        for report in sub_report:
            if checkForSafeReport(report):
                sum +=1
            else:
                for i in range(len(report)):
                    new_report = report[:i] + report[i+1:]
                    if checkForSafeReport(new_report):
                        sum +=1
                        break
#    print("Final Sum",sum)
    return sum

def checkForSafeReport(report):
    flag = False
    print("rep:", report)
    for element in range(len(report) - 1):
        if ((report == sorted(report) or report == sorted(report, reverse=True)) and 
                (abs(report[element] - report[element+1]) >=1 and abs(report[element] - report[element+1]) <= 3)):
            flag = True
            print("rep:", report)
        else:
            flag = False
            break

    return flag
        

if __name__ == '__main__':
    main('Day02Input.txt')