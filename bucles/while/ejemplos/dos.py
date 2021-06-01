def listadoImpar():
  print("Listado de numeros impares: ")

  i = 1
  while (i <= 1000):
    if i % 2 != 0:
      print(i)

    i += 1

def listadoPar():
  print("Listado de numeros pares: ")

  i = 1
  while (i <= 1000):
    if i % 2 == 0:
     print(i)

    i += 1

def main():
  listadoImpar()
  listadoPar()

main()