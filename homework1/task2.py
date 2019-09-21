import task1 as mod

def list_sum(a, b):
    l = mod.List()
    cur_a = a.head
    cur_b = b.head
    over_flag = 0
    while cur_a != None and cur_b != None:
        val = cur_a.value + cur_b.value
        if over_flag:
            val += 1
        over_flag = 0
        if val >= 10:
            val -= 10
            over_flag = 1
        l.add(val)
        cur_a = cur_a.next_n
        cur_b = cur_b.next_n
        if cur_a != None:
            cur = cur_a
        else:
            cur = cur_b
    while cur != None:
        if over_flag:
            l.add(cur.value + 1)
        else:
            l.add(cur.value)
        cur = cur.next_n
    if over_flag:
        l.add(1)
    return l

a, b = map(int, input().split())
l = list_sum(mod.to_list_v2(a), mod.to_list_v2(b))
print(l)
