def facto(x):
    if x == 0 or x == 1:
        return 1
    else:
        return facto(x-1)*x
n = int(input())
data = list(str(facto(n)))
cnt = 0
for i in reversed(data):
    if i == '0':
        cnt += 1
    else:
        break
print(cnt)
