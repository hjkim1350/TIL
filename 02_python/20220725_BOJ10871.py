# BAEKJOON 10871
# Q) 첫 줄에 N과 X가 주어짐
# 둘째줄에 수열 A를 이루는 정수 N개가 주어짐
# X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력

intN, intX = map(int, input().split())
small_X = list(map(int, input().split()))

for i in range(0, intN):
    if small_X[i] < intX:
        print(small_X[i])