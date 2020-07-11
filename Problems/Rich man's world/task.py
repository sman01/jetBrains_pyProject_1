n = int(input())
y = 0
while 50000 <= n < 700000:
    y += 1
    n = n * 1.071
print(y)
