# BAEKJOON 2609
# Q) 2개의 자연수를 입력받아 그 수들의 최대 공약수, 최소 공배수 출력

intA, intB = map(int, input().split())
int_list = []

# 최대 공약수 구하기
if intA < intB:
    for i in range(1, intA+1):
        if intA % i == 0:
            if intB % i == 0:
                int_list.append(i)
else:
    for j in range(1, intB+1):
        if intB % j == 0:
            if intA % j == 0:
                int_list.append(j)

# 최대 공약수 변수 정의
print(int_list)
int_max = int_list[len(int_list)-1]


# 최소 공배수 구하기 - 최소 공배수는 최대공약수를 나눈 약수의 곱을 활용
intA_max = intA // int_max
intB_max = intB // int_max
int_min = intA_max * intB_max * int_max

print(int_max)
print(int_min)