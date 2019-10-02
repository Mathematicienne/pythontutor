def power(a, n):
    if n > 1:
        a *= power(a, n-1)
    return a
print(power(float(input()), int(input())))
