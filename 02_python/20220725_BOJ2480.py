# BAEKJOON 2480
# Q) 주사위 3개 던져서 다음과 같이 상금 받음
# 1) 같은 수 3개 나오면 10,000 + (같은 수) x 1,000원
# 2) 같은 수 2개 나오면  1,000 + (같은 수) x   100원
# 3) 모두 다른 눈이 나오면 (그 중 가장 큰 수) x 100원

intA, intB, intC = map(int, input().split())

if intA == intB == intC:
    print(10000 + intA * 1000)
elif intA == intB != intC:
    print(1000 + intA * 100)
elif intA == intC != intB:
    print(1000 + intA * 100)
elif intB == intC != intA:
    print(1000 + intB * 100)
else:
    intmax = max(intA, intB, intC)
    print(intmax * 100)