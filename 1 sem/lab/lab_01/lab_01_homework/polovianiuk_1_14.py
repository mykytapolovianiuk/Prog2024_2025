def calculate(x, y):
    try:
        first = (2 * x * y) / ((x**2 + y**2)**0.5)
        last = (x + y - 1)**2 / (x * y)
        finalResult = first - last
        return print(f"{finalResult:.3f}")

    except ZeroDivisionError:
        return "Ділення на нуль!"

x, y = [float(a) for a in input().split()]

finalResult = calculate(x, y)