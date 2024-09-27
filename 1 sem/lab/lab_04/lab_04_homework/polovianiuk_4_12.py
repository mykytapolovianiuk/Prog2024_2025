sum_even = 0
while True:
    elem = int(input())
    if elem == 0:
        break
    if elem % 2 == 0:
        sum_even += elem

print(sum_even)
