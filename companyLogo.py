#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter



if __name__ == '__main__':
    for each in Counter(sorted(input())).most_common(3):
        print(*each)
