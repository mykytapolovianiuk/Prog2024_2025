ones = [
    "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
    "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
    "eighteen", "nineteen"
]

tens = [
    "", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"
]

num = int(input())

if num == 0:
    print(ones[0])

result = []

if num >= 100:
    result.append(ones[num // 100] + " hundred")
    num %= 100

if num >= 20:
    result.append(tens[num // 10])
    num %= 10

if 0 < num < 20:
    result.append(ones[num])

print(' '.join(result))
