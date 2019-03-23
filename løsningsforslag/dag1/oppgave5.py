# Oppgave 5

## 5a)
tall = float(input('Gi meg et tall: '))
if tall > 0:
	absoluttverdi = tall
else:
	absoluttverdi = -tall
print(f'Absoluttverdien til {tall} er {absoluttverdi}')

## 5b)
tall1 = float(input('Gi meg et tall: '))
tall2 = float(input('Gi meg enda et tall: '))
if tall1 > 0:
	absoluttverdi1 = tall1
else:
	absoluttverdi1 = -tall1

if tall2 > 0:
	absoluttverdi2 = tall2
else:
	absoluttverdi2 = -tall2

if absoluttverdi1 > absoluttverdi2:
	print(f'Absoluttverdien til {tall1} er større enn den til {tall2}')
elif absoluttverdi1 < absoluttverdi2:
	print(f'Absoluttverdien til {tall2} er større enn den til {tall1}')
else:
	print(f'Absoluttverdien til {tall1} er like stor som den til {tall2}')

