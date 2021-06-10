lista = [11, 9, -2, 3, 8, 5]

var1, var2, var3 = [lista[i] for i in (1,3,5)]
print(var1, var2, var3)

var1, var2, var3 = [lista[i] for i in range(0,6,2)]
print(var1, var2, var3)