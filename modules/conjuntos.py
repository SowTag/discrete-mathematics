print("[2] Conjuntos")
def conjuntos():
    # Función para obtener la unión de dos conjuntos
    def union(conjunto1, conjunto2):
        return conjunto1.union(conjunto2)

    # Función para obtener la intersección de dos conjuntos
    def interseccion(conjunto1, conjunto2):
        return conjunto1.intersection(conjunto2)

    # Función para obtener la diferencia de dos conjuntos (conjunto1 - conjunto2)
    def diferencia(conjunto1, conjunto2):
        return conjunto1.difference(conjunto2)

    # Función para obtener el complemento de un conjunto (en un universo dado)
    def complemento(universo, conjunto):
        return universo.difference(conjunto)

    # Programa principal
    def main():
        # Definir el universo de elementos (dependerá del caso de uso)
        inicio_conjunto_universo = int(input("Ingrese un entero para el inicio del conjunto universo: "))
        fin_conjunto_universo = int(input("Ingrese un entero para el fin del conjunto universo: "))
        universo = set(range(inicio_conjunto_universo, fin_conjunto_universo + 1))  # Ejemplo: un universo de elementos del 1 al 100

        # Solicitar los elementos del conjunto 1 al usuario
        elementos1 = input("Ingrese los elementos del conjunto 1 separados por comas: ")
        conjunto1 = set(map(int, elementos1.split(',')))

        # Solicitar los elementos del conjunto 2 al usuario
        elementos2 = input("Ingrese los elementos del conjunto 2 separados por comas: ")
        conjunto2 = set(map(int, elementos2.split(',')))

        # Calcular las operaciones
        print(f"Conjunto 1: {conjunto1}")
        print(f"Conjunto 2: {conjunto2}")

        print(f"Unión: {union(conjunto1, conjunto2)}\n")
        print(f"Intersección: {interseccion(conjunto1, conjunto2)}\n")
        print(f"Diferencia (Conjunto 1 - Conjunto 2): {diferencia(conjunto1, conjunto2)}\n")
        print(f"Diferencia (Conjunto 2 - Conjunto 1): {diferencia(conjunto2, conjunto1)}\n")
        print(f"Conjunto complementar del Conjunto 1: {complemento(universo, conjunto1)}\n")
        print(f"Conjunto complementar del Conjunto 2: {complemento(universo, conjunto2)}\n")

    if __name__ == "__main__":
        main()
conjuntos()