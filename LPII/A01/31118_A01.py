# Shubham - 31118

# undirected graph
class Graph:
    def __init__(self, n) -> None:
        self.n = n
        self.m = 0
        self.adj_list = [[] for _ in range(n+7)]

    def add_adge(self, u, v):
        self.m += 1
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def print_graph(self):
        print("Graph (Adjacency List Representation):")
        for u in range(self.n):
            print(u, end="-> ")
            for v in self.adj_list[u]:
                print(v, end=" ")
            print()

    def dfs_ut(self, u, vis):
        vis.append(u)
        print(u, end=" ")
        for v in self.adj_list[u]:
            if v not in vis:
                self.dfs_ut(v, vis)

    def dfs(self):
        print("Depth-first-traversal: ")
        vis = []
        for i in range(1, self.n+1):
            if i not in vis:
                self.dfs_ut(i, vis)
                print()

    def bfs_ut(self, vis, que):
        if not que:
            return

        u = que[0]
        que.pop(0)

        print(u, end=" ")
        for v in self.adj_list[u]:
            if v not in vis:
                vis.append(v)
                que.append(v)

        self.bfs_ut(vis, que)

    def bfs(self):
        print("Breadth-first-traversal: ")
        vis = []
        for i in range(1, self.n+1):
            if i not in vis:
                vis.append(i)
                self.bfs_ut(vis, [i])
                print()


def main():
    # 1 - based indexing
    n = int(input("Enter number of vertices: "))
    m = int(input("Enter number of edges: "))
    g = Graph(n)

    print("Enter the edges details")
    for i in range(m):
        inp = input()
        [u_, v_] = inp.split(' ')
        u = int(u_)
        v = int(v_)
        g.add_adge(u, v)

    g.print_graph()

    g.dfs()
    g.bfs()


main()
