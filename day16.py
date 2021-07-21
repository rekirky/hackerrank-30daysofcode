# Day 16 - Exceptions - String to Integer

#!/bin/python3

import math
import os
import random
import re
import sys

S = input()

try:
    int(S)
    print(S)
except:
    print("Bad String")

