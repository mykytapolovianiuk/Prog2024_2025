# Кількість слів

string = input()

new_string = ""
for char in string:
    if char.isalnum() or char.isdigit() or char.isspace():
        new_string += char
print(len(new_string.split()))



