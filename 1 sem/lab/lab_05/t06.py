n = int(input())

nums = [float(i) for i in input().split()]

count = 0
suma = 0
for i in range(2, n , 3):
    if nums[i] > 0:
        suma += nums[i]
        count += 1

print('{} {:.2f}'.format(count, suma))