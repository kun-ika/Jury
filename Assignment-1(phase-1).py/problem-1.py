M = int(input())
N = input()
total = 0
number = ""

for char in N:
    if char == ";":
        total += int(number)
        number = ""
    else:
        number += char

if number:
    total += int(number)

print(total)