a, b, c, d = map(int, input().split())

if a > b:
    a, b = b, a
if c > d:
    c, d = d, c

unique_products = []

for i in range(a, b + 1):
    for j in range(c, d + 1):
        product = i * j
        if product not in unique_products:
            unique_products.append(product)

print(len(unique_products))