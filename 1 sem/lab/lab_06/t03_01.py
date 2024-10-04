# Голосні(модифікована)

string = input()

lst = []
for char in string:
     lst.append(char)
     if char in "aeiouy":
          lst.append(char)
# for char in lst:
#     print(char, end="")
lst_string = "".join(lst)
print(lst_string)
