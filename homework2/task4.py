class Graph:
    def __init__(self):
        self.m = {}
    def add_elem(self, p1, p2):
        if p1 in self.m:
            if p2 not in self.m[p1]:
                self.m[p1] += p2
        else:
            self.m[p1] = []
            self.m[p1] += p2
        if p2 in self.m:
            if p1 not in self.m[p2]:
                self.m[p2] += p1
        else:
            self.m[p2] = []
            self.m[p2] += p1
    def bfs(self):
        seen = []
        layer = []
        for key in self.m:
            if key not in seen:
                layer.append(key)
                while layer:
                    elem = layer.pop(0)
                    next_layer = []
                    print(elem)
                    seen.append(elem)
                    for i in range(0, len(self.m[elem])):
                        if self.m[elem][i] not in seen:
                            next_layer.append(self.m[elem][i])
                    if not layer:
                        layer = next_layer
    def dfs(self):
        seen = []
        layer = []
        for key in self.m:
            if key not in seen:
                layer.append(key)
                while layer:
                    elem = layer.pop(0)
                    next_layer = []
                    print(elem)
                    seen.append(elem)
                    for i in range(0, len(self.m[elem])):
                        if self.m[elem][i] not in seen and self.m[elem][i] not in layer:
                            next_layer.insert(0, self.m[elem][i])
                    layer += next_layer

graph = Graph()
a = input().split()
for i in range(0, len(a), 2):
    graph.add_elem(a[i], a[i + 1])
graph.bfs()
