from utils.numbers import add_commas

def coinflip():
  print("* Hacer n tiros de una moneda, calculando sus distintas probabilidades.")

  n = None

  while not n:
    try:
      n_raw = input("Valor de n o Ctrl-C para salir > ")
      n = int(n_raw)
    except KeyboardInterrupt:
      print("\nSaliendo...")
      return
    
    except ValueError:
      print("\nNo es un entero válido.")
      continue

  print("Para", add_commas(n), "tiros de moneda hay",  add_commas(2 ** n), "posibles estados finales posibles, de los cuales:")

  for i in range(1, n + 1):
    probability = n * (1 / 2)

    print("El %f seran con %i moneda(s) de un mismo lado" % (probability, i))