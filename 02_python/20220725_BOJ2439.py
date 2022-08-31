# BAEKJOON 2439
# Q) 첫번째 줄에는 별 1개, 두번째 줄에는 별 2개, N번째 줄에는 별 N개 출력
# 하지만 오른쪽을 기준으로 정렬한 별을 출력

T = int(input())

for i in range(1, T+1):
    print(' '*(T-i), '*'*i, sep='')