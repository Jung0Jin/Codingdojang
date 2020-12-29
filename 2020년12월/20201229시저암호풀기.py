# https://codingdojang.com/scode/555?answer_mode=hide

word = input()
n = int(input())

list_alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','n','m','o','p','q','r','s','t','u','v','w','x','y','z']
answer = []
for alphabet in word:
    answer.append(list_alphabet[list_alphabet.index(alphabet) + n])
print(answer)