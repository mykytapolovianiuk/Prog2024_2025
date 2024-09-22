import sys
sys.set_int_max_str_digits(0) # Дякую Павло Лазаренко за таку інформацію!

num = int(input())

factorial = 1

for i in range(1, num + 1):
    factorial *= i

num_digits = len(str(factorial))

print(num_digits)
