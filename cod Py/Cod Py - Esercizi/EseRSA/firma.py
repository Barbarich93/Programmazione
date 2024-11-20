from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes               # CREO HASH DEL MESSAGGIO
from cryptography.hazmat.primitives import serialization
import base64

# CARICA CHIAVE PRIVATA
with open('private_key.pem', 'rb') as key_file:                   
    private_key = serialization.load_pem_private_key(key_file.read(),password=None)

# CARICA CHIAVE PUBBLICA
with open('public_key.pem', 'rb') as key_file:
    public_key = serialization.load_pem_public_key(key_file.read())

message = 'Ciao, Epicode spacca!'

# FIRMA CON LA CHIAVE PRIVATA
signed = private_key.sign(message.encode(), padding.PKCS1v15(), hashes.SHA256())

# VERIFICA DELLA FIRMA CON LA CHIAVE PUBBLICA
try:
    encrypted_b64 = base64.b64encode(signed).decode('utf-8')
    public_key.verify(signed, message.encode(), padding.PKCS1v15(), hashes.SHA256())
    print("Base64 della firma:", encrypted_b64)
    print("Messaggio originale da confrontare:", message)
    print("La firma è valida.")
except Exception as e:
    print("La firma non è valida.", str(e))