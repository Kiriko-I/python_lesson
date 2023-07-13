N = int(input())
top = N
i = 2

while i <= N:
    if (top % i) == 0:
        print(i)
        top = top / i
    else:
        i += 1

# N = int(input())

# prime_factors = []
# for i in range(2, int(N ** 0.5) + 1):
#     while N % i == 0:
#         prime_factors.append(i)
#         N //= i

# if N != 1:
#     prime_factors.append(N)

# for a in prime_factors:
#     print(a)