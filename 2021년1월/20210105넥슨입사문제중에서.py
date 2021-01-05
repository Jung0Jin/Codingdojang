# https://codingdojang.com/scode/365?answer_mode=hide

'''
def d(n):
    temp = []
    temp.append(int(n))
    for number in str(n):
        temp.append(int(number))
    return sum(temp)

count = 1
array = []
while True:
    array.append(d(count))
    if count == 5000: break
    count += 1

answer = 0
for i in list(set(array)):
    if i < 5000:
        answer += i
print(answer)
'''

print(sum(set(range(1, 5000)) - {x + sum([int(a) for a in str(x)]) for x in range(1, 5000)}))
