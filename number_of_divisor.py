import math

N = int(input())

prime_factors = []
for i in range(2, int(N ** 0.5) + 1):
    while N % i == 0:
        prime_factors.append(i)
        N //= i # 切り捨て除算
if N != 1:
    prime_factors.append(N)

num = []
a = 0
count = 1

for j in range(len(prime_factors)-1):
    if prime_factors[a] == prime_factors[a+1]:
        count += 1
    else:
        num.append(count+1)
        count = 1
    a += 1
if prime_factors == []:
    num.append(1)
else:
    num.append(count+1)

print(math.prod(num))  