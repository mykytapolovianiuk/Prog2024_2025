s, r = [float(x) for x in input().split()]
pi = 3.14

outRSquared = r * r
innRSquared = outRSquared - (s / pi)

if innRSquared < 0:
    print('Неможливо')
else:
    innRSquared = innRSquared**0.5

    print(f"{innRSquared:.2f}")









