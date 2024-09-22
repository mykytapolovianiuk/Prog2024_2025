import sys
sys.set_int_max_str_digits(0) # Дякую Павло Лазаренко за таку інформацію!

factorial_value = int(input())

factorial = 1
num = 0

for i in range(1, 2001):
    factorial *= i
    if factorial == factorial_value:
        num = i
        break

print(num)