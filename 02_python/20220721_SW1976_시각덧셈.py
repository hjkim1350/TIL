import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    h1, m1, h2, m2 = map(int, input().split())
    
    h_total = h1 + h2
    m_total = m1 + m2

    while h_total > 12:
        h_total -= 12
    
    while m_total > 60:
        m_total -= 60
        h_total += 1
    
    print(f'#{test_case} {h_total} {m_total}')
    