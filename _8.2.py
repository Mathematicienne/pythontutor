def power(a, n):
    a1 = 1
    if n > 0:
        for i in range(n):
            a1 *= a
    elif n < 0:
        a = 1/a
        for i in range(-n):
            a1 *= a
    return(a1)
a = float(input())
n = int(input())
print(power(a, n))

