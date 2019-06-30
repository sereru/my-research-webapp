import math
import numpy as np
import matplotlib.pyplot as plt

def logistic(x,y):
    x = x/12
    y = y/31
    for i in range(10):
        y = x*y*(1-y)
    return y

def julia(X, Y, m, d):
    for i in range(100):
        X, Y = X**2 - Y**2 + m , 2 * X * Y + d
    return X**2+Y**2 <16