from collections import deque
n, k = map(int, input().split())
lst = deque([x for x in range(1, n+1)])
result = []
cnt = 1
while lst:
    x = lst.popleft()
    if cnt==k:
        result.append(x)
        cnt = 1
    else:
        lst.append(x)
        cnt += 1
print("<"+", ".join([str(x) for x in result])+">")
