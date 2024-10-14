def is_prime(N):
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            return False
    return True

# Main

n = int(input())

for i in range(n, 2 * n - 1):
    if is_prime(i) and is_prime(i + 2):
        print(i, i + 2)