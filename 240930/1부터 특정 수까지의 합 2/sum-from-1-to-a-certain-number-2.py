def function(n):
    if n == 0:
        return 0
    return n + function(n-1)
a = int(input())
print(function(a))