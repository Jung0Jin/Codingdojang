# https://codingdojang.com/scode/591?answer_mode=hide

array = list(map(int, input().split(', ')))
test_array = array[:]

for i in array:
    test_array.remove(i)

    answer = 1
    for j in test_array:
        answer *= j
    print(answer)
    test_array.append(i)