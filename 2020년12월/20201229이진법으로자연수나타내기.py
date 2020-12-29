# https://codingdojang.com/scode/556?answer_mode=hide

n = int(input())

answer = []
if n == 1:
    answer = [1]
else:
        
    while True:
        answer.append(n%2)
        n = n // 2
        if n == 1:
            answer.append(n)
            break
    answer.reverse()

print(answer)