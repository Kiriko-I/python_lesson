N = int(input())

is_prime = ["YES"] * (N+1)
is_prime[0], is_prime[1] = "NO", "NO"

sq = int(N**0.5)

for i in range(sq+1):
    if is_prime[i] == "YES":
        for j in range(i**2, N+1, i):
            is_prime[j] = "NO"
            
primes = []
for i, j in enumerate(is_prime): # なじみがないのでいつかrangeに直してみる
    if j == "YES":
        primes.append(i)
if primes[-1] == N:
    print("YES")
else:
    print("NO")

# その数が素数かどうかを判定するプログラムの回答例

# is_prime = [True] * (N + 1)

# is_prime[0] = False
# is_prime[1] = False

# for i in range(2, N + 1):
#     if is_prime[i]:
#         for j in range(i * 2, N + 1, i):
#             is_prime[j] = False

# if is_prime[N]:
#     print("YES")
# else:
#     print("NO")