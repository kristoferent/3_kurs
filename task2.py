class Node:
    def __init__(self, value = None, next_n = None):
        self.value = value
        self.next_n = next_n

class List:
    def __init__(self):
        self.head = None
        self.end = None
        self.length = 0

    def __str__(self):
        if self.end != None:
            cur = self.head
            out = ''
            while cur.next_n != None:
                out += str(cur.value) + ' -> '
                cur = cur.next_n
            out += str(cur.value)
            return out
        return 'List is empty.'

    def add(self, val):
        if self.end == None:
            self.end = self.head = Node(val, None)
        else:
            self.end.next_n = Node(val, None)
            self.end = self.end.next_n
        self.length += 1

    def delete_last(self):
        if self.end == None:
            print('Error! List is empty.')
        elif self.head == self.end:
            self.__init__()
        else:
            cur = self.head
            while cur.next_n != self.end:
                cur = cur.next_n
            self.end = cur
            self.end.next_n = None
            self.length -= 1

    def delete(self, val):
        i = self.find(val)
        if i == self.length - 1:
            self.delete_last()
        elif i != -1:
            self.length -= 1
            cur = self.head
            if i == 0:
                self.head = cur.next_n
                return
            while i != 1:
                cur = cur.next_n
                i -= 1
            cur.next_n = cur.next_n.next_n

    def find(self, val):
        count = 0
        cur = self.head
        while cur != None:
            if cur.value == val:
                return count
            else:
                cur = cur.next_n
                count += 1
        print('No such element: ' + str(val))
        return -1
    def print_length(self):
        print(self.length)

def to_list_v2(num):
    l = List()
    if (num == 0):
        l.add(0)
    while num != 0:
        l.add(num % 10)
        num = num // 10
    return l

def list_sum(a, b):
    l = List()
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
l = list_sum(to_list_v2(a), to_list_v2(b))
print(l)
