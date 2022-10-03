n,m = map(int,input().split())

def gcd(a,b):
    if a==0:
        return b
    else:
        return gcd(b%a,a)

gcd_n = gcd(n,m)

lcm_n = int(n/gcd_n * m/gcd_n * gcd_n)
print(gcd_n)
print(lcm_n)
