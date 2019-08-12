in_put = int(input())

if in_put%3==0 and in_put%5==0 and in_put%7==0:
  print("JugsMugsPugs")
elif in_put%3==0 and in_put%5==0:
  print("JugsMugs")
elif in_put%5==0 and in_put%7==0:
  print("MugsPugs")
elif in_put%7==0 and in_put%3==0:
  print("JugsPugs")
elif in_put%3 == 0:
  print("Jugs")
elif in_put%5 == 0:
  print("Mugs")
elif in_put%7 == 0:
  print("Pugs")
else:
  print(in_put)
