# while문
n = input("1부터 곱하기 값을 구할 숫자를 입력하세요: ")
n = int(n)
cnt = 1
i = 1

if n<=1:
    print("1보다 작은 숫자는 유효하지 않습니다. 시스템을 종료합니다.")
else:
    while i <= n:
        cnt = cnt * i
        i += 1
    print(cnt)

# for문
num = input("1부터 곱하기 값을 구할 숫자를 입력하세요: ")
num = int(num)
cnti = 1
b = 1

if num<=1:
    print("1보다 작은 숫자는 유효하지 않습니다. 시스템을 종료합니다.")
else:
    for b in range(1, num+1):
        cnti = cnti * b
        b += 1
    print(cnti)