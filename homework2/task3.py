arr = [[' '], [''], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'],
        ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
number = input()
prev_list = arr[int(number[0])]
cur_list = prev_list
for i in range (1, len(number)):
    cur_list = []
    new_list = arr[int(number[i])]
    for c1 in prev_list:
        for c2 in new_list:
            cur_list.append(c1 + c2)
    prev_list = cur_list

print(cur_list)
