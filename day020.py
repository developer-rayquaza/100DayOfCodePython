in_put = int(input())

# Hello Sir! I think!, I have made it correctly now Sir!! ...
out_put = ""

if(in_put%3 == 0): # if statement 1
  out_put += "Jugs"
if(in_put%5 == 0): # if statement 2
  out_put += "Mugs"
if(in_put%7==0): # if statement 3
  out_put += "Pugs"
print(out_put or in_put) #Single print statement....
