inicio = int(input("Inicio: ")) 
fin = int(input("Fin: ")) + 1
incremento = int(input("Incremento: "))

for i in range(inicio, fin, incremento):
  print(i)