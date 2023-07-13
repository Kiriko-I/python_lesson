def fibonacci(n):
    a, b = 0, 1
    for k in range(n):
        a, b = b, a + b
    return a

print(fibonacci(int(input())))