num = int(input('Enter a number: '))

inv = 0
while num > 0:
    d = num % 10
    inv = inv * 10 + d
    num = num // 10

print(inv)

