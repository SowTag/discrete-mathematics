print("[2] Conjuntos")
def conjuntos():
    # Función para convertir los elementos a números si es posible, sino mantenerlos como cadenas
    def convertir_elementos(elementos):
        resultado = []
        for elemento in elementos:
            try:
                # Intentamos convertir a entero o flotante
                if '.' in elemento:
                    resultado.append(float(elemento))  # Convertir a float si hay punto decimal
                else:
                    resultado.append(int(elemento))    # Convertir a entero si no hay punto decimal
            except ValueError:
                resultado.append(elemento)  # Si falla, mantenerlo como cadena (letras)
        return resultado

    # Función para obtener la diferencia entre dos conjuntos
    def diferencia(conjunto1, conjunto2):
        return list(set(conjunto1) - set(conjunto2))

    # Función para obtener el complemento de un conjunto con respecto al universo
    def complemento(universo, conjunto):
        return list(set(universo) - set(conjunto))

    # Función para realizar la unión sin perder el orden
    def union_ordenada(conjunto1, conjunto2):
        union = conjunto1[:]  # Copia de conjunto1 para preservar el orden
        for elemento in conjunto2:
            if elemento not in union:
                union.append(elemento)
        return union

    # Función principal
    def main():
        # Entrada de datos por parte del usuario
        universo_input = input("Ingrese los elementos del conjunto universo separados por espacios: ").split()
        conjunto1_input = input("Ingrese los elementos del conjunto 1 separados por espacios: ").split()
        conjunto2_input = input("Ingrese los elementos del conjunto 2 separados por espacios: ").split()

        # Convertir los elementos a números o mantenerlos como cadenas
        universo = convertir_elementos(universo_input)
        conjunto1 = convertir_elementos(conjunto1_input)
        conjunto2 = convertir_elementos(conjunto2_input)
        
        # Mostrar los conjuntos en el mismo orden que fueron ingresados
        print("\nConjunto Universo:", universo)
        print("Conjunto 1:", conjunto1)
        print("Conjunto 2:", conjunto2)
        
        # Operaciones en función de si los conjuntos están vacíos
        if universo:  # Si el conjunto universo no está vacío
            if conjunto1 and conjunto2:  # Si ambos conjuntos están presentes
                # Unión que mantiene el orden
                union = union_ordenada(conjunto1, conjunto2)
                print("\nUnión entre Conjunto 1 y Conjunto 2:", union)
                interseccion = list(set(conjunto1) & set(conjunto2))
                print("Intersección entre Conjunto 1 y Conjunto 2:", interseccion)
                print("Diferencia entre Conjunto 1 y Conjunto 2 (C1 - C2):", diferencia(conjunto1, conjunto2))
                print("Diferencia entre Conjunto 2 y Conjunto 1 (C2 - C1):", diferencia(conjunto2, conjunto1))
                print("Complemento del Conjunto 1 respecto al Universo:", complemento(universo, conjunto1))
                print("Complemento del Conjunto 2 respecto al Universo:", complemento(universo, conjunto2))
                
            elif conjunto1:  # Solo Conjunto 1 está presente
                print("\nUnión entre Conjunto Universo y Conjunto 1:", union_ordenada(universo, conjunto1))
                print("Complemento del Conjunto 1 respecto al Universo:", complemento(universo, conjunto1))
                print("Complemento del Conjunto 2 respecto al Universo:", complemento(universo, conjunto2))
            elif conjunto2:  # Solo Conjunto 2 está presente
                print("\nUnión entre Conjunto Universo y Conjunto 2:", union_ordenada(universo, conjunto2))
                print("Complemento del Conjunto 2 respecto al Universo:", complemento(universo, conjunto2))
                print("Complemento del Conjunto 1 respecto al Universo:", complemento(universo, conjunto1))
            else:  # Ambos conjuntos 1 y 2 están vacíos
                print("\nNo hay conjuntos 1 ni 2 para operar. Solo se utilizará el conjunto universo.")
        
        else:  # Si el conjunto universo está vacío
            if conjunto1 and conjunto2:  # Ambos conjuntos 1 y 2 presentes
                union = union_ordenada(conjunto1, conjunto2)
                print("\nUnión entre Conjunto 1 y Conjunto 2:", union)
                interseccion = list(set(conjunto1) & set(conjunto2))
                print("Intersección entre Conjunto 1 y Conjunto 2:", interseccion)
                print("Diferencia entre Conjunto 1 y Conjunto 2 (C1 - C2):", diferencia(conjunto1, conjunto2))
                print("Diferencia entre Conjunto 2 y Conjunto 1 (C2 - C1):", diferencia(conjunto2, conjunto1))
            elif conjunto1:  # Solo Conjunto 1 está presente
                print("\nUnión entre Conjunto 1 y Universo (vacío):", conjunto1)
                print("Complemento del Conjunto 1 respecto al Universo (vacío):", complemento([], conjunto1))
            elif conjunto2:  # Solo Conjunto 2 está presente
                print("\nUnión entre Conjunto 2 y Universo (vacío):", conjunto2)
                print("Complemento del Conjunto 2 respecto al Universo (vacío):", complemento([], conjunto2))
            else:  # Ambos conjuntos 1 y 2 están vacíos
                print("\nTodos los conjuntos están vacíos.")

    # Ejecución del programa
    if __name__ == "__main__":
        main()

conjuntos()
