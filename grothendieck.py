grothendieck = 57
is_prime = True

for i in range(2, 57):
    if grothendieck % i == 0:
        is_prime = False
        print("NO")
        break
if is_prime:
    print("YES")