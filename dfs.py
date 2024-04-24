class Vertex:
    def __init__(self, data):
        self.data = data
        self.color = "white"
        self.dt = 0
        self.ft = 0

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
        for u in set(self.adj.keys()):
            if u.color == "white":
                time = self.DFS_visit(u, time)

    def __str__(self):
        print("\n ---Adjacency List ---")
        for v in self.adj.keys():
            print(v.data, end=": ")
            for j in self.adj[v]:
                print(j.data, end=" ")
            print("\b")
        return "---End of Adjacency List ---\n"

if __name__ == "__main__":
    graph = Graph(6)
    u, v, w, x, y, z = Vertex('u'), Vertex('v'), Vertex('w'), Vertex('x'), Vertex('y'), Vertex('z')
    graph.add_edge(u, v)
    graph.add_edge(u, x)
    graph.add_edge(x, v)
    graph.add_edge(v, y)
    graph.add_edge(y, x)
    graph.add_edge(w, y)
    graph.add_edge(w, z)
    graph.add_edge(z, z)

    graph.DFS()
    print("DFS: ", end="")
    sorted_vertices = sorted(graph.adj.keys(), key=lambda x: x.ft, reverse=True)
    for v in sorted_vertices:
        print(f"{v.data} ({v.dt}/{v.ft}),", end=" ")
