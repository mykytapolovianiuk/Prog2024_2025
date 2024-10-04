n = int(input())

nums = []
for _ in range(n):
    num = int(input())
    nums.append(num)

l, r = 0, n - 1
while l < r:
    nums[l], nums[r] = nums[r], nums[l]
    l += 1
    r -= 1
print(nums)