def simetrica(relacion):
    for (a, b) in relacion:
        if (b, a) not in relacion:
            return False
    return True

def antisimetrica(relacion):
    for (a, b) in relacion:
        if a != b and (b, a) in relacion:
            return False
    return True

def reflexiva(relacion, conjunto):
    for a in conjunto:
        if (a, a) not in relacion:
            return False
    return True

def transitiva(relacion):
    for (a, b) in relacion:
        for (c, d) in relacion:
            if b == c and (a, d) not in relacion:
                return False
    return True

def ingresar_relacion():
    conjunto = input("Ingresa los elementos del conjunto, separados por comas: ").split(',')
    relacion = []
    n = int(input("Ingresa el número de pares en la relación: "))
    for _ in range(n):
        par = input("Ingresa un par de la relación en el formato 'a,b': ").split(',')
        relacion.append((par[0].strip(), par[1].strip()))
    return conjunto, relacion


conjunto, relacion = ingresar_relacion()

print(f"Relación: {relacion}")
print(f"Es reflexiva: {reflexiva(relacion, conjunto)}")
print(f"Es simétrica: {simetrica(relacion)}")
print(f"Es antisimétrica: {antisimetrica(relacion)}")
print(f"Es transitiva: {transitiva(relacion)}")
