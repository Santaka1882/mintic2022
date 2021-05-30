def freeTimeCalculator(animaciones):
  cantidad_base = int(animaciones)
  print("La cantidad de animaciones que puedes ver es:", animaciones)
  novelas = cantidad_base * 2 + 4
  print("La cantidad de novelas que puedes leer es:", novelas)
  peliculas = int((cantidad_base + novelas) / 5)
  print("La cantidad de peliculas que puedes ver es:", peliculas)

  if (peliculas <= 20):
    nivel = "uno"
  elif (peliculas <= 30):
    nivel = "dos"
  elif (peliculas <= 50):
    nivel = "tres"
  else:
    nivel = "cuatro"
  
  print("Tu nivel de tiempo libre es:", nivel)

cantidad_animaciones = input('¿Cuantas animaciones puedes ver en tu tiempo libre? ')

freeTimeCalculator(cantidad_animaciones)