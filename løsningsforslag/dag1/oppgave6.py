from math import sqrt 
## %% 6a)
a = 1
b = 2.5
c = 1
løsning1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
løsning2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)

print(f'Løsningene for likningen {a}xˆ2 + {b}x + {c} = er {løsning1} og {løsning2}')

# %% 6 b) 

a = float(input('Hva er a? '))
b = float(input('Hva er b? '))
c = float(input('Hva er c? '))

løsning1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
løsning2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)

print(f'Løsningene for likningen {a}xˆ2 + {b}x + {c} = er {løsning1} og {løsning2}')

# %% 6 c) 2 min - 9 min
a = float(input('Hva er a? '))
b = float(input('Hva er b? '))
c = float(input('Hva er c? '))

rot_del = b**2 - 4*a*c

if rot_del < 0:1
    print(f' {a}xˆ2 + {b}x + {c} = 0 har dessverre ingen reelle løsninger')
else:
    løsning1 = (-b + sqrt(rot_del))/(2*a)
    løsning2 = (-b - sqrt(rot_del))/(2*a)
    print(f'Løsningene for likningen {a}xˆ2 + {b}x + {c} = 0 er {løsning1} og {løsning2}')
3