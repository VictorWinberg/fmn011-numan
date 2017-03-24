# -*- coding: utf-8 -

import numpy as np
import matplotlib.pyplot as plt
import math

x = np.linspace(-4, 4, num=1000)
dx = x[1] - x[0]

def fixedPoint(f, x_i):
    for n in range(0, 1000):
        try:
            x_i = f(x_i)
        except:
            print("None")
            return
    print(x_i)
    print(f(x_i))

def f1(x):
    return np.cos(x)

def f2(x):
    return np.cos(x)**2

def df(f):
    return np.gradient(f(x), dx)

plt.plot(x, x, 'k--', label='x')
plt.plot(x, f1(x), label='f1')
plt.plot(x, f2(x), label='f2')
plt.legend(loc='upper left')

plt.figure()

plt.plot(x, np.ones(x.size), 'k--', label='+-1')
plt.plot(x, -np.ones(x.size), 'k--')
plt.plot(x, df(f1), label='df1')
plt.plot(x, df(f2), label='df2')
plt.legend(loc='upper left')

plt.draw()

print(" --- f1 --- ")
fixedPoint(f1, 0)

print(" --- f2 --- ")
fixedPoint(f2, 0)

plt.show()
