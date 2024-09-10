n = int(input())
line = []

for i in range(n):
    a, b = map(int, input().split())
    line.append((a, 1))
    line.append((b, -1))
line.sort()

maxvar = 0
var = 0 
index = 0 
maxindex = 0 
for i in range(len(line)):
    var += (line[i])[1]
    if var > maxvar:
        maxvar = var
        maxindex = i
print(maxvar)