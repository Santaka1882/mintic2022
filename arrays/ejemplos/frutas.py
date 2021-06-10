frutas = []
fruta = ""

while (fruta != "salir"):
  fruta = input("Digita una fruta o escribe salir para salir: ")
  if fruta != "salir":
    frutas.append(fruta)
print(frutas)