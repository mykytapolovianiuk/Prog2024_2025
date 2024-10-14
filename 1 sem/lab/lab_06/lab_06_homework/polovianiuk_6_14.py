def is_palindrome(s):
    s = s.replace(" ", "")

    if s == s[::-1]:
        return "YES"
    else:
        return "NO"


s = input()

print(is_palindrome(s))