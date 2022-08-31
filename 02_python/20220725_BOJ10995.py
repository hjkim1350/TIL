# BAEKJOON 10995
# Q) 입력되는 정수에 따라 별 개수를 출력
# 첫번째 줄과 두번째줄은 서로 별이 크로스되어야 함

T = int(input())

for i in range(1, T+1):
    if i%2 == 1:
        print('* ' * T)
    else:
        print(' *' * T)