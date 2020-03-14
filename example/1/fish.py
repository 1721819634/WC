import math
import numpy as np
from sympy import *

def calc_si(max_value,data):
    m=len(data)             # m是data的行数
    n=len(data[0])          # n是data的列数
    SI=np.zeros((m,n))      # 用于存放相应网格的SI
    for i in m:
        for j in n:
            SI[i][j]=data[i][j]/max_value
    return SI

def calc_nor_par(SI,data):
    miu=symbols('μ')
    sig=symbols('σ')
    Nor=np.zeros((m,n))      # 建立正态分布数组，用于求解方程组
    for i in m:
        for j in n:
           Nor[i][j]=SI[i][j]-math.exp((-(data[i][j]-miu)**2)/(2*sig**2))/sig*math.sqrt(2*math.pi)
    

