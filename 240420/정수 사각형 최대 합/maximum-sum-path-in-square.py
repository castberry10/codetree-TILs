n = int(input())
map_ = list()
dp = list()
for i in range(n):
    map_.append(list(map(int, input().split())))
    dp.append([0] * n)

dp[0][0] = map_[0][0]
for i in range(n): # y
    for j in range(n): # x
        if i != n-1: # 맨 아래가 아니라면 
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + map_[i + 1][j])
        if j != n-1: # 맨 오른쪽이 아니라면
            dp[i][j + 1] = max(dp[i][j + 1], dp[i][j] + map_[i][j + 1])
print(dp[n-1][n-1])