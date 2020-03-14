import numpy as np
from sympy import *
from numpy import random
'''
this file is used to test wc. Here is the parameters 
chars: 407
words: 75
code_lines: 11
space_lines: 1
comment_lines: 10
total_lines: 22
'''

sst = random.randint(10, 30, size=(10, 10))
s = sst.ravel()
long = len(s)
mean = sum(s) / long
std = np.sqrt(sum((s - mean) ** 2 / long))
print(np.pi)
print(math.sqrt(4))
print(std)
# print(net)
