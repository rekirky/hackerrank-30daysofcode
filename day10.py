# Day 10 - Binary Numbers

#!/bin/python3

import math
import os
import random
import re
import sys

def counter(range):
    count = 0
    longest = 0
    for i in range:
        if int(i) == 1 and count <= longest:
            count +=1
            if count > longest:
                longest = count
        else:
            count = 0
    return longest
            

if __name__ == '__main__':
    n = int(input().strip())
    range = bin(n)[2:]
    longest = counter(range)
    print(longest)
    
