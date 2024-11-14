import http.client

host = input("Inserisci host/IP del sistema target: ")
port = input("Inserisci la porta del sistema target (defoult:80)")
path = input("Inserisci il percorso (defoult:'/): ")
if(port==""): port = 80
if(path==""): port = '/'
try:
    connection = http.client.HTTPConnection(host, port)
    connection.request('OPTIONS', path)
    response = connection.getresponse()
    if(response.status >= 200 and response.status <= 299 and response.getheader("Allow") ):
        print("I metodi abilitati sono", response.getheader("Allow"))
    else:
        print("usa un metodo alternativo per determinare i verbi", response.status, response.getheader)
        connection.close()
except ConnectionError:
    print("Connessione fallita", ConnectionError.strerror)
