number = int(input())

a = 0
b = 1

for i in range(number):
    c = a + b
    a = b
    b = c
    print(c)
