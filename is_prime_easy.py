n = int(input())

is_prime = True

if n == 1:
    is_prime = False
else:
    for i in range(2, (n - 1)):
        result = n % i
        if result == 0:
            is_prime = False
            # break 不要

if is_prime:
    print("YES")
else:
    print("NO")