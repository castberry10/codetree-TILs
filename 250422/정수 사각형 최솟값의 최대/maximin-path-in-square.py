n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
memo = [[1e9 for i in range(n)] for j in range(n) ]
for i in range(n):
    for j in range(n):
        maxlist = []
        if i != 0:
            maxlist.append(grid[i-1][j])
        if j != 0:
            maxlist.append(grid[i][j-1])
        if maxlist:
            grid[i][j] = min(max(maxlist), grid[i][j])
print(grid[n-1][n-1])