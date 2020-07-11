a = int(input())
b = int(input())
c = int(input())
if a % 2 != 0:
    a += 1
if b % 2 != 0:
    b += 1
if c % 2 != 0:
    c += 1
print(int(a/2 + b/2 + c/2))
