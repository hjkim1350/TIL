# 2022.07.29 모의고사 02 문자열의 거울상
# b d p q 로 이루어진 문자열이 주어짐.
# 이 문자열을 거울에 비추면 어떤 문자열이 되는지 구하기
# ex) bdppq --> pqqbd

# 테스트 케이스 입력받음
T = int(input())

# 거울에 비춘 문자열 결과를 담는 리스트 정의
mirror_list = []

# 테스트 케이스 횟수(T)만큼 for문 실행
for i in range (1, T+1):

    # 거울에 비출 문자열 입력 받음
    given_str = input()

    # 거울에 비춘 문자열 결과를 담는 변수 정의
    mirror = ""

    # 문자 하나하나를 거울에 비춘 결과의 문자로 바꿔서 mirror라는 새로운 문자열을 생성
    for j in range(0, len(given_str)):
        # 주어진 문자 b라면 거울에 비춘 문자는 d
        if given_str[j] == "b":
            mirror += "d"
        # 주어진 문자 d라면 거울에 비춘 문자는 b
        elif given_str[j] == "d":
            mirror += "b"
        # 주어진 문자 p라면 거울에 비춘 문자는 q
        elif given_str[j] == "p":
            mirror += "q"
        # 주어진 문자 q라면 거울에 비춘 문자는 p
        # else로 처리해도 되는 이유는 문제에서 문자열이 b, d, p, q만으로 이루어져있다고 전제하였음
        else:
            mirror += "p"
    
    # 문자열들이 거울에 비췄을 경우 순서자체도 뒤집혀서 역순으로 정의
    mirror = mirror[::-1]

    # 거울에 비춘 결과를 mirror_list 리스트에 담음
    mirror_list.append(mirror)

# 결과값 출력
for j in range(1, len(mirror_list)+1):
    print(f"#{j}", mirror_list[j-1])