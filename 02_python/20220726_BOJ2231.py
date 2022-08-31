# BAEKJOON 2231
# Q) 자연수N의 생성자를 구하기
# 예를 들어 245의 분해합은 256(245+2+4+5)이기 때문에,
# 256의 생성자는 245임.
# 자연수 중 생성자가 없는 수도 있고, 여러개인 경우 가장 작은 생성자 출력

# 문제풀이 공략
# 1) 
# 2) 


N = int(input())
x_sum = 0 # 각 자리수 더하기

for x in range(1,N+1): # 1부터 N까지 돌면서
    for i in str(x):   
        x_sum += int(i) # 각 자리수 더한 값
    if x + x_sum != N: # x + x의 각 자리수 합이 N이 아니면
        x_sum = 0  # 각 자리수 합 초기화
    if x + x_sum == N:
        print(x)
        break