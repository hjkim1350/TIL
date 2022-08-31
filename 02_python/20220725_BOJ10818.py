# BAEKJOON 10818
# Q) N개 정수 주어질 때 최소값과 최대값 구하기

T = int(input())
min_max = list(map(int, input().split()))

min_max.sort()

print(min_max[0], min_max[len(min_max)-1])