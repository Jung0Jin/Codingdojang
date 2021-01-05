# https://codingdojang.com/scode/397?answer_mode=hide

# while True:
#     n, m = input().split()
#     if n == '0' and m == '0':
#         break
#     count = 0
#     for i in range(len(n)):
#         if int(n[i]) + int(m[i]) >= 10:
#             count += 1

#     if count == 0:
#         print('No carry operation.')

#     else:
#         print(f'{count} carry operation.')

def getCarries(a, b):
    carry = 0
    cflag = 0
    for (a1, b1) in zip(a[::-1], b[::-1]):
        if (int(a1) + int(b1) + cflag > 9):
            carry = carry + 1
            cflag = 1
        else:
            cflag = 0

    return carry

res = list()
while 1:
    a, b = input().split(' ') 
    if a == '0': break
    res.append(getCarries('0' * len(b) + a, '0' * len(a) + b))

for carries in res:
    if carries == 0:
        print("No carry operation.")
    elif carries == 1:
        print("1 carry operation.")
    else:
        print("%d carry operations." % carries)
