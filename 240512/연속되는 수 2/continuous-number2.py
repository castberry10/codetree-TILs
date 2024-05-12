n = int(input())

li = []

for i in range(n):
    li.append(int(input()))

cnt = 0
for i in range(n-1):
    print(i)
    if li[i] != li[i+1]:
        cnt += 1
print(cnt)