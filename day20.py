# Day 20 - Sorting

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    swaps = 0
    for i in range(0,n-1):
        for i in range(0,n-1):
            if a[i]>a[i+1]:
                a[i],a[i+1] = a[i+1],a[i]
                swaps +=1
    print(f"Array is sorted in {swaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")




