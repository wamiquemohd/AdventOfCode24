#!/bin/python3

#==================================================================================================================================================
# name:             Day03.py
# Desciprtion:      AOC Day 03 refer Problem Statement
# Dependencies:     -
# Author:           Husain Samani, Mohammad Wamique (TT-S6)
#==========================================================================================
import re

def main(filepath):
    instruction_list = readDataFromFile(filepath)
    all_muls = getallMuls(instruction_list)
    sum_of_muls = getSumOfMuls(all_muls)
    all_muls_with_condition = getCondallMuls(instruction_list)

    print("Sum of Mults: ", sum_of_muls)
    print("Sum of all Mults with condition", all_muls_with_condition)
    return True

def readDataFromFile(filepath):
    list_val= []
    instr_list = []
    str_list = ""
    try:
        with open(filepath, 'r') as f:
            list_val = [line.strip() for line in f]
            instr_list.append(list_val)
            str_list  = "".join(instr_list[0])
#            print(str_list)
    except FileNotFoundError:
        print("Error opening File")

    return str_list 

def multi(a, b):
    return a*b

def getCondallMuls(instruction_list):
    sum = 0
    index_dont = 0
    index_do = 0
    pattern_1 = r"mul\(\d{1,3},\d{1,3}\)"
    pattern_2 = r"don\'t\(\)"
    pattern_3 = r"do\(\)"

    index_of_dont= re.search(pattern_2, instruction_list).start()
    index_of_do = re.search(pattern_3, instruction_list).start()

#    print("index of dont",index_of_dont)
#    print("index of do",index_of_do)

    # To get Muls from start till first don#t()
    match_1 = re.findall(pattern_1, instruction_list[:index_of_dont])
#    print(match_1)
    sum_1 = getSumOfMuls(match_1)

    # for find sum of Mults in between do and donts
    for dos in re.finditer(pattern_3, instruction_list):
        index_do = dos.start()
        if index_do < index_dont:
            continue
       # for donts in re.finditer(pattern_2, instruction_list):
        for donts in re.finditer(pattern_2, instruction_list):
            index_dont = donts.start()
            if index_do > index_dont:
                continue
            else:
#                print("index_dont, j",j,index_dont)
                match_do_dont = re.findall(pattern_1, instruction_list[index_do:index_dont])
                sum_1 = sum_1 + getSumOfMuls(match_do_dont)

                break
    return sum_1


def getallMuls(instruction_list):
    match = []
    final_list = []
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    match = re.findall(pattern, instruction_list)
    final_list.extend(match)
    return final_list

def getSumOfMuls(all_muls):
    sum = 0
    pattern = r"\((\d+),(\d+)\)"
    for item in all_muls:
        val = re.findall(pattern, item)
        for i in val:
            number1 = int(i[0])
            number2 = int(i[1])
            sum = sum + multi(number1, number2)
    return sum

if __name__ == '__main__':
    main('Day03Input.txt')