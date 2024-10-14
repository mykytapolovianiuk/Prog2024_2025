def is_prime(N):
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            return False
    return True
def is_square(N):
    n = (N ** 0.5)
    n_int = int(n)
    n_int_square = n_int ** 2
    return n_int_square == N

def is_pow5(N):
    while N > 1:
        if N % 5 != 0:
            return False
        n = n // 5
    return True


# Main

nums = [int(el) for el in input().split()]
primes = []
pow5s = []
squares = []
for n in nums:
    if is_pow5(n):
        pow5s.append(n)
    if is_prime(n):
        primes.append(n)
    if is_square(n):
        squares.append(n)

print(primes)
print(squares)
print(pow5s)