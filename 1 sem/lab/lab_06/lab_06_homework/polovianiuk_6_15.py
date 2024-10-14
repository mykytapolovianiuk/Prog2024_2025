def clean_word(w):
    clean = ""
    for ch in w:
        if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z') or ('0' <= ch <= '9') or ch in ["-"]:
            clean += ch.lower()
    return clean


def is_palindrome(w):
    w = w.replace('-', '').replace("'", '')
    return w == w[::-1]


# Main
sentence = input()

words = sentence.split()

champion = -1
max_len = -1

for i in range(len(words)):
    clean = clean_word(words[i])

    if is_palindrome(clean) and len(clean) > max_len:
        max_len = len(clean)
        champion = i + 1

print(champion)