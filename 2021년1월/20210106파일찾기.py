# https://codingdojang.com/scode/404?answer_mode=hide

import os

def func(dirname):
    for root, dirs, files in os.walk(dirname):
        for name in files:
            if '.txt' in name:
                f = open(os.path.join(root, name), 'r')
                txt = f.read()
                if 'LIFE IS TOO SHORT' in txt:
                    print(name)
                f.close()

func('.')