print("scrivimi un numero e ti dirò se è pari o dispari")   # PRESENTAZIONE DELLA FUNZIONE DEL PROGRAMMA
numero = int(input("Inserisci un numero: "))                # CHIEDE IL NUMERO
if numero % 2 == 0:                                         # SE IL NUMERO DIVISO "2" DA RESTO "0"
    print("Il numero è pari")
else:                                                       # ALTRIMENTI
    print("Il numero è dispari")