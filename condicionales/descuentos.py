def calculadora_descuentos(n, precio):
  if n <= 5:
    valor = n * precio
  elif n <= 10:
    valor = n * precio * 0.95
  elif n <= 20:
    valor = n * precio * 0.90
  else:
    valor = n * precio * 0.80
  return valor

print("---- Pago final ----")
print(calculadora_descuentos(4,10000))
print(calculadora_descuentos(8,10000))
print(calculadora_descuentos(15,10000))
print(calculadora_descuentos(25,10000))
