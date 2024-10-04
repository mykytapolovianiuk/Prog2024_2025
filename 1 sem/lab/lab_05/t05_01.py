n = int(input())

nums = [int(i) for i in input().split()]

for i in range(n):
    if nums[i] >= 0:
        nums[i] += 2
print(*nums)