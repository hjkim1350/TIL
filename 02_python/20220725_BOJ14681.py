# BAEKJOON 14681
# Q) x좌표와 y좌표가 주어질 때 몇 사분면인지 출력

intA = int(input())
intB = int(input())

if intA > 0:
    if intB > 0:
        print(1)
    else:
        print(4)
else:
    if intB > 0:
        print(2)
    else:
        print(3)