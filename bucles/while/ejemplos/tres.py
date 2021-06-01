numeroBase = int(input("Ingresa un numero: "))

print("Los numeros pares menores a", numeroBase, "son:")

if numeroBase % 2 == 0:
  numeroBase
else:
  numeroBase -= 1

while numeroBase >= 2:
  print(numeroBase)
  numeroBase -= 2