def sum_args(*numbers):
  sum = 0
  for number in  numbers:
      sum += number
  return sum
print(sum_args(8, 17, 26, 28))
