def mas_uno(n):
  return n + 1

d = 10

desplaza = [d + x for x in range(5)] #Crea una lista con los numeros del 10 al 14
print(desplaza)

potencias = [3 ** x for x in range(2, 6)] #Crea una lista con las 4 primeras potencias de 3
print(potencias)


potencias2 = [3 ** mas_uno(x)  for x in range(2, 6)] #Crea una lista con las potencias de tres entre 2 y 6
print(potencias2)