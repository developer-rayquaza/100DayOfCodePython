digit_c = input()
number_s = input() 

# digit_c is the character equivalent of a digit  
# number_s is the string equivalent of a number 

#--------------METHOD 1 
# usual method 
#print("METHOD 1 output")
for digit in number_s: 
  if digit == digit_c:
    print(True)
    break
else:
  print(False)
  
#--------------METHOD 2 
# using the membership operator 'in' 
#print("METHOD 2 output")
if digit_c in number_s: 
  print(True)
else:
  print(False )
  
# -------------METHOD 3
# the Pythonic way! 
#print("METHOD 3 output")
print(digit_c in number_s) 
