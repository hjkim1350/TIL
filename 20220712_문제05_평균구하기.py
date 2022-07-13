numbers = [3, 10, 20]

numbers_sum = 0
i = 0
cnt = 0

for i in numbers:
    numbers_sum = i + numbers_sum
    cnt += 1

avr = numbers_sum/cnt
avr = int(avr)
print(avr)