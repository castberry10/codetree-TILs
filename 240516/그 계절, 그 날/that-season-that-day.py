def isDbssus(Y):
    if Y % 4 == 0 and Y % 100 == 0 and Y % 400 == 0:
        return 29
    if Y % 4 == 0 and Y % 100 == 0:
        return 28
    if Y % 4 == 0:
        return 29
    return 28

def whatSeason(M):
    if 3<= M <= 5:
        return "Spring"
    if 6<= M <= 8:
        return "Summer"
    if 9<= M <= 11:
        return "Fall"
    return "Winter"
    
def isdate(Y, M, D):
    date31D = [1, 3, 5, 7, 8, 10, 12]
    if M in date31D:
        if D <= 31:
            return True
        else:
            return False
    if M == 2:
        if D <= isDbssus(Y):
            return True
        else:
            False
    if M <= 30:
        return True
    else:
        return False

Y, M, D = map(int, input().split())
day31 = [1, 3, 5, 7, 8, 10, 12]
if isdate(Y, M, D):
    print(whatSeason(M))
else:
    print(-1)