import numpy as np
from math import sin, cos


rads = np.arange(0, np.pi, 1e-5)
g = 9.81
u = 3
mu = 5/12.

x = 0.75

low = 0.75 - 1e-5
high = 0.75 + 1e-5

for rad in rads:
    right_hand_side = (u**2 / (2*g*(sin(rad) + mu*cos(rad))))
    if low < right_hand_side < high:
        print(rad, right_hand_side)
