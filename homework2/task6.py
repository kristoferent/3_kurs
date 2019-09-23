class Graph:
    def __init__(self):
        self.m = {}
        self.weight = {}
    def add_elem(self, p1, p2, w):
        if p1 in self.m:
            if p2 not in self.m[p1]:
                self.m[p1].append([p2, w])
        else:
            self.m[p1] = []
            self.m[p1].append([p2, w])
        self.weight[p1] = float('inf')
        if p2 in self.m:
            if p1 not in self.m[p2]:
                self.m[p2].append([p1, w])
        else:
            self.m[p2] = []
            self.m[p2].append([p1, w])
        self.weight[p2] = float('inf')
    def find_way(self, nodeStart, n):
        seen = []
        layer = []
        best_way = {}
        self.weight[nodeStart] = 0
        layer.append(nodeStart)
        best_way[nodeStart] = [nodeStart]
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
        for i in range (1, n + 1):
            key = str(i)
            if key not in self.weight:
                return -1
            if self.weight[key] > max_time:
                max_time = self.weight[key]
        return max_time


graph = Graph()
a = input().split()
N = input()
X = input()
for i in range(0, len(a), 3):
    graph.add_elem(a[i], a[i + 1], a[i + 2])
print(graph.find_way(X, int(N)))

