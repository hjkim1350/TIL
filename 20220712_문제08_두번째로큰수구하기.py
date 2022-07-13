#numbers = [100, 500, 300, 600, 400]
#numbers.sort(reverse=True)

#print(numbers)
#print(numbers[1])


# ---------------------------------------------------------
# 강사님 해설 정리 - max(), sort() 함수 쓰지 않음

numbers = [0, 20, 100, 40]
max_num = numbers[0]
sec_num = numbers[0]

# 1. 전체 숫자를 반복
for n in numbers:
   # 만약에, n이 최대보다 크다면
   if max_num < n:
        # 최대값이었던 것이 두번째로 큰 수
        sec_num = max_num
        max_num = n
   elif sec_num < n and n < max_num:
       sec_num = n
print(sec_num)