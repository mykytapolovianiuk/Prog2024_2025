# Пиріжки

uah, penny, amount = [int(x) for x in input().split()]

if 0 <= uah <= 100 and 0 <= penny <= 100 and 0 <= amount <= 100:
    total_uah = uah * amount
    total_penny = penny * amount

    total_uah += total_penny // 100
    total_penny = total_penny % 100

    print(total_uah, total_penny)


