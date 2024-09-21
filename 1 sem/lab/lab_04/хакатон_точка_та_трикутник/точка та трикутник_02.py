def triangle_area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2)

xo, yo, xa, ya, xb, yb, xc, yc = map(int, input().split())

area_ABC = triangle_area(xa, ya, xb, yb, xc, yc)
area_OAB = triangle_area(xo, yo, xa, ya, xb, yb)
area_OBC = triangle_area(xo, yo, xb, yb, xc, yc)
area_OCA = triangle_area(xo, yo, xc, yc, xa, ya)

print(1 if area_ABC == area_OAB + area_OBC + area_OCA else 0)
