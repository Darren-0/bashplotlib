#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Plotting terminal based scatterplots
"""

from __future__ import print_function
import csv
import sys
import optparse
from .utils.helpers import *
from .utils.commandhelp import scatter


def get_scale(series, is_y=False, steps=20):
    min_val = min(series)
    max_val = max(series)
    scaled_series = []
    for x in drange(min_val, max_val, (max_val - min_val) / steps,
                    include_stop=True):
        if x > 0 and scaled_series and max(scaled_series) < 0:
            scaled_series.append(0.0)
        scaled_series.append(x)

    if is_y:
        scaled_series.reverse()
    return scaled_series


def _plot_scatter(xs, ys, size, pch, colour, title, cs, xs_title, ys_title):
    graph = ""
    plotted = set()
    axis_x, axis_y, point_0, axis_x_count = False, False, False, True
    if min(xs) < 0 and max(xs) > 0: 
        axis_y = True
    if min(ys) < 0 and max(ys) > 0:
        axis_x = True
    if axis_y == True and axis_x == True:
        point_0 =True
    #print title box
    if title:
        graph += f'{box_text(title, 2 * (len(get_scale(xs, False, size)) + 1))}\n'

    if ys_title != None and isinstance(ys_title, str):
        graph += f'y: {ys_title}\n'
    graph += "-" * (2 * (len(get_scale(xs, False, size)) + 2)) + '\n'
    for y in get_scale(ys, True, size):
        graph += "| "
        axis_y_count = True
        for x in get_scale(xs, False, size):
            point = " "
            #generate the x-axis(i.e. there are positive and negative y points)
            if axis_x and y < 0 and axis_x_count:
                point = "-"
                if axis_y and x > 0 and axis_y_count:
                    point = "0"
                    axis_y_count = False
            #generate the y-axis(i.e there are positive and negative x points)
            elif axis_y and x > 0 and axis_y_count:
                point = "|"
                axis_y_count = False
            for (i, (xp, yp)) in enumerate(zip(xs, ys)):
                if xp <= x and yp >= y and (xp, yp) not in plotted:
                    point = pch
                    plotted.add((xp, yp))
                    if cs:
                        colour = cs[i]
            graph += point + " "
        graph += " |\n"
        if y < 0:
            axis_x_count = False
    graph += ("-" * (2 * (len(get_scale(xs, False, size)) + 2))) + '\n'
    if xs_title != None and isinstance(xs_title, str):
        graph += (" " * (2 * (len(get_scale(xs, False, size)) + 2) - len(xs_title) - 3) 
        + "x: " + xs_title) + '\n'
    return graph


def plot_scatter(f, xs, ys, size, pch, colour, title, xs_title = None, ys_title = None):
    """
    Form a complex number.

    Arguments:
        f -- comma delimited file w/ x,y coordinates
        xs -- if f not specified this is a file w/ x coordinates
        ys -- if f not specified this is a file w/ y coordinates
        size -- size of the plot
        pch -- shape of the points (any character)
        colour -- colour of the points
        title -- title of the plot
    """
    cs = None
    if f:
        if isinstance(f, str):
            with open(f) as fh:
                data = [tuple(line.strip().split(',')) for line in fh]
        else:
            data = [tuple(line.strip().split(',')) for line in f]
        xs = [float(i[0]) for i in data]
        ys = [float(i[1]) for i in data]
        if len(data[0]) > 2:
            cs = [i[2].strip() for i in data]
    elif isinstance(xs, list) and isinstance(ys, list):
        pass
    else:
        with open(xs) as fh:
            xs = [float(str(row).strip()) for row in fh]
        with open(ys) as fh:
            ys = [float(str(row).strip()) for row in fh]

    graph = _plot_scatter(xs, ys, size, pch, colour, title, cs, xs_title, ys_title)
    #if point == "|" or point == "-" or point == "0":
        #printcolour(point + " ", True, "default")
    #else:
        # printcolour(point + " ", True, colour)
    print(graph)
    

# need to add option to add axis title in this
def main():

    parser = optparse.OptionParser(usage=scatter['usage'])

    parser.add_option('-f', '--file', help='a csv w/ x and y coordinates', default=None, dest='f')
    parser.add_option('-t', '--title', help='title for the chart', default="", dest='t')
    parser.add_option('-x', help='x coordinates', default=None, dest='x')
    parser.add_option('-y', help='y coordinates', default=None, dest='y')
    parser.add_option('-s', '--size', help='y coordinates', default=20, dest='size', type='int')
    parser.add_option('-p', '--pch', help='shape of point', default="x", dest='pch')
    parser.add_option('-c', '--colour', help='colour of the plot (%s)' %
                      colour_help, default='default', dest='colour')

    opts, args = parser.parse_args()

    if opts.f is None and (opts.x is None or opts.y is None):
        opts.f = sys.stdin.readlines()

    if opts.f or (opts.x and opts.y):
        plot_scatter(opts.f, opts.x, opts.y, opts.size, opts.pch, opts.colour, opts.t)
    else:
        print("nothing to plot!")


if __name__ == "__main__":
    main()
