# 문제15
# 문자열 word가 주어질 때, 해당 문자열에서 a가 처음 등장하는 위치 출력
# a가 없는 경우 -1 출력
# find(), index() 메서드 사용 금지
# Input : banana
# output : 1
# 추가 테스트 케이스: apple # 0 kiwi # -1

word ='apple'
cnt = 0

for i in word:
    if i == 'a':
        print('Input: apple >', cnt)
        break
    else:
        if cnt == len(word)-1:
            cnt = -1
            print('Input: apple >', cnt)
        else:
            cnt += 1

# 강사님 풀이-----------------------------------

word_new = 'kiwi'

for idx in range(len(word_new)):
    if word_new[idx] == 'a':
        print('강사님 풀이',idx)
        break
else:
    print('강사님 풀이', -1)



# 문제15 - 추가 문제
# 문자열 word가 주어질 때, 해당 문자열에서 a의 모든 위치 출력
# a가 없는 경우 -1 출력
# find(), index() 메서드 사용 금지
# Input : HappyHacking
# output : 1 6
# 추가 테스트 케이스: banana # 1 3 5 kiwi # 

word4 ='HappyHacking'
cnt4 = 0
cnts = []

for n in word4:
    if cnt4 <= len(word4)-1:
        if n == 'a':
            cnts.append(cnt4)
            cnt4 += 1
        else:
            cnt4 += 1

print (*cnts)

# 강사님 풀이-----------------------------------

word_new1 = 'kiwi'
result = []

for idx1 in range(len(word_new1)):
    if word_new[idx1] == 'a':
        result.append(idx1)
print(result)