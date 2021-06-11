v = [1, 2, 3, 4, 5, 6, 7, 8, 9]
w = [10, 10, 10, 10, 10, 10, 10, 10, 10]
z = []

producto_escalar = 0

for n in range(0, len(v)):
  producto = v[n] * w[n]
  z.append(producto)

for n in z:
  producto_escalar += n

print(producto_escalar)
