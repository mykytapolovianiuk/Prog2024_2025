m, n = [int(x) for x in input().split()]

# m * n

multiplication = 0
i = 0

while i < m:
    multiplication = multiplication + n
    i += 1

print(multiplication)