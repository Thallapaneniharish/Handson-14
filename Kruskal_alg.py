class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        x_root = self.find(parent, x)
        y_root = self.find(parent, y)

        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    def kruskal_mst(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = [i for i in range(self.V)]
        rank = [0] * self.V

        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        return result


g = Graph(9)
vertex_labels = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8}
g.add_edge(vertex_labels['a'], vertex_labels['b'], 4)  # a-b
g.add_edge(vertex_labels['a'], vertex_labels['h'], 8)  # a-h
g.add_edge(vertex_labels['b'], vertex_labels['h'], 11)  # b-h
g.add_edge(vertex_labels['b'], vertex_labels['c'], 8)  # b-c
g.add_edge(vertex_labels['h'], vertex_labels['i'], 7)  # h-i
g.add_edge(vertex_labels['g'], vertex_labels['h'], 1)  # g-h
g.add_edge(vertex_labels['g'], vertex_labels['i'], 6)  # g-i
g.add_edge(vertex_labels['c'], vertex_labels['i'], 2)  # c-i
g.add_edge(vertex_labels['c'], vertex_labels['f'], 4)  # c-f
g.add_edge(vertex_labels['c'], vertex_labels['d'], 7)  # c-d
g.add_edge(vertex_labels['f'], vertex_labels['d'], 14)  # f-d
g.add_edge(vertex_labels['f'], vertex_labels['e'], 10)  # f-e
g.add_edge(vertex_labels['d'], vertex_labels['e'], 9)  # d-e

mst = g.kruskal_mst()

print("Minimum Spanning Tree:")
for u, v, w in mst:
    print(f"{u} -- {v} == {w}")
