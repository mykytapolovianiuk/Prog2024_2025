num = int(input())

num = abs(num)

firstNum = (num // 10) // 10
lastNum = num % 10

if firstNum > lastNum:
    print(firstNum)
elif lastNum > firstNum:
    print(lastNum)
else:
    print("=")