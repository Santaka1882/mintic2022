import json

with open("//home/santaka/mintic2022/datos_json/json/data_file.json", "r") as read_file:
  data = json.load(read_file)
print(data["cientifico"])