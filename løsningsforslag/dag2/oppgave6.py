#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Oppgave 6

#vi bruker funksjonene fra kanonkule.py (Oppgave 3)

from pylab import arange,plot,show #imprterer det vi trenger fra pylab

def kanonkule_x(t):
    return 25*t


def kanonkule_y(t):
    return 45*t - 5*t**2


def kanonkule_posisjon(t):
    x = kanonkule_x(t)
    y = kanonkule_y(t)
    return x,y

#a)
t = arange(0,9.1,0.1)

#b)
x_pos, y_pos = kanonkule_posisjon(t) #får to arrays med x og y posisjoner

#c)
plot(x_pos,y_pos) #plott banen

#d)
treff_x, treff_y = kanonkule_posisjon(8) #finn treffpunktet ved 8 sek
plot(treff_x,treff_y,'ro') #plott punktet, 'ro' for å få et rødt punkt

show()
