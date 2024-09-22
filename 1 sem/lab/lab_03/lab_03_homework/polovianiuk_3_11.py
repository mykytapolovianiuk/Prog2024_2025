number = input()

suma = 0
has_even_digits = False

for digit in number:
    digit_int = int(digit)
    if digit_int % 2 == 0:
        suma += digit_int
        has_even_digits = True

if has_even_digits:
    print(suma)
else:
    print(-1)
