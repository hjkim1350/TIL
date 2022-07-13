# 접근 방법
# 1) slice를 활용
# 2) reversed() 활용

str = 'apple'

# 1) slice를 활용
rev_str = str[::-1]
print(rev_str)

# 2) reversed() 활용
rev_str_two = "".join(reversed(str))
print(rev_str_two)

# 3) len() 활용
for i in range(len(str)):
    print(str[len(str)-i-1], end='')