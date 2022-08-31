# BAEKJOON 11021
# Q) 첫째줄에는 테스트 케이스 개수 T 주어짐
# 각 테스트 케이스는 한줄로 이루어져있으며, 각줄에는 A B가 주어짐
# 그에 따라 "Case #x: " 출력 후 A+B 출력

T = int(input())
A_list_i = []
B_list_i = []
sum_i = []

for i in range(1, T+1):
    A_i, B_i = map(int, input().split())
    A_list_i.append(A_i)
    B_list_i.append(B_i)
    sum_i.append(A_i+B_i)

for num in range(1, T+1):
    print(f'Case #{num}:', A_list_i[num-1],'+', B_list_i[num-1], '=', sum_i[num-1])