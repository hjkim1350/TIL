# 접근 방법
# 중첩 while문, f-string 활용

# 단 변수 정의
dan = 1

# 곱셈 숫자 정의
soo = 1

# 곱셈 결과값 정의
mul = 0

while dan < 9:
     dan += 1
     print (f'{dan}단')
     while soo < 10:
          mul = dan * soo
          print(f'{dan} X {soo} = {mul}')
          soo += 1
     print()
     soo = 1