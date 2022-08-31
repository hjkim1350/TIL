import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    sheep_list = []
    sheep_list_complete = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    k = 0
    numbers = 0
    
    while sheep_list != sheep_list_complete :
        k += 1
        numbers = N * k
        
        while numbers:
            sheep_list.append(numbers % 10)
            numbers = numbers // 10
            sheep_list = sorted(set(sheep_list))

    print(f'#{test_case} {N*k}')
