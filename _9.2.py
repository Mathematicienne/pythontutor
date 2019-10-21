n = int(input())
a = [['.'] * n for i in range(n)]
s = n // 2
b = 0
for i in range(n):
    if i < s:
        a[i][0 + i] = '*'
        a[i][s] = '*'
        a[i][-1 - i] = '*'
        print(' '.join(a[i]))
    elif i == s:
        a[i] = ['*'] * n
        print(' '.join(a[i]))
    else:
        b += 1
        a[i][s - b] = '*'
        a[i][s] = '*'
        a[i][s + b] = '*'
        print(' '.join(a[i]))
