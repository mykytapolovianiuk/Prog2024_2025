N = int(input())
arr = [int(i) for i in input().split()]

result = []

for num in arr:
    if num not in result:
        result.append(num)

print(" ".join(map(str, result)))
