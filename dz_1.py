mas = []
for x in range(1000):
    mas.append(x)
mas = list(filter(lambda num: not num % 3 or not num % 5, mas))
print(mas)
print(sum(mas))
