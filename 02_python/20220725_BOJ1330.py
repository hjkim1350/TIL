# BAEKJOON 1330
# Q) 공백으로 구분되어 입력된 정수 A, B 비교
# A가 B보다 크면 '>' 출력, A가 B보다 작으면 '<' 출력, 같으면 '==' 출력

intA, intB = map(int, input().split(' '))

if intA > intB:
    print(">")
elif intA < intB:
    print("<")
else:
    print("==")