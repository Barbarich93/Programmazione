numero=int(input("Inserisci primo numero per il calcolo del fattoriale: "))
fattoriale = numero
for n in range(1,numero):
    fattoriale = fattoriale * n

print(f"Il fattoriale di {numero} è {fattoriale}")