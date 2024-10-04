# Кількість операцій

string = input()

count = 0
for char in string[1::]:
    if char in ("*", "-", "+"):
        count += 1

print(count)