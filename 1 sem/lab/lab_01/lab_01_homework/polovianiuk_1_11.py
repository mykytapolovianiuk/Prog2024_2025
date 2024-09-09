a, b, c, d, f = [int(x) for x in input().split()]

if 0 < a <= 100 and 0 < b <= 100 and 0 < c <= 100 and 0 < d <= 100 and 0 < f <= 100:
    s1 = (a + b + f) / 2
    area1 = (s1 * (s1 - a) * (s1 - b) * (s1 - f)) ** 0.5

    s2 = (c + d + f) / 2
    area2 = (s2 * (s2 - c) * (s2 - d) * (s2 - f)) ** 0.5

    total_area = area1 + area2

    print(f"{total_area:.4f}")