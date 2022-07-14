# 문제18
# 문자열 word가 주어질때 Dictionary를 활용해서 문자열에 등장한 모든 알파벳 개수 출력
# Input : banana
# output
# b 1
# a 3
# n 2

word = 'banana'
my_dict = {}
cnt=0

for i in word:
    i = str(i)
    my_dict.update({i:0})

for i in word:
    if i in my_dict.keys():
        my_dict[i] = my_dict[i] + 1

for key, value in my_dict.items():
    print (key, value)


# 강사님 해설 -----------------------------------------------
words = 'banana'
result = {}

for char in words:
    # result['a'] 없으면 keyError
    # result.get('a') 기본값이 None
    # result.get('a', 0) 기본값이 0
    result[char] = result.get(char,0) + 1
print(result)