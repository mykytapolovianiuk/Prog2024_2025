score = int(input())

if score >= 1 and score <= 3:
    print("Initial")
elif score >= 4 and score <= 6:
    print("Average")
elif score >= 7 and score <= 9:
    print("Sufficient")
else:
    print("High")