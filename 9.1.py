text = input()
a = dict(zip(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
             [11, 12, 13, 14, 15, 21, 22, 23, 24, 25, 31, 32, 33, 34, 35, 41, 42, 42, 43, 44, 45, 51, 52, 53, 54, 55]))
for i in text:
    x = x[::] + str(a[i] // 10)
    y = y[::] + str(a[i] % 10)
C = x + y