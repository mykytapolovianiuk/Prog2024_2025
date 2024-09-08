x1, y1, x2, y2, x3, y3 = [float(a) for a in input().split()]
d1 = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
d2 = ((x3 - x2)**2 + (y3 - y2)**2)**0.5
d3 = ((x1 - x3)**2 + (y1 - y3)**2)**0.5
pr = d1 + d2 + d3

pp = pr / 2
pl = (pp * (pp - d1) * (pp - d2) * (pp - d3))**0.5

print(f"{pr:.4f}, {pl:.4f}")