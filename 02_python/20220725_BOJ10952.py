# BAEKJOON 10952
# Q) 두 정수 A, B 입력받은 후 A+B 출력, 마지막 0 0은 합 출력하지 않음

intA = 1
intB = 1
sum = []

while intA:
    intA, intB = map(int, input().split())
    sum.append(intA+intB)

for i in range(0, len(sum)-1):
    print(sum[i])