n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i != 0 and j != 0:
            grid[i][n - 1 - j] += min(grid[i-1][n - 1 - j], grid[i][n-1-j+ 1])
        elif i != 0:
            grid[i][n - 1 - j] += grid[i-1][n - 1 - j] 
        elif j != 0:
            grid[i][n - 1 - j] += grid[i][n - 1 - j + 1]

print(grid[n-1][0])
