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

def to_list(number):
    l = List()
    strnum = str(number)
    i = 0
    while i < len(strnum):
        l.add(int(strnum[i]))
        i += 1
    return l

l = to_list(12345)
l.add(6)
l.delete(3)
l.delete(1)
print(l)

