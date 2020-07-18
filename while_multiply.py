a = [8, 19, 4]
b = [9, 1, 33]
c = []
n = 0
while n != 3:
    m = 0
    while m != 3:
        c.append(a[n] * b[m])
        m += 1
    n += 1
print(c)