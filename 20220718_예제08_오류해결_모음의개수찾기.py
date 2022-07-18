# Output 3

word = "HappyHacking"

count = 0

for char in word:
#    if char == "a" or "e" or "i" or "o" or "u":
    if char in ('a', 'e', 'i', 'o', 'u'):   
        count += 1
        print(count, char)

print(count)