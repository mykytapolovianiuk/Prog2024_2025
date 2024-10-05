n = int(input())

result = 0
result += (n//100) * 100

n = n % 100
result += (n//20) * 30

n = n % 20
result += n * 2

print(result)