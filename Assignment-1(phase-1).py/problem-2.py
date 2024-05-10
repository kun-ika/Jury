M = int(input())
input_str = input()
element_list = []
element = ''

for char in input_str:
    if char == ',':
        element_list.append(element)
        element = ''
    else:
        element += char

if element:
    element_list.append(element)

N = input()
found = False

for i in range(len(element_list)):
    if N == element_list[i]:
        print(i)
        found = True
        break

if not found:
    print("Better Luck Next Time") 
