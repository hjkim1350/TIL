numbers = input()
numbers = int(numbers)
count = 1

if numbers > 0:
    while 10 ** count <= numbers:
        count += 1
    print(count)
else:
    print("양의 정수만 입력하세요.")



# log를 활용
#import math
#number = 123
#print(round(math.log10(number)+1))