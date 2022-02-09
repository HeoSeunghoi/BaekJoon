from collections import deque
n, k = map(int,input().split())
dp = [float('inf') for x in range(200001)]
dp[n] = 0
que = deque()
que.append(n)
while que:
    cur = que.popleft()
    if cur+1 < 110000 and dp[cur+1] > dp[cur]+1:
        dp[cur+1] = dp[cur]+1
        que.append(cur+1)
    if cur-1 >= 0 and dp[cur-1] > dp[cur]+1:
        dp[cur-1] = dp[cur]+1
        que.append(cur-1)
    if cur*2 < 110000 and dp[cur*2] > dp[cur]+1:
        dp[cur*2] = dp[cur]+1
        que.append(cur*2)
print(dp[k])
