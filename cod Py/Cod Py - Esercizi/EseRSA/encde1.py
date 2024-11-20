from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
import base64

password_prv="Simone"
password_pub="Barbieri"

print("\nInserisci il messaggio da criptare: ")
message = input()

with open('private_key.pem', 'rb') as key_file:                          # CARICA LE CHIAVI PRIVATE
     private_key = serialization.load_pem_private_key (key_file.read(), password=None)
     
with open('public_key.pem', 'rb') as key_file:                           # CARICA LA CHIAVE PUBBLICA
      public_key = serialization.load_pem_public_key(key_file.read())

encrypted = public_key.encrypt(message.encode(), padding.PKCS1v15())     # CRIPTAZIONE CON LA CHIAVE PUBBLICA


print("\nMessaggio criptato in:", base64.b64encode(encrypted).decode('utf-8'))

print("\nPer decriptarlo inserisci la prima chiave: ")
chiave_prv = input()
if chiave_prv == password_prv:
      print("\nPer decriptarlo inserisci la seconda chiave:")
      chiave_pub = input()
      if chiave_pub == password_pub:
            decrypted = private_key.decrypt(encrypted, padding.PKCS1v15())           # DECRIPTAZIONE CON LA CHIAVE PRIVATA
            print("\nMessaggio originale:", message)
            print("Messaggio decriptato:", decrypted.decode('utf-8'))
      else:
            input("\nChiave spabliata")
            

else:
      print("\nChiave sbagliata")
      

