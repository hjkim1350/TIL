# BAEKJOON 9498
# Q) 100~90점:A, 89~80점:B, 79~70점:C, 69~60점:D, 그 외:F

score = int(input())

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")