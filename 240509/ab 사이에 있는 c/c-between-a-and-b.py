a, b, c = map(int, input().split())
result = False
for i in range(a, b +1):
    if c % i == 0:
        result = True
if result:
    print("YES")
else:
    print("NO")