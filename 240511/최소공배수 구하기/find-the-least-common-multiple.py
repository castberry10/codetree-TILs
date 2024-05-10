n, m = map(int, input().split())

# a가 b보다 크다는 전제
def gcd(a, b):
    if b > a:
        a, b = b,a 
    if a % b == 0:
        return b
        
    return gcd(b, a % b)

print(m * n // gcd(n, m))