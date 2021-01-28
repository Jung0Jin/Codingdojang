# https://codingdojang.com/scode/408?answer_mode=hide

def spair(S):
    dict = {}
    for (x, y) in zip(S[:-1], S[1:]):
        if not dict.get(y-x):
            dict[y-x] = [(x, y)]
        else:
            dict[y-x] = dict[y-x] + [(x,y)]

    return dict[min(dict.keys())]

S = [1, 3, 4, 8, 13, 17, 20]
print(spair(S))