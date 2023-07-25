N = int(input())
top = N
i = 2

while i <= N:
    if (top % i) == 0:
        print(i)
        top = top / i
    else:
        i += 1

if N == 1:
    print(1)