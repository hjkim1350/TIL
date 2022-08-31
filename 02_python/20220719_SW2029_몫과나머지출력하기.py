# 2개 수 a, b 입력받아 a, b로 나눈 몫과 나머지 출력

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    a, b= map(int, input().split())
    print("#{} {} {}".format(test_case, a//b, a%b))