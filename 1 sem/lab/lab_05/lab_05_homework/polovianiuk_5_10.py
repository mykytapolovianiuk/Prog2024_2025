n = int(input())
first_array = list(map(int, input().split()))

m = int(input())
second_array = list(map(int, input().split()))

result = []

for num in first_array:
    if num not in second_array:
        result.append(num)

print(len(result))
print(" ".join(map(str, result)))