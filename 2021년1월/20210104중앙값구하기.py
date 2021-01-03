# https://codingdojang.com/scode/611?answer_mode=hide

import statistics

test =[[7,9,14],[24, 31, 35, 49],[17,37,37,47,57]]

for i in range(len(test)):
    print(test[i],'=',statistics.median(test[i]))
