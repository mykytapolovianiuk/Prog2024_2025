n = int(input())
numbers = list(map(int, input().split()))

minimum = numbers[0]

for i in range(1, n):
    if numbers[i] < minimum:
        minimum = numbers[i]

print(minimum)