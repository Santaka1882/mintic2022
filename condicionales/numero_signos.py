def imprimir_numero(numero):
  if numero >= 0:
    print ("+", end = "")
  print(numero)

x = float(input("Ingrese el numero: "))

imprimir_numero(x)