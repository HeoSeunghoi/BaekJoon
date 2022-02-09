n = int(input())
lst = list(map(int,input().split()))
dp = [0 for x in range(n)]
dp[0] = lst[0]
m = dp[0]
for i in range(1, n):
    dp[i] = max(dp[i-1]+lst[i],lst[i])
    if dp[i] > m:
        m = dp[i]
print(m)
