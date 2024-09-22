num = input()

modified_number = ''

for digit in num:
    digit_int = int(digit)
    if digit_int % 2 == 0:
        modified_number += str(digit_int + 1)
    else:
        modified_number += str(digit_int - 1)

final_number = int(modified_number)

print(final_number)
