import sys
n = int(sys.stdin.readline())
lst = []
dp = []
for i in range(n):
    data = list(map(int,sys.stdin.readline().split()))
    lst.append(data)
    dp.append([0,0,0])
    
dp[0] = lst[0]
for i in range(1, n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + lst[i][0]
    dp[i][1] = min(dp[i-1][2], dp[i-1][0]) + lst[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + lst[i][2]
print(min(dp[n-1]))
