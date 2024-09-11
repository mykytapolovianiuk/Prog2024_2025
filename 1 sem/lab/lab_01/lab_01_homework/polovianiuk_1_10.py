s, r = [float(x) for x in input().split()]
pi = 3.141592653589793

outRSquared = r * r
innRSquared = outRSquared - (s / pi)

if innRSquared < 0:
    print('Неможливо')
else:
    innR = innRSquared ** 0.5
    print(f"{innR:.2f}")









