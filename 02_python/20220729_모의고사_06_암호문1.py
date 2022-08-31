# 2022.07.29 모의고사 06 암호문1
# I x, y, s: I x의 위치 바로 다음 y개의 숫자 삽입, s는 덧붙일 숫자 y개 나열
# Input 첫번째줄: 원본 암호문 길이
# Input 두번째줄: 원본 암호문
# Input 세번째줄: 명령어의 개수
# Input 네번째줄: 명령어

# 암호문 담는 리스트 정의
enc_list = []

# 테스트 케이스는 총 10개로 한정하는 문제 조건에 따라 for문은 10번만 실행
for i in range(10):

    # 원본 암호문의 길이 N 입력받음
    N = int(input())
    # 원본 암호문을 입력받아 리스트로 정의
    enc = list(input().split())
    # 명령어의 개수 입력받음
    com_N = int(input())
    # 명령어를 입력받아 리스트로 정의
    com = list(input().split())

    # I x y s로 구성된 Input 네번째줄 명령어 리스트 개수만큼 for문 실행
    for j in range(len(com)):

        # 삽입할 s는 여러개이므로 리스트에 담아 처리
        s = []

        # com이라는 리스트 요소가 I로 시작한다면
        if com[j] == "I":
            # I 다음 문자는 위치 x
            x = int(com[j+1])
            # 위치 x 다음 문자는 삽입할 s의 개수인 y
            y = int(com[j+2])

            # 삽입할 암호문은 I, x, y 다음이므로 +3부터 위치하고 있으며, y개만큼 입력이 될 예정이므로
            # for문의 시작점은 j+3, 마지막지점은 (j+3)+y가 됨
            # 이 범위만큼 s라는 리스트에 암호문을 추가(append)함
            for h in range(j+3, j+3+y):
                s.append(com[h])

            # y개만큼의 암호문을 원본 암호문(enc)에 추가하기 위해 range(y) 설정한 for문 실행
            # 원본 암호문의 위치는 x이고, x 위치에서부터 뒷쪽으로 명령어가 추가됨
            # 따라서 .insert의 시작점은 x+0, x+1... x+y가 되므로 range로 설정한 m이 더해져야함
            # 그리고 s리스트는 y개만큼 요소가 담겼기 때문에 m이라는 값으로 함께 처리 가능
            for m in range(y):
                enc.insert(x+m, s[m])
        
        # 다음 for문을 돌릴 j의 위치는 +3(I, x, y) + y(암호문 담긴 s리스트 개수) 이여야 함
        j = j+3+y
        continue
    
    # 명령어가 추가된 암호문(enc)은 10개까지만 추출하여 결과 리스트(enc_list)에 추가
    enc_list.append(enc[0:10])

# 결과값 출력
for o in range(1, 11):
    print(f"#{o}", end= ' ')
    for p in range(0, 10):
        print(enc_list[o-1][p], end=' ')
    print()