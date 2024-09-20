n = int(input())
current_number = 1
count = 0
result = ""

while count < n:
    if current_number % 2 != 0 and current_number % 3 != 0 and current_number % 5 != 0:
        if count == 0:
            result += str(current_number)
        else:
            result += " " + str(current_number)
        count += 1
    current_number += 1
print(result)
