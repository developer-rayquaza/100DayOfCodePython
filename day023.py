in_range = int(input())
rev = int(input())

for in_put in range(1, in_range+1):
  out_put = ""
  if(rev):
    if(in_put%7 is 0 or '7' in str(in_put)): out_put += "Pugs"
    if(in_put%5 is 0 or '5' in str(in_put)): out_put += "Mugs"
    if(in_put%3 is 0 or '3' in str(in_put)): out_put += "Jugs"
  else:
    if(in_put%3 is 0 or '3' in str(in_put)): out_put += "Jugs"
    if(in_put%5 is 0 or '5' in str(in_put)): out_put += "Mugs"
    if(in_put%7 is 0 or '7' in str(in_put)): out_put += "Pugs"
  print(out_put or in_put)
