# BAEKJOON 2739
# Q) N을 입력받은 뒤 구구단 N단을 출력하는 프로그램 작성

T = int(input())

for i in range(1, 10):
    print(T, '*', i, '=', T*i)