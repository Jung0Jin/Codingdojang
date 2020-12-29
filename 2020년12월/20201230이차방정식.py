# https://codingdojang.com/scode/577?answer_mode=hide

def f(a, b, c):
    D = b*b-4*a*c
    if D > 0:
        x1 = round((-b-D**0.5)/2*a)
        x2 = round((-b+D**0.5)/2*a)
        print('x =', x1, ',', x2)
    elif D == 0:
        x = round(-b/2*a)
        print('중근입니다.')
        print('x =', x)
    else:
        print('허근입니다.')

a=int(input('a를 입력해 주세요.'))
b=int(input('b를 입력해 주세요.'))
c=int(input('c를 입력해 주세요.'))
f(a,b,c)