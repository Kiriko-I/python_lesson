n = int(input())

is_prime = True

if n == 1:
    is_prime = False
else:
    for i in range(2, int(n**0.5) + 1):
        result = n % i
        if result == 0:
            is_prime = False

if is_prime:
    print("YES")
else:
    print("NO")