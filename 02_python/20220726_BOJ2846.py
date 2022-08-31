# BAEKJOON 2846
# Q) 입력값 첫째줄: 상근이가 측정한 높이 수이자 수열의 크기
# 입력값 둘째줄: 양의 정수로 구성된 수열
# 둘째줄 수열에서 연속으로 증가하는 값들 중 가장 큰 값과 수열의 크기 비교

lenT = int(input())
T = list(map(int,input().split()))
up = 0 # 올라간 높이의 합
r = []


for i in range(1,lenT):
    if T[i]>T[i-1]:         # 오르막길입니까?
        up = up + T[i] - T[i-1]   # 오르막길의 총합
        if i == lenT-1:     # 오르막길 도중 배열의 맨 끝에 도달하면
            r.append(up)    
    else:                   # 오르막길이 아닐때
        r.append(up)         # 구한 up을 넣고,(이게 부분순열의 오르막높이)
        up = 0              # 오르막길의 총합  초기화
print(max(r))       # 오르막길의 부분 합 중 가장 큰것을 구해라