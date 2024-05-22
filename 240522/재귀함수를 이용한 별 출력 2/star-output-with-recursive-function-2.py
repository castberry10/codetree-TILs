n = int(input())
def sp(n):
    rsprint(n, 0)
    sprint(n, n)
# a가 기준
def sprint(a, b):
    if b <= 0:
        return
    for i in range(a - b + 1):
        print("*", end=" ")
    print()
    return sprint(a, b-1)

def rsprint(a, b):
    if b >= a:
        return
    for i in range(a - b):
        print("*", end=" ")
    print()
    return rsprint(a, b+1)

sp(n)