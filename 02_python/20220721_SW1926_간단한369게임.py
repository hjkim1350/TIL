from re import I
import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    i = str(test_case)
    
    clap = i.count('3') + i.count('6') + i.count('9')

    if clap == 0:
        print(i, end=' ')
    else:
        print("-" * clap, end = ' ')