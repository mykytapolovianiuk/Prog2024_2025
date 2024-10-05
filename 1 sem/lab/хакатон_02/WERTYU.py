row1 = "`1234567890-="
row2 = "QWERTYUIOP[]\\"
row3 = "ASDFGHJKL;'"
row4 = "ZXCVBNM,./"

keyboard_rows = [row1, row2, row3, row4]

input_lines = []
while True:
    try:
        line = input()
        input_lines.append(line)
    except EOFError:
        break

for line in input_lines:
    decoded_message = []

    for char in line:
        found = False
        for row in keyboard_rows:
            if char in row:
                index = row.index(char)
                decoded_message.append(row[index - 1])
                found = True
                break
        if not found:
            decoded_message.append(char)

    print(''.join(decoded_message))