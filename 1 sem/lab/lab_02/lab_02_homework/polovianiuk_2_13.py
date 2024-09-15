a, b, c = [int(x) for x in input().split()]

if ((a == b) and (b == c)):
    print("1")
elif ((a == b) or (a == c) or (b == c)):
    print("2")
else:
    print("3")
