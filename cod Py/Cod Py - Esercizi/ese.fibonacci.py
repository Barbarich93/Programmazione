numero_iniziale = int(input("Da quale numero devo iniziare a calcolare la sequenza di Fibonacci?: "))
numero_finale = int(input("Dopo quanti numeri mi devo fermare?: "))
a, b = 0, 1
while a < numero_iniziale:
    a, b = b, a + b
print("Questa la sequenza a partire da", numero_iniziale, ":")
for _ in range (numero_finale):
    print(a, end=" ")
    a, b= b, a + b