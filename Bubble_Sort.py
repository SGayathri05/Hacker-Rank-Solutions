#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if a[i]>a[j]:
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
                count+=1
    print(f"Array is sorted in {count} swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[-1])
