# 2022.07.29 모의고사 01 소득불균형
# 소득이 주어졌을 때 평균 이하의 소득을 가진 사람들의 수 출력

# 테스트 케이스 입력받음
T = int(input())

# 평균 이하의 소득 담는 리스트 정의
cnt_list = []

# 테스트 케이스 횟수(T)만큼 for문 실행
for i in range(1, T+1):

    # 테스트 케이스 번호 입력 받음
    test_case = int(input())

    # 스페이스로 구분되는 소득 목록을 list로 정의
    income = list(map(int, input().split()))

    # 전체 소득 합(sum), 소득 평균(avr), 소득 평균 이하 사람수(cnt) 선언
    sum = 0
    avr = 0
    cnt = 0

    # 테스트 케이스 번호만큼 for문 실행
    for j in range(test_case):
        # 소득 목록의 소득 합을 계산
        sum += income[j]
    
    # 소득 합에 전체 사람 수 나눠서 평균 계산
    avr = sum / test_case

    # 소득 평균 이하 사람수 계산
    for h in income:
        if h <= avr:
            cnt += 1
    
    # 테스트 케이스에 따른 결과값 list에 담음
    cnt_list.append(cnt)

# 결과값 출력
for m in range(1, len(cnt_list)+1):
    print(f"#{m}", cnt_list[m-1])