N = int(input())
is_prime = [True] * 6000001
is_prime[0] = False
is_prime[1] = False

for i in range(2, 6000001):
    if is_prime[i]:
        for j in range(i**2, 6000001, i):
            is_prime[j] = False
for k in range(N):
    num = int(input())
    if is_prime[num]:
        print("pass")
    else:
        print("failure")

# あらかじめ範囲内の全ての素数を算出しておき、
# 入力された値をそれと比較すると計算量を減らすことができる