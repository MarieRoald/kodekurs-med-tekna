#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Oppgave 3

#a)
def kanonkule_x(t):
    return 25*t

#b)
def kanonkule_y(t):
    return 45*t - 5*t**2

#c)
def kanonkule_posisjon(t):
    x = kanonkule_x(t)
    y = kanonkule_y(t)
    return x,y

#d/e)
tid = float(input("Skriv inn antall sekunder etter avfyrt skudd: "))
x,y = kanonkule_posisjon(tid)
print(f"lengde: {x}m  høyde:{y}m")

print() #en blank linje

#f)
print("Posisjon de første 10 sekundene:")
for tid in range(0,11):
    x,y = kanonkule_posisjon(tid)
    print(f"tid:{tid:4.1f}s lengde:{x:3.0f}m  høyde:{y:3.0f}m")

"""
Output av koden over skal bli:

lengde:  0m  høyde:  0m
lengde: 25m  høyde: 40m
lengde: 50m  høyde: 70m
lengde: 75m  høyde: 90m
lengde:100m  høyde:100m
lengde:125m  høyde:100m
lengde:150m  høyde: 90m
lengde:175m  høyde: 70m
lengde:200m  høyde: 40m
lengde:225m  høyde:  0m

Her ser vi at når kula er framme ved borgen (200m) er den 40 meter over bakken.
Den treffer bakken ved 225m, altså 25m "bortenfor" borgmuren, altså treffer den
borgen. (med mindre det er en veldig liten borg)
"""
