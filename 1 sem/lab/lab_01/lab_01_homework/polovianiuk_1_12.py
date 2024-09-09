x1, y1, x2, y2, a = [float(a) for a in input().split()]

if not(-100 <= coord <= 100 for coord in [x1, y1, x2, y2]):
    print("Не згідно умові")
else:
    x = (a * x2 + x1) / (1 + a)
    y = (a * y2 + y1) / (1 + a)

    print(f"{x:.2f} {y:.2f}")
