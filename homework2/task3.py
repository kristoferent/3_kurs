"""
Input a string of numbers from 0 to 9.
Example:
Input: 23
Output: ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
"""
def possible_combinations(arr, number):
    """Return all possible number combinations that one could
    dial using given numbers in given order"""
    prev_list = arr[int(number[0])]
    cur_list = prev_list
    for i in range(1, len(number)):
        cur_list = []
        new_list = arr[int(number[i])]
        for c_1 in prev_list:
            for c_2 in new_list:
                cur_list.append(c_1 + c_2)
        prev_list = cur_list
    return cur_list

TEL_ARRAY = [[' '], [''], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'],
             ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
NUMBER = input()
print(possible_combinations(TEL_ARRAY, NUMBER))
