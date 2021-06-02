texto = input("Ingresa tu texto: ")
palabra = input("Que palabra buscas? ")

if palabra in texto:
  print("La palabra si se encuentra en el texto")
else:
  print("La palabra no se encuentra en el texto")