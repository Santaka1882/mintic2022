import json

data = {
  'cientifico': {"Nombre": "Alan Mathison Turing", "Edad": "41"}
}

with open("/home/santaka/mintic2022/datos_JSON/JSON/data_file.json", "w") as write_file:
  json.dump(data, write_file)