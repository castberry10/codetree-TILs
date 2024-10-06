import sys
input = sys.stdin.readline
n = int(input())

ls = []
for i in range(n):
    ls.append(int(input()))

mid = sum(ls) // len(ls)
abscnt = 0
for i in ls:
    abscnt += abs(mid - i)
print(abscnt // 2)