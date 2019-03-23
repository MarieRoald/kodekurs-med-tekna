# Oppgave 4

## 4a)
# Kode: print(Hei, Verden!)
# Feil: Mangler fnutter
print('Hei, Verden!')

## 4b)
# Kode: Print('Hei, Verden!')
# Feil: Stor P
print('Hei, Verden!')

## 4c)
# Kode:
### person = input('Hva heter du?')
### print('Hei på deg', navn)
# Feil: Feil variabelnavn, prøver å printe navn, ikke person
person = input('Hva heter du?')
print('Hei på deg', person)

## 4d)
# Kode:
### pi = 3,14
### radius = 4
### areal = radius *pi**2
# Her er det to feil:
## Feil 1: pi = 3,14
### I Python bruker vi punktum som desimaltegn
## Feil 2: areal = radius*pi**2
### Dette er ikke arealformelen. Selv om koden er "rett", betyr det ikke at den gjør det vi vil
pi = 3.14
radius = 4
areal = pi*radius**2
