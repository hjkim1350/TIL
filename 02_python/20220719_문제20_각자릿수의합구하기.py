# 정수 number가 주어질 때, 각 자릿수의 합을 구해서 출력하세요.
# Input 123 Output 6

number = input()
number = int(number)
rest = 0

while number > 0:
    rest += (number % 10)
    number = number // 10

print(rest)


# 강사님 풀이 - 아래 케이스 외에도 
numbers = 123

# numbers가 0일때 멈춤, 0이면 false이기 때문
result = 0
while numbers:
    # 몫은 다음 number가 됨.
    # 나머지는 더해나가면됨
    result += numbers%10
    numbers //= 10

print(result)
