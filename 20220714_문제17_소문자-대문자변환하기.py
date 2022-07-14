# 문제17
# 소문자로 구성된 문자열 word가 주어질때 모두 대문자로 바꾸어 표현
# .upper(), .swapcase() 메서드 사용 금지
# Input : banana
# output : BANANA
# 추가 테스트 케이스: aeiou # 5 zxcvb # 0

# print(ord("A")) => 65
# print(ord("a")) => 97
# print(ord("B")) => 66
# print(ord("b")) => 98

word = 'banana'

for i in word:
    print(chr(ord(i)-32),end='')