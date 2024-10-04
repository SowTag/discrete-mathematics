import random

def lanzar_moneda(num_monedas):
    caras = 0
    cruces = 0

    for _ in range(num_monedas):
        resultado = random.choice(['Cara', 'Cruz'])
        if resultado == "Cara":
            caras +=1
        else:
            cruces += 1
    
    return caras, cruces

def calcular_probabilidad(caras, cruces, total_de_lanzamientos):
    prob_de_caras = caras/total_de_lanzamientos
    prob_de_cruces = cruces/total_de_lanzamientos
    return prob_de_caras,prob_de_cruces

def juego():
    
    while True:
        try:
            num_monedas = int(input("Ingresa las monedas a lanzar: "))
            if num_monedas <= 0:
                print("El numero tiene numero tiene que ser mayor a 0.")
            else:
                break
        except ValueError:
            print("Por favor, ingresar un numero valido.")
    
    caras, cruces = lanzar_moneda(num_monedas)

    prob_caras, prob_cruces = calcular_probabilidad(caras, cruces, num_monedas)

    print(f"Resultado despues de {num_monedas} lanzadas:")
    print(f"Caras: {caras} (Probabilidad: {prob_caras: .2f})")
    print(f"Cruces: {cruces} (Probabilidad: {prob_cruces: .2f})")


juego()