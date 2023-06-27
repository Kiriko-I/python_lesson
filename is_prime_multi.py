N = int(input())
a = 2

for num in range(N):
    is_prime = True
    num = int(input())
    if num == 1:
        is_prime = False
    else:
        for i in range(2, int(num**0.5) + 1):
            result = num % i
            if result == 0:
                is_prime = False
    if is_prime == True:
        print("pass")
    else:
        print("failure")
