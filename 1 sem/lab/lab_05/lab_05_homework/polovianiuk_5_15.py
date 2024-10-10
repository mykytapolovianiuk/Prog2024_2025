n = int(input())
arr = [int(i) for i in input().split()]

max_val = max(arr)
min_val = min(arr)

for i in range(n):
    if arr[i] == max_val:
        arr[i] = min_val
    elif arr[i] == min_val:
        arr[i] = max_val

print(" ".join(map(str, arr)))
