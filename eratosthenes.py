N = int(input())

is_prime = ["YES"] * (N+1)
is_prime[0], is_prime[1] = "NO", "NO"

sq = int(N**0.5)

for i in range(sq+1):
    if is_prime[i] == "NO":
        continue # すでにNOの場合は次の数字の処理をするために先頭に戻る
    for j in range(i**2, N+1, i):
        is_prime[j] = "NO"
primes = []
for i, j in enumerate(is_prime): # なじみがないのでいつかrangeに直してみる
    if j == "YES":
        primes.append(i)
print(primes)
