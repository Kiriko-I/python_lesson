N = int(input())
a = 2
is_prime = True

if N % a == 0:
    is_prime = False
else:
    fermat = a ** (N - 1) % N
    if fermat != 1:
        is_prime = False

if is_prime:
    print("YES")
else:
    print("NO")