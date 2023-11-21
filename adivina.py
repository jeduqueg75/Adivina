import random


def adivina_el_número (x):

    print("=========================")
    print("   BIENVENID@ AL JUEGO   ")
    print("=========================")
    print("Adivina el número que eligió el pc")

    número_aleatorio = random.randint(1, x) ## aleatorio entre 1 y x

    prediccion = 0

    while prediccion != número_aleatorio:
        #el usuario ingresa el número
        prediccion = int(input(f"adivina el número entre 1 y {x}: ")) #f-string
        
        if prediccion < número_aleatorio:
            print("el número es menor. intenta otra vez")
        elif prediccion > número_aleatorio:
            print("el número es mayor. intenta otra vez")
    print(f"Felicitaciones adivinaste el número {número_aleatorio} correctamente")


adivina_el_número(20)
