# 2022.07.29 모의고사 04 신용카드만들기1
# 신용카드는 룬의 공식을 만족해야함
# 룬의 공식은 하기와 같음
# 1) 매 홀수자리 숫자마다 2를 곱해서 더하기
# 2) 매 짝수자리 숫자는 그대로 더하기
# 3) 1), 2)를 더한 숫자에 N을 더한 숫자가 10으로 나눴을 때 나눠 떨어지면 유효
# 마지막 N 구하기

# 테스트 케이스 입력받음
T = int(input())

# N 숫자 담는 리스트 정의
card_list = []

# 테스트 케이스 횟수(T)만큼 for문 실행
for i in range(1, T+1):

    # 스페이스로 구분되는 카드 번호목록을 list로 정의
    card_num = []
    card_num = list(map(int, input().split()))

    # 룬의 공식의 1), 2)를 합한 결과를 담을 sum 정의
    sum = 0

    # 카드 번호는 총 15개 주어지는 조건을 활용하여 for문 실행
    for j in range (1, 16):
        # 카드번호 위치가 홀수일 경우
        if j % 2 == 1:
            # 카드번호에 곱하기 2를 하여 총합(sum)에 더하기
            sum += card_num[j-1]*2
        # 카드번호 위치가 짝수일 경우
        else:
            # 카드번호만 총합(sum)에 더하기
            sum += card_num[j-1]

    # 구해진 sum이 10으로 나눠떨어질 경우 N은 0이 됨
    if sum % 10 == 0:
        card_list.append("0")
    # 구해진 sum이 10으로 나눠떨어지지 않을 경우 10으로 나눈 나머지를 10에서 빼면 N이 됨.
    else:
        card_list.append(10-sum%10)

# 결과값 출력
for h in range(1, len(card_list)+1):
    print(f"#{h}", card_list[h-1])