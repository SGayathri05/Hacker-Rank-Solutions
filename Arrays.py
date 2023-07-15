#HACKERRANK 30 DAYS OF CODE - ARRAYS

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    r = arr[::-1]
    print(' '.join(str(x) for x in r))
