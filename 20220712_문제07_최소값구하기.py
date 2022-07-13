numbers = [0, 20, 100, 50, -60, 50, 100]
tmp = numbers[0]

for i in numbers:
    if i < tmp:
        tmp = i
print(tmp)
