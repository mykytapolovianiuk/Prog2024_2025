# Добуток цифр трицифрового числа

num = int(input())

firstNum = num // 100
secondNum = (num // 10) % 10
thirdNum = num % 10

productOfNum = firstNum * secondNum * thirdNum

print(productOfNum)
