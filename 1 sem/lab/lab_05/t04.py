n = int(input())

nums = [int(i) for i in input().split()]

max_ = float("inf")

for num in nums:
    if num > max_:
        max_ = num
print(max_)

# print(max(nums))


