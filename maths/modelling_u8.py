# -*- coding: utf-8 -*-
from __future__ import division
from math import pi, sqrt
import numpy as np
import matplotlib.pyplot as plt

import plotly.plotly as py
import plotly.graph_objs as go
py.sign_in('', '')


# Mathematical model for emptying a bath
g = 9.81

# Assumptions: bath is a rectangular vessel whose base
# has area A and whose depth is h (in metres)
w = 0.75
l = 1.5
A = w * l
h = 0.5

# Plug hole area
S = pi * 0.05**2

# Initially the bath is completely full so that y(t) represents
# the depth of the water at time t after the plug is removed, then
# y(0) = h.
# Need to determine the variation of y with t, the time t_h such
# that y(t_h) = 0 (how long the bath takes to empty), and t_h/2 such
# that y(t_h/2) = h / 2 (time taken for the first half to empty).

# v(t) - speed of water leaving the bath through the plug hole
# V(t) - volume of water left in the bath at time t
# S * v(t) * 𝛿t - amount of water leaving the plug hole
k = (S / A) * sqrt(2 * g)


def v(t):
    return sqrt(2 * g * y(t))


def y(t):
    return (sqrt(h) - ((k*t)/2))**2


def t_h():
    return (2 * sqrt(h)) / k


def t_h_2():
    return (sqrt(2 * h)) / k


def draw_graph(t, y):
    plt.plot(t, y)
    plt.xlabel("time (t)")
    plt.ylabel("height (y)")
    plt.title("Change of height as bath empties")
    plt.grid(True)
    plt.savefig("bath.png")


def generate_plotly(t, ys, image_name, title):
    data = []
    annotations = []
    for label, y in ys:
        trace = go.Scatter(
            x=t,
            y=y,
            mode="lines",
            line=dict(color="rgba(67,67,67,1)"),
            name=label
        )
        data.append(trace)
    data.append(
        go.Scatter(
            x=[0, 13.25],
            y=[0.25, 0.25],
            mode="lines",
            line=dict(color="rgba(67,67,67,1)", dash=5, width=1)
        )
    )
    data.append(
        go.Scatter(
            x=[13.25, 13.25],
            y=[0, 0.25],
            mode="lines",
            line=dict(color="rgba(67,67,67,1)", dash=5, width=1)
        )
    )
    layout = dict(
        title=title,
        xaxis=dict(title="time (t)"),
        yaxis=dict(title="height (h)")
    )
    annotations.append(dict(
        xref='paper',
        x=-0.05, y=0.25,
        xanchor='left', yanchor='middle',
        text="h/2",
        font=dict(
            size=14,
            color="rgba(14,0,179,1)"
        ),
        showarrow=False,))
    annotations.append(dict(
        xref='paper',
        x=0.27, y=-0.02,
        xanchor='left', yanchor='middle',
        text="t_h/2",
        font=dict(
            size=14,
            color="rgba(14,0,179,1)"
        ),
        showarrow=False,))
    layout['annotations'] = annotations
    py.image.save_as({'data': data, 'layout': layout}, image_name)
    print 'Saved {}'.format(image_name)


if __name__ == '__main__':
    ys, ts = [], []
    for t in np.arange(0, 60, 0.25):
        yt = y(t)
        ys.append(yt)
        ts.append(t)
        if 1e-5 > yt >= -1e-5:
            break
        # print "Time: {}, y: {}".format(t, yt)

    print "Time the bath takes to empty is {}".format(t_h())
    print "Time the bath takes to half empty is {}".format(t_h_2())

    y_plot = [('Water depth', ys)]

    # Generate plot for the whole duration of bath emptying
    generate_plotly(
        ts,
        y_plot,
        'bath_full_to_empty.png',
        "Change of height as bath empties"
    )

    # # Generate plot for first half vs second half
    # generate_plotly(
    #     ts,
    #     y_plots,
    #     'bath_first_vs_second_half.png',
    #     "first half vs second half"
    # )

    # draw_graph(ts, ys)
