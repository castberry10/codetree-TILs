a, b, c = map(int, input().split())

l = list((a, b, c))
l.sort()
print(l[1])