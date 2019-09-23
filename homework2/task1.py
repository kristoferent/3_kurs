"""
Input a string.
Example:
Input: abcabcabcabc
Output: 4
"""

def find_substring(string):
    """If given string consits of a repeating substring, return
    the amount of times that it's repeated. Else return 0."""
    sub_s = ""
    if len(string) == 1:
        print(1)
    for k in range(0, len(string) // 2):
        sub_s = sub_s[:k] + string[k]
        pos = 0
        next_pos = string.find(sub_s, pos + k + 1)
        count = 1
        while next_pos != -1 and next_pos == pos + k + 1:
            count += 1
            pos += k + 1
            next_pos = string.find(sub_s, pos + k + 1)
        if next_pos == -1 and pos == len(string) - k - 1:
            return count
    return 0

S = input()
print(find_substring(S))

