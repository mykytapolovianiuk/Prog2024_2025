# Сума цифр двоцифрового числа

num = int(input())
num = abs(num)

firstNum = num // 10
lastNum = num % 10

print(firstNum + lastNum)