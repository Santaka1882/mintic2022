text = ["cien", "años", "de", "soledad"]

apariciones = 0

for palabra in text:
  if "s" in palabra:
    apariciones += palabra.count("s")
print("Encontrada", apariciones, "veces")