def add_world(word):
    print(word + 'World')

add_world('Hello')

def calculator(result):
    print(result)
calculator(8 % 2)

names = ["太郎", '二郎', '三郎']
for name in names:
    print(name)

i = 0
while i <= 100:
    print(i)
    if i == 7:
        break
    i += 1

def if_test(num):
    if num > 100:
        print('100より大きい')
    elif num > 50:
        print('100未満50より大きい')
    elif num > 0:
        print('50未満0より大きい')
    elif num == 0:
        print('0と等しい')
    else:
        print('0より小さい')
if_test(2000)
if_test(75)
if_test(0)
if_test(-100)
    
print(type(False))

for i, j in zip(['国語', '算数', '英語'], [80, 80, 50]):
    print(f'{i} : {j}')

with open('sample.txt') as f:
    print(f.read())