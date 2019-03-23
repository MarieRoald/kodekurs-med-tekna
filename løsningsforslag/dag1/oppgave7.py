# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 15:02:07 2019

@author: Marie
"""

# Oppgave 7

## a)

bank1_rente = 1.03
bank2_rente1 = 1.033
bank2_rente2 = 1.028

start_beløp = 10000

år = 10
bank1_penger = start_beløp
# Bank1
for i in range(år): 
    bank1_penger *= bank1_rente
    
print(f'Etter {år} år har du {bank1_penger:.2f},- i bank 1')

bank2_penger = start_beløp
for i in range(5): 
    bank2_penger *= bank2_rente1
    

for i in range(5, år):
    bank2_penger *= bank2_rente2
    

print(f'Etter {år} år har du {bank2_penger:.2f},- i bank 2')



## b) Ved å prøve deg frem kan du finne ut at det lønner seg med bank1 dersom du
# sparer i 12 år. 


## c)
år = 10
bank1_penger = 0

for i in range(år): 
    bank1_penger += 1000
    bank1_penger *= bank1_rente
    
print(f'Etter {år} år har du {bank1_penger:.2f},- i bank 1')

bank2_penger = 0
for i in range(5): 
    bank2_penger += 1000
    bank2_penger *= bank2_rente1
    

for i in range(5, år):
    bank2_penger += 1000
    bank2_penger *= bank2_rente2
    

print(f'Etter {år} år har du {bank2_penger:.2f},- i bank 2')

## d) 9 år