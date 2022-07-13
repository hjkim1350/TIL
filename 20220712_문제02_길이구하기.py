# 문자열 word의 길이를 구하라

word = input("길이를 구할 문자열을 입력하세요: ")
word_len = 0

for i in word:
    word_len += 1

print(word_len)