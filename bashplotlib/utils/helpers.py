#!/usr/bin/evn python
# -*- coding: utf-8 -*-

"""
Various helpful function for bashplotlib
"""

import sys

isiterable = lambda x: hasattr(x, '__iter__') or hasattr(x, '__getitem__')

bcolours = {
    "white":   '\033[97m',
    "aqua":    '\033[96m',
    "pink":    '\033[95m',
    "blue":    '\033[94m',
    "yellow":  '\033[93m',
    "green":   '\033[92m',
    "red":     '\033[91m',
    "grey":    '\033[90m',
    "black":   '\033[30m',
    "default": '\033[39m',
    "ENDC":    '\033[39m',
}

colour_help = ', '.join([colour for colour in bcolours if colour != "ENDC"])


def get_colour(colour):
    """
    Get the escape code sequence for a colour
    """
    return bcolours.get(colour, bcolours['ENDC'])


def printcolour(text, sameline=False, colour=get_colour("ENDC")):
    """
    Print color text using escape codes
    """
    if sameline:
        sep = ''
    else:
        sep = '\n'
    sys.stdout.write(get_colour(colour) + text + bcolours["ENDC"] + sep)


def drange(start, stop, step=1.0, include_stop=False):
    """
    Generate between 2 numbers w/ optional step, optionally include upper bound
    """
    if step == 0:
        step = 0.01
    r = start

    if include_stop:
        yield r
        while r < stop:
            r += step
            r = round(r, 10)
            yield r
    else:
        while r < stop:
            yield r
            r += step
            r = round(r, 10)


def abbreviate(labels, rfill=' '):
    """
    Abbreviate labels without introducing ambiguities.
    """
    max_len = max(len(l) for l in labels)
    for i in range(1, max_len):
        abbrev = [l[:i].ljust(i, rfill) for l in labels]
        if len(abbrev) == len(set(abbrev)):
            break
    return abbrev


def box_text(text, width, separator = False, title_align = "c", offset=0):
    """
    Return text inside an ascii textbox
    
    Arguments help:
    text -- text to be placed in the box, can be single line or multiple line
    width -- width of the box
    separator -- option to separate the first line from the rest
    title_align -- c for centre, r for right, l for left
    offset -- how far the box would be offset from the left
    """
    #need to make sure that multi-line text is able to be processed
    #maybe accept the text in list form
    #if separator = True, separate the first line, can improve to choose which line to separate

    #to account for modification to the text box
    width -= 2

    if isinstance(text, list):
        title = text[0]
        content = text[1:]
    elif isinstance(text, str):
        title = text
        content = None
    if len(title) > width:
        title = title[:width-3] + "..."
    
    box = " " * offset + "+" + "-" * (width+2) + "+" + "\n"
    box += " " * offset + "|+" + "-" * (width) + "+|" + "\n"
    if title_align == "c":
        box += " " * offset + "||" + title.center(width) + "||" + "\n"
    elif title_align == "l":
        box += " " * offset + "||" + title.ljust(width) + "||" + "\n"
    elif title_align == "r":
        box += " " * offset + "||" + title.rjust(width) + "||" + "\n"
    if content != None:
        if separator:
            box += " " * offset + "||" + "-" * (width) + "||" + "\n"
        for i in content:
            box += " " * offset + "||" + i.center(width) + "||" + "\n"
    box += " " * offset + "|+" + "-" * (width) + "+|" + "\n"
    box += " " * offset + "+" + "-" * (width+2) + "+"
    return box
