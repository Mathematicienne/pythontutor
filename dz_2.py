vod = input("VVod: ")

for i in ["+", "-", "*", "/", "**", "//"]:
    zn = vod.find(i)
    if zn != -1:
        break
x = float(input())
y = float(input())
znaki = {
    "+": x + y,
    "*": x * y,
    "/": x / y,
    "-": x - y,
    "**": x ** y,
    "//": x // y
}
print(znaki[vod[zn]])
