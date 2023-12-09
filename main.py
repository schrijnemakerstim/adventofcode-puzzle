#Script for completing adventofcode puzzles

import numpy as np
import re as expr

#Open the file and read the data into the variable
input_data = open(".\input_data_puzzle_1.txt", "r")
numbers_sumation = 0 #need to start with zero numbers


#Read 1 line strip the last enter characters from it
for line in input_data.readlines():
    #Try to find the first and last number
    try: 
        found_numbers = expr.findall(r'\d', line)
    except:
        print("something wrong with this input:" + str(line))
    
    #Convert both numbers to strings and put them next to each other
    word_sum = str(found_numbers[0]) + str(found_numbers[-1])
    numbers_sumation += float(word_sum)

print("The sum of the first numbers and last numbers of a string are: " + str(int(numbers_sumation)))