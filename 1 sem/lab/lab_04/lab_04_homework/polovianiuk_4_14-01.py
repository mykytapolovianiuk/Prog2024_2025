n = int(input())

for i in range(n // 2, 0, -1):
    if n % i == 0:
        print(i)
        break
