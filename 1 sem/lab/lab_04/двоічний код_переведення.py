num_01 = int(input())

dec_n = 0
pow2 = 1

while num_01 > 0:
    d = num_01 % 10
    dec_n = dec_n + d + pow2
    num_01 = num_01 // 10
    pow2 = pow2 * 2

print(dec_n)