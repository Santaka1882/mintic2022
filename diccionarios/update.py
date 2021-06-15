dict_ports1 = {22:"SSH", 80:"Http"}
dict_ports2 = {35:"DNS", 443:"https"}
print(dict_ports1)
dict_ports1.update(dict_ports2)
print(dict_ports1)