fasitsvar = 45
maksforsøk = 100
print("Jeg har tenkt på et tall mellom 1 og 1000.")
print("Prøv å gjett det!")
print()

for forsøk in range(1, maksforsøk + 1):
    gjett = int(input("Gjett: "))
    
    if gjett == fasitsvar:
        print("Helt riktig!")
        print(f"Du brukte {forsøk} forsøk!")
        break  
    elif gjett > fasitsvar:
        print(f"Ditt gjett på {gjett} er for høyt.")
    elif gjett < fasitsvar:
        print(f"Ditt gjett på {gjett} er for lavt.")

else:  # Hvis løkka ikke avsluttes med break
    print(f"Der har du prøvd {maksforsøk} ganger og gått tom for gjett! Riktig svar er {fasitsvar}")
