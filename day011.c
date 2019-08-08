three_digit_number = int(input())

sum_digit = 0

while(three_digit_number!=0):
  sum_digit += three_digit_number%10
  three_digit_number //= 10

print(sum_digit)
