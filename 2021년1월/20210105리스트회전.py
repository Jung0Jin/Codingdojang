# https://codingdojang.com/scode/400?answer_mode=hide

# array = list(input().split())

# n = int(array[0])
# array = array[1:]
# answer = array[:]

# if n % len(answer) != 0:
#     n = n % len(answer)

# if n == 0:
#     print(answer)

# elif n > 0:
#     answer[0:n] = array[-n:]
#     answer[n:] = array[:-n]
#     print(answer)

# else:
#     answer[-n:] = array[:-n]
#     answer[:len(array)+n] = array[-n:]
#     print(answer)

data = input('회전수와 문자열을 입력하세요. : ').split()
rn = int(data.pop(0)) % len(data)
print(' '.join([(data*3)[len(data) + i - rn] for i in range(len(data))]))
