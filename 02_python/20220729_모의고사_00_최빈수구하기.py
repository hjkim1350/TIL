# 2022.07.29 모의고사 00 최빈수 구하기
# 최빈수: 가장 여러번 나타나는 값

# 테스트 케이스 입력받음
T = int(input())

# 최빈수 담는 리스트 정의
result = []

# 테스트 케이스 횟수(T)만큼 for문 실행
for i in range(1, T+1):

    # 테스트 케이스 번호 입력 받음
    test_case = int(input())

    # 스페이스로 구분되는 점수 목록을 list로 정의
    score_list = []
    score_list = list(map(int, input().split()))
    
    # 동일한 점수를 받은 학생수를 dictionary 형태로 정의
    score_dic = {}

    # 동일한 점수를 받은 학생수를 dictionary 형태로 카운트
    for j in score_list:
        # 만약 점수가 dictionary에 없으면 점수를 key에 입력하고 학생수 1로 설정
        if j not in score_dic:
            score_dic.setdefault(j, 1)
        # 만약 점수가 dictionary에 있다면 학생수 +1
        else:
            score_dic[j] += 1

    # 동일한 최빈수가 발생했을 때 가장 높은 점수를 출력하기 위해,
    # 점수(key)를 역순으로 정렬
    score_dic_sort = dict(sorted(score_dic.items(), reverse=True))

    # 학생수(value)가 가장 큰 값을 result_라는 변수에 담고, 이 변수를 다시 result 리스트에 담음.
    result_ = max(score_dic_sort, key=score_dic_sort.get)
    result.append(result_)

# 결과값 출력
for h in range(1, T+1):
    print(f"#{h}", result[h-1])