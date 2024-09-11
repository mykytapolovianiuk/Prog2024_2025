def calculate(x, y):
    try:
        first = (x ** 2 - 2 * x * y + 4 * y ** 2) / (x + 5)
        last = (3 * x ** 2 - y ** 2) / (y - 7)
        finalResult = first + last
        return print(f"{finalResult:.3f}")

    except ZeroDivisionError:
        return "Ділення на нуль!"

x, y = [float(a) for a in input().split()]

finalResult = calculate(x, y)

