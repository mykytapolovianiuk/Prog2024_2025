m = int(input())

steps = 0

for i in range(100):
    if str(m) == str(m)[::-1]:
        break
    m += int(str(m)[::-1])
    steps += 1

print(steps)
