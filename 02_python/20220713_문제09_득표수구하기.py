# 접근 방법 2가지 방법으로 실행할 예정
# 1) count() 함수를 활용하여 찾기
# 2) if를 활용하여 찾기


students = ['이영희', '김철수', '이영희', '조민지', '김철수', '조민지', '이영희', '이영희']

# 1) count() 함수 활용
elected = students.count('이영희')
print (elected)
cnt = 0

# 2) if 활용
for i in students:
     if i == '이영희':
          cnt += 1

print (cnt)