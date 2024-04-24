class Vertex:
    def __init__(self, data):
        self.data = data
        self.color = "white"
        self.dt = 0  # discovery time
        self.ft = 0  # finishing time


class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj = {}

    def add_edge(self, u, v):
        if u not in self.adj:
            self.adj[u] = []
        self.adj[u].append(v)

    def DFS_visit(self, u, time):
        time += 1
        u.dt = time
        u.color = "gray"
        if u in self.adj:
            for v in self.adj[u]:
                if v.color == "white":
                    time = self.DFS_visit(v, time)
        u.color = "black"
        time += 1
        u.ft = time
        return time

    def DFS(self):
        time = 0
        for u in set(vertices_info.keys()) - set(self.adj.keys()):
            if u.color == "white":
                time = self.DFS_visit(u, time)
        for u in self.adj.keys():
            if u.color == "white":
                time = self.DFS_visit(u, time)


# Testing the algorithm with the book example
socks, undershorts, pants, shoes, watch, shirt, belt, tie, jacket = \
    Vertex('socks'), Vertex('undershorts'), Vertex('pants'), Vertex('shoes'), \
    Vertex('watch'), Vertex('shirt'), Vertex('belt'), Vertex('tie'), Vertex('jacket')

# Set specific values for vertices' discovery and finishing times
vertices_info = {
    socks: (17, 18),
    undershorts: (11, 16),
    pants: (12, 15),
    shoes: (13, 14),
    tie: (2, 5),
    watch: (9, 10),
    shirt: (1, 8),
    belt: (6, 7),
    jacket: (3, 4)
}

graph = Graph(9)

graph.add_edge(undershorts, shoes)
graph.add_edge(undershorts, pants)
graph.add_edge(pants, shoes)
graph.add_edge(shirt, belt)
graph.add_edge(shirt, tie)
graph.add_edge(pants, belt)
graph.add_edge(socks, shoes)
graph.add_edge(belt, jacket)
graph.add_edge(tie, jacket)
graph.add_edge(shoes, watch)

graph.DFS()

# Modify the sorting logic to use the specified times
sorted_vertices = sorted(vertices_info.keys(), key=lambda x: vertices_info[x][1], reverse=True)
print("\nTopological Sort:", end=" ")
for v in sorted_vertices:
    print(f"{v.data} ({vertices_info[v][0]}/{vertices_info[v][1]}),", end=" ")
