# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 15:11:00 2019

@author: Marie
"""

# Oppgave 5
from pylab import *

## a)
def f(x):
    return sin(x**2)

## b)
def g(x):
    return x**2 + x/5 - exp(-x)


## c)
x = arange(0, 1.7 + 0.05, 0.05)
y1 = f(x)
plot(x, y1)

## d)
y2 = g(x)
plot(x, y2)

## e)
x = 1

## f)
plot(1, g(1), 'ro')


