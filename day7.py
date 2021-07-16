# Day 7 - Arrays

#!/bin/python3

import math
import os
import random
import re
import sys

def reverse(arr):
    word=""
    for i in range (len(arr)-1,-1,-1):
        word += str(arr[i])
        word += " "
    print(word)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    reverse(arr)
        
