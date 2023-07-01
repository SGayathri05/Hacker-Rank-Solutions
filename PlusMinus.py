#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pos =0
    neg = 0
    zero = 0
    l = len(arr)
    for i in range(len(arr)):
        if arr[i]>0:
            pos+=1
        elif arr[i]<0:
            neg+=1
        elif arr[i]==0:
            zero+=1   
    print(pos/l)
    print(neg/l)
    print(zero/l)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
