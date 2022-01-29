lst = [x for x in range(2*123456+1)]
check_num = 2
def sosoo(n):
    for i in range(check_num,n):
        if lst[i] == 0:
            continue
        for j in range(i*i, 2*n+1, i):
            lst[j] = 0

def print_cnt(n):
    cnt = 0
    for i in range(n+1, 2*n+1):
        if lst[i] != 0:
            cnt += 1
    print(cnt)

while True:
    x = int(input())
    if x == 0:
        break
    else:
        sosoo(x)
        print_cnt(x)
