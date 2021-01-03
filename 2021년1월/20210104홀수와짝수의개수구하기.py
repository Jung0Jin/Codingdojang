# https://codingdojang.com/scode/613?answer_mode=hide

def count_odd_n_even(lst):
    odd = len([x for x in lst if x % 2 == 1])
    return (odd, len(lst) - odd)

print(count_odd_n_even([3, 4, 5, 6, 7]))