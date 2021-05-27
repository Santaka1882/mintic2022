from math import pi

def cuadrado( n ):
  return n ** 2

def area_circulo( radio ):
  return pi * cuadrado(radio)

print( area_circulo(5) )