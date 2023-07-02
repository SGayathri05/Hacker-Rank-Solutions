#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    hours = int(s[:2])
    minutes = int(s[3:5])
    seconds = int(s[6:8])
    
    # Checking if the time is in AM or PM
    if s[-2:] == "PM":
        # If the time is in the afternoon or evening, add 12 to the hours
        if hours != 12:
            hours += 12
    else:
        # If the time is in the morning, and the hours is 12, reset it to 0
        if hours == 12:
            hours = 0
    
    # Formatting the time in 24-hour format
    formatted_time = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    
    return formatted_time

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
