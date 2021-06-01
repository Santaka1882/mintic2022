def suma(n):
  s = 0
  for i in range(1, n + 1, 1):
    s += i
  return s

def main():
  n = int(input("n? = "))
  print("La suma de los digitos anteriores a", n, "es:", end = " ")
  print(suma(n))

main()