n = int(input())

nums = [int(i) for i in input().split()]

for num in nums:
    if num >= 0:
        print(num + 2, end=" ")
    else:
        print(num, end=" ")