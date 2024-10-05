number = input()

counter = 0
missing_numbers = []
all_numbers = '0123456789'

for n in all_numbers:
    if n not in number:
        missing_numbers.append(n)
        counter += 1

print(counter)
print(*missing_numbers)