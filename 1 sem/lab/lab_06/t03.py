# Голосні

string = input()

result = ""
for char in string:
     result = result + char
     if char in "aeiouy":
          result += char
print(result)


