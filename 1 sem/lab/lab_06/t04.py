# Зайві пропуски

string = input()

n = len(string)
for l in range(n):
    if string[l] != ' ':
        break
for r in range(n - 1, -1, -1):
    if string[r] != ' ':
        break

result = string[l:r + 1]

new_string = ""
for char in result:
    if char != " ":
        new_string += char
    else:
        if new_string[-1] != " ":
            new_string += char
print(new_string)