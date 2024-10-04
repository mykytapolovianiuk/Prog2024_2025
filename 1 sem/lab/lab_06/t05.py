# Без повторень 3
string = input()

new_string = string[0]
for char in string[1:]:
    if new_string[-1] != char:
        new_string += char
print(new_string)