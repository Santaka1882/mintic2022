año = 2022
poblacion_A = 25000000
poblacion_B = 18500000

while poblacion_B < poblacion_A:
  poblacion_A = poblacion_A * 1.02
  poblacion_B = poblacion_B * 1.03

  año += 1

print("La poblacion de la ciudad B supera a la de la ciudad A en el año", año)