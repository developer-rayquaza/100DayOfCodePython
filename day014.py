first_data = int(input())
sec_data = int(input())
third_data = int(input())

if(first_data<sec_data and first_data<third_data):
  print(first_data)
elif(sec_data<third_data):
  print(sec_data)
else:
  print(third_data)
