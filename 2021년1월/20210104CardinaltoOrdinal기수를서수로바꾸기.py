# https://codingdojang.com/scode/686?answer_mode=hide

def num(n):
    if n%10==1 and n%100!=11:
        return str(n)+"st"
    elif n%10==2 and n%100!=12:
        return str(n)+"nd"
    elif n%10==3 and n%100!=13:
       return str(n)+"rd"
    else:
        return str(n)+"th"

print (num(1))
print (num(11))
print (num(22))
print (num(12))
print (num(23))
print (num(13))
print (num(34))
print (num(101))
print (num(111))
print (num(112))
print (num(113))
print (num(114))