def multiplicacion(x, y):
  if y == 0:
    return 0
  else:
    return multiplicacion(x , y - 1) + x

print(multiplicacion(3, 3))