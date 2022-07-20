import sys
sys.stdin = open("input.txt", "r")

T = int(input())

while T > -1:
    print(T, end=' ')
    T -= 1