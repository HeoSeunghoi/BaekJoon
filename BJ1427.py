def print_num(dic, n):
    for i in range(dic[n]):
        print(n,end='')
lst = list(input())
dic = {}
for i in lst:
    if i in dic.keys():
        dic[i] += 1
    else:
        dic[i] = 1

for i in range(9, -1, -1):
    if str(i) in dic.keys():
        print_num(dic,str(i))
