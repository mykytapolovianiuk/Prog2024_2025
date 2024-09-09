x, y = [float(a) for a in input().split()]

squaredX = x * x
squaredY = y * y

print(float((squaredX - 2  * x * y + squaredY / x + 5) + 3 * squaredX - squaredY / y - 7))

