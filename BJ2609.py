a, b = map(int, input().split())
m = a*b
while b != 0:
    r = a%b
    a = b
    b = r
print(a)
print(int(m/a))
