n = int(input())

if n == 1:
    total_sum = 0
    for i in range(100, 1000):
        hundreds = i // 100
        tens = (i // 10) % 10
        units = i % 10
        if hundreds % 2 == 0 and tens % 2 == 0 and units % 2 == 0:
            total_sum += i
    print(total_sum)
elif n == 2:
    count = 0
    for i in range(100, 1000):
        hundreds = i // 100
        tens = (i // 10) % 10
        units = i % 10
        if hundreds < tens < units:
            count += 1
    print(count)
elif n == 3:
    total_sum = 0
    for i in range(100, 1000):
        hundreds = i // 100
        tens = (i // 10) % 10
        units = i % 10
        if hundreds % 2 != 0 and tens % 2 != 0 and units % 2 != 0:
            total_sum += i
    print(total_sum)
elif n == 4:
    count = 0
    for i in range(100, 1000):
        hundreds = i // 100
        tens = (i // 10) % 10
        units = i % 10
        if hundreds > tens > units:
            count += 1
    print(count)
elif n == 5:
    total_sum = 0
    for i in range(100, 1000):
        hundreds = i // 100
        tens = (i // 10) % 10
        units = i % 10
        if i == hundreds**3 + tens**3 + units**3:
            total_sum += i
    print(total_sum)
elif n == 6:
    count = 0
    for i in range(100, 1000):
        hundreds = i // 100
        tens = (i // 10) % 10
        units = i % 10
        if hundreds != tens and hundreds != units and tens != units:
            count += 1
    print(count)