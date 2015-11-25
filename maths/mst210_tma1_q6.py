import numpy as np
from math import sin, cos


rads = np.arange(0, np.pi, 1e-5)
g = 9.81
u = 3
mu = 5/12.
x = 0.75

low = x - 1e-5
high = x + 1e-5

for rad in rads:
    dist = (u**2 / (2*g*(sin(rad) + mu*cos(rad))))
    if low < dist < high:
        print 'Rad: {}, x: {}'.format(rad, dist)
