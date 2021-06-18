# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# try:
#   pos = int(input('A que posicion quieres acceder? '))
# except ValueError:
#   print('Ingresa un numero entero por favor')
# else:
#   try: 
#     print(lista[pos])
#   except IndexError:
#     print('la posicion', pos, 'no esta en lista')

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pos = 0
flag = True

while flag:
  try:
    pos = int(input('A que posicion quieres acceder? '))
    print(lista[pos])
  except ValueError:
    print('Ingresa un numero entero por favor')
  except IndexError:
    flag = False
    print('la posicion', pos, 'no está en lista')