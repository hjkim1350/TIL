# 문제14
# 문자열 word가 주어질 때, 해당 문자열에서 a 개수를 구하세요.
# count() 메서드 사용 금지
# Input : apple
# output : 1
# 추가 테스트 케이스: banana # 3 kiwi # 0

word ='apple'
cnt = 0

for i in word:
    if i == 'a':
        cnt += 1

print(cnt)

print ('a' in word) # True, False로 출력