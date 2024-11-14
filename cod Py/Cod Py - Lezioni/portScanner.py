import socket as so

target = input("Inserisci l' indirizzo da scansire: ") # CHI È LA VITTIMA
portrange = input("Inserisci porta minima\n e porta massima nel dormato min-max es [5-200]: ") # DA QUALE PORTA A QUALE PORTA

lport = int(portrange.split('-')[0])
hport = int(portrange.split('-')[1])

print("Scansione in corso da", target, "dalla porta", lport, "alla porta", hport) # SVILUPPARE CICLO CHE VA DALLA PORTA PIU' BASSA ALLA PIU' ALTA
chiuse = ""
for port in range(lport, hport+1):
    s = so.socket(so.AF_INET, so.SOCK_STREAM)
    status = s.connect_ex((target, port))
    if(status ==0):
        print('*** Porta', port, '- APERTA ***')
    else:
        chiuse.appened(port)

if(len(chiuse) > 0):
    yesno = input(f"Trovate {len(chiuse)-1} chiuse, le vuoi visualizzare? (s/n) ")
    if(yesno.lower().starswith("s")):
        print(f"Porte chiuse: {chiuse}")
s.close

