def reflexiva(relacion, conjunto):
    for a in conjunto:
        if (a, a) not in relacion:
            print(f"- {a} no está relacionado consigo mismo, por lo tanto NO es una relación reflexiva.")
            return False
    print("- Todos los elementos están relacionados consigo mismos. La relación es reflexiva.")
    return True

def simetrica(relacion):
    for (a, b) in relacion:
        if (b, a) not in relacion:
            print(f"- {a} está relacionado con {b}, pero {b} no está relacionado con {a}. Entonces NO es Simétrica.")
            return False
    print("- Para todos los pares, si (a, b) se encuentra en la relación, entonces (b, a) también lo está. La relación es Simétrica.")
    return True

def antisimetrica(relacion):
    for (a, b) in relacion:
        if a != b and (b, a) in relacion:
            print(f"- {a} está relacionado con {b} y a su vez {b} está relacionado con {a}, pero {a} ≠ {b}. No es Antisimétrica.")
            return False
    print("- No hay pares distintos que se relacionen en ambas direcciones. La relación es Antisimétrica.")
    return True

def transitiva(relacion):
    for (a, b) in relacion:
        for (c, d) in relacion:
            if b == c and (a, d) not in relacion:
                print(f"- {a} está relacionado con {b}, y {b} con {d}, pero {a} no está relacionado con {d}. No es Transitiva.")
                return False
    print("- Para todos los pares, si (a, b) y (b, c) están en la relación, entonces (a, c) también lo está. La relación es Transitiva.")
    return True

def ingresar_relaciones():
    print("=== Ingreso de relación y conjunto ===")
    conjunto = input("Ingresa los elementos del conjunto (sepáralos por comas, ej: a,b,c,d): ").split(",")
    conjunto = [k.strip() for k in conjunto]
    relacion = []
    
    print("Ahora ingresa los pares ordenados de la relación: ")
    
    while True:
        pares = input("Ingresa un par en formato 'a,b' (S para terminar): ")
        if pares.lower() == "s":  # Aquí está el cambio
            break
        try:
            a, b = pares.split(",")
            relacion.append((a.strip(), b.strip()))
        except:
            print("El formato es incorrecto. Vuelve a intentarlo.")
            
    return conjunto, relacion

def mostrar_datos(conjunto, relacion):
    print(f"\nConjunto: {conjunto}")
    print(f"Relación: {relacion}")
    
    # Verificación
    reflexiva(relacion, conjunto)
    simetrica(relacion)
    antisimetrica(relacion)
    transitiva(relacion)

def main():
    print(" === Verificación de las propiedades ===")
    conjunto, relacion = ingresar_relaciones()
    mostrar_datos(conjunto, relacion)
    

main()