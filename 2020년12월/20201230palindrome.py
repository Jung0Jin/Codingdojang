# https://codingdojang.com/scode/562?answer_mode=hide

answer = []
for i in range(999,99,-1):
    for j in range(999,99,-1):
        if str(i*j) == str(i*j)[::-1]:
            answer.append(i*j)

# print(answer)
print(max(answer))
