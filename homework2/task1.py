s = input()
t = ""
if (len(s) == 1):
    print(1)
for k in range (0, len(s) // 2):
    t = t[:k] + s[k]
    pos = 0
    next_pos = s.find(t, pos + k + 1)
    count = 1
    while next_pos != -1 and next_pos == pos + k + 1:
        count += 1
        pos += k + 1
        next_pos = s.find(t, pos + k + 1)
    if next_pos == -1 and pos == len(s) - k - 1:
        print(count)
        break
