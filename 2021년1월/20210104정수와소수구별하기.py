# https://codingdojang.com/scode/685?answer_mode=hide

import re
p=re.compile('\D')
n=input()
if p.findall(n)!=["."] and p.findall(n)!=[]: print('math error')
else : print('integer') if float(n)==round(float(n)) else print('not integer')
