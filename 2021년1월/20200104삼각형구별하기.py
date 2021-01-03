# https://codingdojang.com/scode/614?answer_mode=hide

def testTri(l1):
    if len(l1) != 3 or sum(l1) != 180 or min(l1) <= 0: return "삼각형이 아니다"
    if 90 in l1: return "직각삼각형"
    if max(l1) > 90: return "둔각삼각형"
    return "예각삼각형"

list1 = [[60, 60, 60],
    [30, 60, 90],
    [20, 40, 120],
    [0, 90, 90],
    [60, 70, 80],
    [40, 40, 50, 50]]


for l1 in list1:
    print(l1, '=', testTri(l1))
