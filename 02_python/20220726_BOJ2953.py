# BAEKJOON 2953
# Q) 참가자들이 얻은 점수 합산 중 가장 최고점만 출력

# 참가자 점수 합계 담을 리스트 선언
#score_total = []

# 참가자 점수 합계를 차례로 리스트에 추가
#for i in range(5):
#    score1, score2, score3, score4 = map(int, input().split())
#    score_total.append(score1 + score2 + score3 + score4)

# 가장 합계가 높은 값 구하기
#result = max(score_total)

# 최고 합계의 index 번호 구하기
# 단, 리스트 index는 0부터 시작하여 +1로 참가자 번호 맞춰주기
#num = score_total.index(result) + 1

# 결과 출력
#print(num, result)


win = 0     #우승자 초기화
total = 0   #총점 초기화
for i in range(5):  #입력값이 5줄 나오게하기.
    a, b, c, d = map(int,input().split())  #입력값
    if total < a + b + c + d:   # 총점이 현재는 0이라면
        win = i + 1             # 초기화값이 0이라서 i에 1을 더해줌. 사람들 번호주기
        total = a + b + c + d   # 총점 구하기
print(win ,total)