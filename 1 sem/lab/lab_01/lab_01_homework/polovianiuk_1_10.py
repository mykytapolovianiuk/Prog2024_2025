s = 50.2655
r = 5
pi = 3.14

outRSquared = r * r
innRSquared = outRSquared - (s / pi)

if innRSquared < 0:
    print('Неможливо')
else:
    innRSquared = innRSquared**0.5

    print(f"{innRSquared:.2f}")









