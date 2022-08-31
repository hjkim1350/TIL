num = input("정수를 입력하세요: ")
num = int(num)

if num>= 0:
    if num%3==0:
        if num%2==0:
            print("참")
else:
    print("거짓")