puertos = {80:"HTTP", 23:"SMTP", 443:"HTTPS"}
if 80 in puertos:
  print("yes")
if 110 not in puertos:
  print("no")
else:
  print("yes")