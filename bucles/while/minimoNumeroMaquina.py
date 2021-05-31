def min_maquina():
  Xo = 1.0
  Xi = Xo / 2.0
  while(Xi > 0.0):
    Xo = Xi
    Xi = Xo / 2.0
  return Xo
  
print("El minimo numero positivo", end = (" "))
print("En esta maquina es:", min_maquina())
