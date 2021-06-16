# with open('/home/santaka/mintic2022/manejo de archivos/files/data.txt', 'r') as f:
#   data = f.read()
#   print(data)
#   f.close()

# with open('/home/santaka/mintic2022/manejo de archivos/files/wdata.txt', 'w') as f:
#   data = 'Estamos en clase de programacion 123 \n'
#   f.write(data)
#   f.write(data)
#   f.write(data)

# with open('/home/santaka/mintic2022/manejo de archivos/files/wdata.txt', 'a') as f:
#   data = 'Con estudiantes\n'
#   f.write(data)
#   f.write(data)
#   f.write(data)

# with open('/home/santaka/mintic2022/manejo de archivos/files/data1.txt', 'r') as f:
#   print(f.read())

# with open('/home/santaka/mintic2022/manejo de archivos/files/data1.txt', 'r') as f:
#   linea1 = f.read(6)
#   linea2 = f.read(10)
# print(linea1)
# print(linea2)

# with open('/home/santaka/mintic2022/manejo de archivos/files/data1.txt', 'r') as f:
#   print(f.readline())
#   print(f.readline())
#   print(f.readline())
#   print(f.readline())

# with open('/home/santaka/mintic2022/manejo de archivos/files/data1.txt', 'r') as f:
#   lines = f.readlines()
#   print(lines[3])

# with open('/home/santaka/mintic2022/manejo de archivos/files/data1.txt', 'r') as f:
#   for line in f:
#     print(line, end = "")

# with open('/home/santaka/mintic2022/manejo de archivos/files/data2.txt', 'a+') as f:
#   f.write('\nEsta es la linea 4: abcabcabc')

# values = [1234, 5678, 9012, 3.14159265, False]
# with open("/home/santaka/mintic2022/manejo de archivos/files/data3.txt", "w+") as f:
#   for value in values:
#     str_value = str(value)
#     f.write(str_value)
#     f.write("\n")

# with open("/home/santaka/mintic2022/manejo de archivos/files/data4.txt", "r") as f:
#   f.seek(11,0)
#   for line in f:
#     print(line, end='')

# with open("/home/santaka/mintic2022/manejo de archivos/files/data4.txt", "a+") as f:
#   print(f.tell())

# with open("/home/santaka/mintic2022/manejo de archivos/files/data5.txt", "r") as f:
#   list_content = f.readlines()
# list_content.insert(1, "Esta es la l ́ınea 1.5: jajaja\n")

# with open("/home/santaka/mintic2022/manejo de archivos/files/data5.txt", "w") as f:
#   contenido = "".join(list_content)
#   f.write(contenido)

# import os
# entries = os.scandir('/home/santaka/mintic2022/manejo de archivos/files/')
# for entry in entries:
#   print(entry.name + ", es directorio: "
#         + str(entry.is_dir()) + ', size:' +
#           str(entry.stat().st_size) + 'bytes.')

# import pickle 
# name = ["mohit", "bhaskar", "manish"]
# skill = ["Python", "Python", "Java"]
# dict1 = dict([(k,v) for k,v in zip(name, skill)])
# with open("/home/santaka/mintic2022/manejo de archivos/files/programming_powers.pkl", "wb") as p_file:
#   pickle.dump(name, p_file)
#   pickle.dump(skill, p_file)
#   pickle.dump(dict1, p_file)

# import pickle
# with open("/home/santaka/mintic2022/manejo de archivos/files/programming_powers.pkl", "rb") as p_file:
#   list1 = pickle.load(p_file)
#   list2 = pickle.load(p_file)
#   dict1 = pickle.load(p_file)
# print(list1)
# print(list2)
# print(dict1)

with open("/home/santaka/mintic2022/manejo de archivos/files/discurso.jpg", "rb") as imagen:
  data = imagen.read()
with open("/home/santaka/mintic2022/manejo de archivos/files/copy.jpg", "wb") as f:
  f.write(data)