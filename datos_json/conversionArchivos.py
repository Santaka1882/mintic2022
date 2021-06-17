import json
from pprint import pprint
strjson = '''{
"boolean1": null,
"diccionario": {"papa": 2000, "arroz": 5000},
"intValue": 0, 
"myList": [],
"myList2":["info1", "info2"],
"littleboolean": false, 
"myEmptyList": null,
"text1": null, 
"text2": "hello", 
"value1": null,
"value2": null
}'''
data = json.loads(strjson)
pprint(data)


print(data["text2"], type(data["text2"]))
print(data["text1"], type(data["text1"]))
print(data["intValue"], type(data["intValue"]))
print(data["myList"], type(data["myList"]))
print(data["myList2"], type(data["myList2"]))
print(data["diccionario"], type(data["diccionario"]))
print(data["myList2"][1])
print(data["diccionario"]["papa"])