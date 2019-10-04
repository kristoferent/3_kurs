"""
Input 2k numbers, where k is natural.
Example:
Input: 0 3 1 3 2 3 4 3 5 4
Output: ??? (depends on the algorithm)
"""

class Graph:
    """m_arr is a dictionary where 'm_arr[key] = value' means
    that there is a verge between nodes 'key' and 'value'."""
    def __init__(self):
        self.m_arr = {}
    def add_elem(self, p_1, p_2):
        """Add new verge between p_1 and p_2"""
        if p_1 in self.m_arr:
            if p_2 not in self.m_arr[p_1]:
                self.m_arr[p_1] += p_2
        else:
            self.m_arr[p_1] = []
            self.m_arr[p_1] += p_2
        if p_2 in self.m_arr:
            if p_1 not in self.m_arr[p_2]:
                self.m_arr[p_2] += p_1
        else:
            self.m_arr[p_2] = []
            self.m_arr[p_2] += p_1
    def bfs(self):
        """Breadth first search"""
        seen = []
        layer = []
        for key in self.m_arr:
            if key not in seen:
                layer.append(key)
                while layer:
                    elem = layer.pop(0)
                    next_layer = []
                    print(elem)
                    seen.append(elem)
                    for i in range(0, len(self.m_arr[elem])):
                        if self.m_arr[elem][i] not in seen:
                            next_layer.append(self.m_arr[elem][i])
                    if not layer:
                        layer = next_layer
    def dfs(self):
        """Depth first search"""
        seen = []
        layer = []
        for key in self.m_arr:
            if key not in seen:
                layer.append(key)
                while layer:
                    elem = layer.pop(0)
                    next_layer = []
                    print(elem)
                    seen.append(elem)
                    for j in range(0, len(self.m_arr[elem])):
                        if self.m_arr[elem][j] not in seen and self.m_arr[elem][j] not in layer:
                            next_layer.insert(0, self.m_arr[elem][j])
                    layer += next_layer

GRAPH = Graph()
Str = input()
S = []
new_num = 0
num_started = 0
for i in range(len(Str)):
    if Str[i] >= '0' and Str[i] <= '9':
        new_num = new_num * 10 + int(Str[i])
        num_started = 1
    elif num_started:
        S.append(str(new_num))
        new_num = 0
        num_started = 0

for k in range(0, len(S), 2):
    GRAPH.add_elem(S[k], S[k + 1])
choice = input("Choose between dfs and bfs: ")
if choice == "dfs":
    GRAPH.dfs()
elif choice == "bfs":
    GRAPH.bfs()
else:
    print("Invalid input")
