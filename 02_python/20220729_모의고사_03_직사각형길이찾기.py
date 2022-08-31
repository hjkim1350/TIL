# 2022.07.29 모의고사 03 직사각형 길이 찾기
# 직사각형 네 변 중 세 변의 길이가 주어짐. 나머지 한 변 길이 출력

# 테스트 케이스 입력받음
T = int(input())

# 직사각형 한 변 길이를 담는 리스트 정의
D_list = []

# 테스트 케이스 횟수(T)만큼 for문 실행
for i in range(1, T+1):

    # 주어진 세 변의 길이를 각각 변수에 입력
    A, B, C = map(int, input().split())

    # 하기 조건은 직사각형은 마주보는 두 변이 길이가 서로 같은 특성을 활용.
    # 만약 A, B 변의 길이가 같다면
    if A == B:
        # C 변의 길이는 D와 동일함
        D_list.append(C)
    # 만약 B, C 변의 길이가 같다면
    elif B == C:
        # A 변의 길이는 D와 동일함
        D_list.append(A)
    # 그 외의 케이스인 A, C 변의 길이가 같다면
    else:
        # B 변의 길이는 D와 동일함
        D_list.append(B)

# 결과값 출력
for j in range(1, len(D_list)+1):
    print(f"#{j}", D_list[j-1])