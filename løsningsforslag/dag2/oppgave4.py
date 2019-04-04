# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 15:00:50 2019

@author: Marie
"""

# Oppgave 4

from pylab import *

x = arange(-1, 1+0.05, 0.05)
y1 = exp(x)
y2 = exp(-x)

plot(x, y1, label='exp(x)')
plot(x, y2, label='exp(-x)')

xlim(-1, 1)
ylim(0, 3)
title('Noen eksponensialfunksjoner')
xlabel('x')
ylabel('y')
legend()

show()

