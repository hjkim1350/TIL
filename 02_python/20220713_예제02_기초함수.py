# 접근 방법
# 1) 넓이 구하기, 둘레 구하기 함수 각각 정의
# 2) 함수 호출 및 넓이, 둘레 결과 출력

# 넓이 구하기 함수 정의
def area (hori, verti):
    res_two = hori * verti
    return res_two

# 둘레 구하기 함수 정의
def circum (hori, verti):
    res = (hori + verti) * 2
    return res

print('가로 20, 세로 30의 넓이:', area(20, 30))
print('가로 20, 세로 30의 둘레:', circum(20, 30))