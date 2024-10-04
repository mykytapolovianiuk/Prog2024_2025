n = int(input())

nums = []
for _ in range(n):
    num = int(input())
    nums.append(num)

reverse_nums = []
for i in range(n-1, -1, -1):
    reverse_nums.append(nums[i])

print(*reverse_nums)