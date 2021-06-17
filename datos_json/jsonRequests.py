import json
import requests
from pprint import pprint

response = requests.get('https://jsonplaceholder.typicode.com/todos')

pendientes = json.loads(response.text)

pendientes_por_usuario = {}

for pendiente in pendientes:
  if pendiente["completed"]:
    if pendiente["userId"] in pendientes_por_usuario:
      pendientes_por_usuario[pendiente["userId"]] += 1
    else:
      pendientes_por_usuario[pendiente["userId"]] = 1

def numero_tareas(par):
  return par[1]

items_ordenados = sorted(pendientes_por_usuario.items(), key=numero_tareas, reverse=True)

maximas_tareas_completadas = items_ordenados[0][1]

usuarios = []

for usuario, num_tareas_completadas in items_ordenados:
  if num_tareas_completadas == maximas_tareas_completadas:
    usuarios.append((str(usuario)))
  else:
    break

usuarios_con_max = " y ".join(usuarios)
print("los usuarios", usuarios_con_max)
print("han completado ", maximas_tareas_completadas, "tareas")

def filtro(pendiente):
  esta_completa = pendiente["completed"]
  esta_en_el_maximo_conteo = str(pendiente["userId"]) in usuarios
  return esta_completa and esta_en_el_maximo_conteo
  
with open("//home/santaka/mintic2022/datos_json/json/tareas_filtradas.json", "w") as archivo_salida:
  tareas_filtradas = list(filter(filtro, pendientes))
  json.dump(tareas_filtradas, archivo_salida, indent=2)
