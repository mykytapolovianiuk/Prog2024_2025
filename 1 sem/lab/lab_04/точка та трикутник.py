xo, yo, xa, ya, xb, yb, xc, yc = map(int, input().split())

area_ABC = abs((xa * (yb - yc) + xb * (yc - ya) + xc * (ya - yb)) / 2)

area_OAB = abs((xo * (ya - yb) + xa * (yb - yo) + xb * (yo - ya)) / 2)
area_OBC = abs((xo * (yb - yc) + xb * (yc - yo) + xc * (yo - yb)) / 2)
area_OCA = abs((xo * (yc - ya) + xc * (ya - yo) + xa * (yo - yc)) / 2)

if area_ABC == area_OAB + area_OBC + area_OCA:
    result = 1
else:
    result = 0

print(result)

