# https://codingdojang.com/scode/700?answer_mode=hide

count = 0
while True:
    if (count + 6) % 4 == 2:
        count += 1
        print(count)
        count += 1
        print(count)
    elif (count + 6) % 4 == 1:
        count += 1
        print(count)
        count += 1
        print(count)
        count += 1
        print(count)
    elif (count + 6) % 4 == 3:
        count += 1
        print(count)
    if count == 30:
        break
    for n in range(3):
        my_number = int(input())
        if my_number == count + 1:
            count = my_number
        elif my_number == 0:
            pass

print("졌습니다..")
