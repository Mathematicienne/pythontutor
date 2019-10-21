n, m = input().split()
a = []
for i in range(int(n)):
    a.append([])
    for j in range(int(m)):
        if not((j + i % 2) % 2):
            a[i].append('.')
        else:
            a[i].append('*')
    print(' '.join(a[i]))

