# https://codingdojang.com/scode/646?answer_mode=hide

words = input().split()

int_word = []
str_word = []

for word in words:
    temp = []
    for alphabet in word:
        try:
            int_word.append(int(alphabet))
        except:
            temp.append(alphabet)
    str_word.append(temp)

print(int_word)
print(str_word)