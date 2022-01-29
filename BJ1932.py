import sys
n = int(sys.stdin.readline())
data_set = []
dp = []
for i in range(n):
    line = list(map(int,sys.stdin.readline().split()))
    data = []
    dp_part = []
    for x in line:
        data.append(x)
        dp_part.append(0)
    data_set.append(data)
    dp.append(dp_part)
    
dp[0] = data_set[0]
for i in range(1, n):
    for j in range(len(dp[i])):
        if j == 0:
            dp[i][j] = data_set[i][0] + dp[i-1][0]
        elif j == len(dp[i])-1:
            dp[i][j] = data_set[i][j] + dp[i-1][j-1]
        else:
            dp[i][j] = data_set[i][j] + max(dp[i-1][j], dp[i-1][j-1])
print(max(dp[n-1]))
