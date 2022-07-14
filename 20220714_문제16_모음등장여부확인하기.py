# 문제16
# 문자열 word가 주어질 때, 해당 문자열에서 모음의 갯수 출력
# count() 메서드 사용 금지
# Input : apple
# output : 2
# 추가 테스트 케이스: aeiou # 5 zxcvb # 0

word = 'apple'
cnt = 0

for i in word:
    if i in ('a', 'e', 'i', 'o', 'u'):
        cnt += 1

print(cnt)

#강사님 풀이 ------------------------------------
word1 = 'apple'
cnt1 = 0

for word1 in 'aeiou':
    cnt1 += 1

print(cnt1)