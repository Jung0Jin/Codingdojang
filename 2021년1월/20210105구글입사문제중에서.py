# https://codingdojang.com/scode/393?answer_mode=hide

'''
count = 0
for i in range(1, 10001):
    for j in str(i):
        if j == '8':
            count += 1
print(count)
'''

print(str(list(range(1, 10001))).count('8'))