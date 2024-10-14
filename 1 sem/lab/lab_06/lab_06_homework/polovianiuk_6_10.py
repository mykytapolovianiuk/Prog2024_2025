def double_letters(input_str):
    result = ''
    for char in input_str:
        if char.isalpha():
            result += char * 2
        else:
            result += char
    return result

input_str = input()
print(double_letters(input_str))