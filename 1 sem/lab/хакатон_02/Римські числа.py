roman_to_arabic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

arabic_to_roman = [
    (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
    (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
    (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
]

input_data = input()

A_roman, B_roman = input_data.split('+')

A_value = 0
prev_value = 0
for char in A_roman:
    current_value = roman_to_arabic[char]
    if current_value > prev_value:
        A_value += current_value - 2 * prev_value
    else:
        A_value += current_value
    prev_value = current_value

B_value = 0
prev_value = 0
for char in B_roman:
    current_value = roman_to_arabic[char]
    if current_value > prev_value:
        B_value += current_value - 2 * prev_value
    else:
        B_value += current_value
    prev_value = current_value

sum_value = A_value + B_value

result_roman = ''
for arabic, roman in arabic_to_roman:
    while sum_value >= arabic:
        result_roman += roman
        sum_value -= arabic

print(result_roman)