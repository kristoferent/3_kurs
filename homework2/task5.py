"""
Input 3k numbers, where k is natural. Then input 2 more numbers.
Example:
Input: 0 3 5 1 3 11 2 3 56 4 3 77 5 4 89
       0 5
Output: ['0', '3', '4', '5']
"""

class Graph:
    """'weight' dictionary is necessary for the Dijkstra algorithm"""
    def __init__(self):
        self.m_arr = {}
        self.weight = {}
    def add_elem(self, p_1, p_2, wgt):
        """Add a verge between p_1 and p_2 and give it a weight wgt. Add every node
        in the 'weight' dictionary and assign them infinite values"""
        if p_1 in self.m_arr:
            if p_2 not in self.m_arr[p_1]:
                self.m_arr[p_1].append([p_2, wgt])
        else:
            self.m_arr[p_1] = []
            self.m_arr[p_1].append([p_2, wgt])
        self.weight[p_1] = float('inf')
        if p_2 in self.m_arr:
            if p_1 not in self.m_arr[p_2]:
                self.m_arr[p_2].append([p_1, wgt])
        else:
            self.m_arr[p_2] = []
            self.m_arr[p_2].append([p_1, wgt])
        self.weight[p_2] = float('inf')
    def find_way(self, node_start, node_end):
        """Create the 'best_way' dictionary, it contains the best paths
        from node_start to every other node"""
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
            for i in range(0, len(self.m_arr[elem])):
                if self.m_arr[elem][i][0] not in seen:
                    if self.m_arr[elem][i][0] not in layer:
                        next_layer.append(self.m_arr[elem][i][0])
                    if self.weight[elem] + int(self.m_arr[elem][i][1]) < self.weight[self.m_arr[elem][i][0]]:
                        self.weight[self.m_arr[elem][i][0]] = self.weight[elem] + int(self.m_arr[elem][i][1])
                        best_way[self.m_arr[elem][i][0]] = [] + best_way[elem]
                        best_way[self.m_arr[elem][i][0]].append(self.m_arr[elem][i][0])
            if not layer:
                layer = next_layer
        print(best_way[node_end])

GRAPH = Graph()
S = input().split()
N = input().split()
for k in range(0, len(S), 3):
    GRAPH.add_elem(S[k], S[k + 1], S[k + 2])
GRAPH.find_way(N[0], N[1])
