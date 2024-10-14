def caesar_decrypt(ciphertext, k):
    decrypted_text = ""

    for char in ciphertext:
        decrypted_char = chr((ord(char) - ord('A') - k) % 26 + ord('A'))
        decrypted_text += decrypted_char

    return decrypted_text


ciphertext = input()
k = int(input())

print(caesar_decrypt(ciphertext, k))