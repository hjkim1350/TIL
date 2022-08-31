# BAEKJOON 1065
# Q) 자연수 N이 주어졌을 때 1부터 N까지 한줄에 하나씩 큰 숫자부터 출력

T = int(input())

for i in range(1, T+1):
    print(T+1-i)