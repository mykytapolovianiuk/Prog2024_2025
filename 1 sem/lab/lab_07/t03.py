# НСД двох чисел

# Умова: Знайдіть НСД (найбільший спільний дільник) двох натуральних чисел.

def gcd(num1, num2):
    if num1 < num2:
        num1, num2 = num2, num1

    while num2 > 0:
        num1, num2 = num2, num1 % num2

        return num2

# Main
print(gcd(3 * 5 * 7, 2 * 3 * 5 * 11))