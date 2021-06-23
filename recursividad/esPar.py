def es_par(n):
  if n == 0:
    return True
  if n == 1:
    return False
  else:
    return es_par(n-2)

x = int(input("numero "))
print(es_par(x))
