with open("/home/santaka/mintic2022/problemas/SalesJan2009.csv", "r") as sales_f:
  encabezado = sales_f.readline().split(",")
  lineas = sales_f.readlines()
  transacciones = []
  for linea in lineas:
    linea = linea.split(',')
    transaccion = dict(list(zip(encabezado, linea)))
    transacciones.append(transaccion)

pais = input("Pais a consultar? ")
apariciones = 0
for t in transacciones:
  if t["Country"].upper() == pais.upper():
    apariciones += 1

print("Se hicieron", apariciones, "transacciones en", pais)