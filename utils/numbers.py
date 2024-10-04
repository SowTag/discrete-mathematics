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