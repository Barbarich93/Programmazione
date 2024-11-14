import socket as so         # IMPORTARE LIBRERIA "SOCKET"

SRV_ADDR = ""               # QUALE MEC ANDRESS ASCOLTARE (IN QUESTO CASO TUTTI)
SRV_PORT = 4444             # DA QUALE PORTA COLLEGARSI

s = so.socket(so.AF_INET, so.SOCK_DGRAM)    # METTERSI IN CONTATTO
s.bind((SRV_ADDR, SRV_PORT))                # RISERVARE LA PORTA
                                # QUANTE PORTE ASCOLTARE
print("Sto attendenso una connessione...")
connection, andress = s.accept()           # STABILIRE CONNESSIONE
print("Ho stabilito una connessione con: ", andress)
while True:                                 # CREARE UN CICLO, INPUT, OUTPUT
    print("C: ")
    data = connection.recv(1024)                            # (1024) = PUÒ RICEVERE MASSIMO 1024 CARATTERI
    if not data: break                                      # USCIRE DALLA CONNESSIONE SE CI SONO ERRORI DI CONNESSIONE (INTERRUZZIONI ECC.)
    connection.sendall (b"Ho ricevuto il messaggio! \n")    # INVIARE
    print(data.decode('utf-8'))
connection.close(  )                        #CHIUDERE CONNESSIONE