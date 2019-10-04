"""
Input 3k numbers, where k is natural. Then input
2 more numbers separately.
Example: 2 1 1 2 3 1 3 4 1
         4
         2
Output: 2
"""

class Graph:
    """Already explained."""
    def __init__(self):
        self.m = {}
        self.weight = {}
    def add_elem(self, p_1, p_2, wgt):
        """Already explained."""
        if p_1 in self.m:
            if p_2 not in self.m[p_1]:
                self.m[p_1].append([p_2, wgt])
        else:
            self.m[p_1] = []
            self.m[p_1].append([p_2, wgt])
        self.weight[p_1] = float('inf')
        if p_2 in self.m:
            if p_1 not in self.m[p_2]:
                self.m[p_2].append([p_1, wgt])
        else:
            self.m[p_2] = []
            self.m[p_2].append([p_1, wgt])
        self.weight[p_2] = float('inf')
    def find_way(self, node_start, n_nodes):
        """The only difference in this function is that now it
        returns the biggest node 'weight'"""
        seen = []
        layer = []
        best_way = {}
        self.weight[node_start] = 0
        layer.append(node_start)
        best_way[node_start] = [node_start]
        while layer:
            elem = layer.pop(layer.index(min(layer)))
            next_layer = []
            seen.append(elem)
            for i in range(0, len(self.m[elem])):
                if self.m[elem][i][0] not in seen:
                    if self.m[elem][i][0] not in layer:
                        next_layer.append(self.m[elem][i][0])
                    if self.weight[elem] + int(self.m[elem][i][1]) < self.weight[self.m[elem][i][0]]:
                        self.weight[self.m[elem][i][0]] = self.weight[elem] + int(self.m[elem][i][1])
                        best_way[self.m[elem][i][0]] = [] + best_way[elem]
                        best_way[self.m[elem][i][0]].append(self.m[elem][i][0])
            if not layer:
                layer = next_layer
        max_time = 0
        for i in range(1, n_nodes + 1):
            key = str(i)
            if key not in self.weight:
                return -1
            if self.weight[key] > max_time:
                max_time = self.weight[key]
        return max_time


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
N, X = map(int, input().split())
for k in range(0, len(S), 3):
    GRAPH.add_elem(S[k], S[k + 1], S[k + 2])
print(GRAPH.find_way(str(X), N))
