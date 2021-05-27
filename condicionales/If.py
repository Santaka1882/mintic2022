def comparar_numeros(a,b):
  if a > b:
    return a
  else:
    return b

numero1 = float(input('Ingrese el numero 1: '))
numero2 = float(input('Ingrese el numero 2: '))

print(comparar_numeros(numero1,numero2))