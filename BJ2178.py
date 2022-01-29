import sys
from collections import deque
def check(lst, x, y):
    xp = [-1, 1, 0, 0]
    yp = [0, 0, -1, 1]
    result = []
    for i in range(4):
        if lst[x+xp[i]][y+yp[i]] == '1':
            result.append((x+xp[i], y+yp[i]))
    return result

n, m = map(int, sys.stdin.readline().split())
lst = [['0' for i in range(m+2)]]
dp = []
for i in range(1, n+1):
    lst.append(['0'])
    lst[i] += list(sys.stdin.readline())
    lst[i].append('0')
lst.append(['0' for i in range(m+2)])

for i in range(n+2):
    dp.append([10001 for x in range(m+2)])

cur = (1,1)
dp[cur[0]][cur[1]] = 1
neighbor = []
que = deque()
que.append(cur)
visit = [cur]
while que:
    cur = que.popleft()
    neighbor = check(lst, cur[0], cur[1])
    for i in neighbor:
        if i not in visit:
            dp[i[0]][i[1]] = min(dp[cur[0]][cur[1]]+1, dp[i[0]][i[1]])
            que.append(i)
            visit.append(i)
print(dp[n][m])
