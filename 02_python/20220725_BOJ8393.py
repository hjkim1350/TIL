# BAEKJOON 8393
# Q) N이 주어졌을 때 1부터 N까지의 합 출력

T = int(input())
sum = 0

for i in range(1, T+1):
    sum += i
print(sum)