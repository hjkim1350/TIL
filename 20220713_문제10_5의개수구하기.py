# 접근 방법 2가지 방법으로 실행할 예정
# 1) map() 함수를 활용하여 찾기
# 2) if를 활용하여 찾기


numbers = [7, 17, 10, 5, 4, 3, 17, 5, 2, 5]

# 1) map() 함수 활용
cnt = list(map(int, numbers))
total = 0
for a in cnt:
     if a == 5:
          total += 1

print('map()함수 활용 결과값:', total)


# 2) if 활용 - list 안에 있는 값을 string에서 int로 형변환하여 더해주기

numbers_two = [7, 17, 10, 5, 4, 3, 17, 5, 2, 5]
total_sum = 0

for i in range(len(numbers_two)):
     numbers_two[i] = int(numbers_two[i])

     if numbers_two[i] == 5:
          total_sum += 1

print('if 활용 결과값: ', total_sum)
