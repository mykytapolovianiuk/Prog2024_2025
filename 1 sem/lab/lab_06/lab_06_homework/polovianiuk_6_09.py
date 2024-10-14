expression = input()

operations = ['+', '-', '*', '**', '/', '//', '%']

count = 0

i = 0
while i < len(expression):
    if expression[i:i+2] == '**':
        count += 1
        i += 2
    elif expression[i] in ['+', '-', '*', '/', '%']:
        count += 1
        if expression[i:i+2] == '//':
            i += 2
        else:
            i += 1
    else:
        i += 1

print(count)
