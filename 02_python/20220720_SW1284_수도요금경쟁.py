import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())

    # A사 수도요금 계산
    com_A = W * P
    
    # B사 수도요금 계산
    # 기본 용량만 사용하였을 경우
    if W <= R:
        com_B = Q
    # 기본 용량 초과 사용하였을 경우
    else:
        com_B = Q + (W-R) * S
    
    # A사가 더 저렴할 경우 A사 요금 출력
    if com_A <= com_B:
        print(f'#{test_case} {com_A}')
    # B사가 더 저렴할 경우 B사 요금 출력
    else:
        print(f'#{test_case} {com_B}')