# https://codingdojang.com/scode/593?answer_mode=hide

from math import gcd

n,m = map(int, input().split())
print(n * m // gcd(n, m)**2)
