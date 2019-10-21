n, m = input().split()
n = int(n)
m = int(m)
a = [input().split() for i in range(n)]
b = int(a[0][0])
x = 0
y = 0
for i in range(n):
    for j in range(m):
        k = int(a[i][j])
        if k > b:
            b = k
            x = i
            y = j
print(x, y)

