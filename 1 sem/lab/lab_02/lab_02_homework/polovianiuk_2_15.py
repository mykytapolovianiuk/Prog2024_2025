a, b, c = [int(x) for x in input().split()]
D = b ** 2 - 4 * a * c

if D < 0:
    print("No roots")
elif D == 0:
    x = -b // (2 * a)
    print(f"One root: {x}")
else:
    x1 = (-b + int(D ** 0.5)) // (2 * a)
    x2 = (-b - int(D ** 0.5)) // (2 * a)

    if x1 > x2:
        x1, x2 = x2, x1

    print(f"Two roots: {x1} {x2}")
