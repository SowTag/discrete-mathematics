def factorial(n):
  result = n
  while n > 1:
    n -= 1
    result *= n

  return result

def add_commas(n):
  number_str = str(int(n))

  reversed_str = number_str[::-1]
  result = ""
  for i, char in enumerate(reversed_str):
    if i % 3 == 0 and i != 0:
      result += ","
    result += char
  return result[::-1]


def permutation_nr(n):
  return factorial(n)

def variation_nr(n, k):
  return factorial(n) / factorial(n - k)

def variation_r(n, k):
  return n ** k

def combination_nr(n, k):
  return factorial(n) / (factorial(k) * factorial(n - k))

def combination_r(n, k):
  return combination_nr(n + k - 1, k)

def combinatorics():
  print("Combinatoria - Operaciones disponibles:")
  print("* Si el orden es relevante:")
  print("\tPermutación sin repetición: P(n) = n!")
  print("\tVariación sin repetición: V(n, k) = n! / (n - p)!")
  print("\tVariación con repetición: V(n, k) = n^k")
  print("* Si el orden es irrelevante:")
  print("\tCombinación sin repetición: C(n, k) = n! / (k!(n - k)!)")
  print("\tCombinación con repetición: C(n, k) = C(n + k - 1, k)")

  valid_values = False

  while not valid_values:
    print()
    n = None
    k = None

    try:
      n = int(input("Valor de N: "))
      k = input("Valor de K (opcional): ")

      if k:
        k = int(k)

        if n <= k:
          print("Error: n no puede ser menor o igual a k ya que provocaría una división por cero.")
          continue

      valid_values = True
    except:
      print("\nValores inválidos detectados.")

  print("")
  print("* Permutación sin repetición:", add_commas(permutation_nr(n)), "permutaciones")

  if k:
    print("* Variación sin repetición:", add_commas(variation_nr(n, k)), "variaciones")
    print("* Variación con repetición:", add_commas(variation_r(n, k)), "variaciones")
    print("* Combinación sin repetición:", add_commas(combination_nr(n, k)), "combinaciones")
    print("* Combinación con repetición:", add_commas(combination_r(n, k)), "combinaciones")
