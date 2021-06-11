arreglo = [1.5 * x for x in range(1,11)]
suma = 0

for n in arreglo:
  suma += n

promedio = suma / len(arreglo)

print(promedio)