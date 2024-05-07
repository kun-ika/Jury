def arrange(ilist):
    count1 = ilist.count(1)
    count2 = ilist.count(2)

    sorted_list = [1] * count1 + [2] * count2
    return sorted_list

T = int(input(""))

test_cases = []

for _ in range(T):
    M = int(input("")) 
    ele12 = input("").split() 
    list12 = [int(x) for x in ele12] 

    sorted_list = arrange(list12)
    test_cases.append(sorted_list[:M])

for test_case in test_cases:
    print(*test_case)