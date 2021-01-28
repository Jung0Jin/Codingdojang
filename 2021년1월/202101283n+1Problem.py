# https://codingdojang.com/scode/409?answer_mode=hide

def find_max_cycle(i, j):
    cycle_list = []
    for num in range(i, j+1):
        array =[]
        while True:
            array.append(num)
            if num % 2 == 0:
                num = num // 2
                continue
            
            else:
                if num == 1:
                    break

                num = (num * 3) + 1
                continue
        cycle_list.append(len(array))

    return print(i, j, max(cycle_list))

find_max_cycle(1, 10)
find_max_cycle(100, 200)
find_max_cycle(201, 210)
find_max_cycle(900, 1000)