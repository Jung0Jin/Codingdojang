# https://codingdojang.com/scode/584?answer_mode=hide

# def LCM(x, y):
#     if x<y:
#         max = y
#     else:
#         max = x
#     for i in range(max, (x*y)+1):
#         if i % x == 0 and i % y == 0:
#             answer = i
#             break
#     return answer

# 최소공배수 구해서 하려다가 문제 포기함 ㅠ_ㅠ

elem=[2]
for i in range(3, 20):
    for j in range(2, i):
        if i % j == 0:
            break
        elif j == i-1:
            elem.append(i)

answer = 1
for i in elem:
    while True:
        if i * i > 20:
            answer *= i
            break
        i *= i

print(answer)

### 답변자가 20이하의 소수를 구하여서 이들의 20이하의 최댓값을 판단, 그들을 곱하였다고 하였다.

# def minvalue():

#     i = 0
#     while True:
#         i += 1
#         if (i % 1 == 0 and i % 2 ==0 and i % 3 == 0 and i % 4 == 0 and i % 5 == 0 and i % 6 == 0 and i % 7 == 0 and i % 8 == 0 and i % 9 == 0 and i % 10 == 0 and i % 11 == 0 and i % 12 == 0 and i % 13 == 0 and i % 14 == 0 and i % 15 == 0 and i % 16 == 0 and i % 17 == 0 and i % 18 == 0 and i % 19 == 0 and i % 20 == 0):
#             print(i)
#             break

# minvalue()

# 232792560
# Wall time: 1min 10s
