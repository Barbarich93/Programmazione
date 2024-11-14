print("Scegli una figura tra: ")
scelta = print("Quadrato: digita 1")
scelta = print("Triangolo: digita 2")
scelta = print("Cerchio: digita 3")

if scelta == "1":
    lato = input(print("Quanto misura il lato?: "))
    perimetro = lato_1 * 4
    print("Il perimetro del quadrato è",perimetro)