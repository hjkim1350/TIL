import sys
sys.stdin = open("input.txt", "r")

import statistics

T = int(input())
for test_case in range(1, T + 1):
    avr = []
    result=0
    avr = map(int, input().split())
    result=round(statistics.mean(avr))
    print("#{} {}".format(test_case, result))