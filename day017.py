in_put = int(input())
if in_put%3==0 and in_put%5==0:
  print("JugsMugs")
elif in_put%3 == 0:
  print("Jugs")
elif in_put%5 == 0:
  print("Mugs")
else:
  print(in_put)
