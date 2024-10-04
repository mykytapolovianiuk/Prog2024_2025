# Голосні

string = input()

count = 0
for char in string:
    if char in ("A", "E", "I", "O", "U", "Y"):
        count += 1

print(count)