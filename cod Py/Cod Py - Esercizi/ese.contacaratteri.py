print("Scrivi una frase e ti dirò quanti caratteri ha")           # SPIEGAZIONE DELLA FUNZIONE DEL PROGRAMMA
frase = input("Scrivimi una frase: ")                             # LA VARIABILE "FRASE" SARÀ L' INPUT DELL' UTENTE

numero_caratteri = len(frase)                                     # "LEN" SERVE A CALCOLARE IL NUMERO DI CARATTERI IN UNA FRASE

print("La frase contiene", numero_caratteri, "caratteri.")