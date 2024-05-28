from collections import deque
from typing import List


class GraphList:
    def __init__(self, size: int) -> None:
        self.size = size
        self.adj_list = [[] for _ in range(size)]

    def add_edge(self, src: int, dst: int, weight: int):
        if not (0 <= src < self.size) or not (0 <= dst < self.size):
            raise Exception("Invalid key number for graph")

        self.adj_list[src].append((dst, weight))

    def traverse(self, start: int = 0, type: str = "bfs") -> List[int]:
        if type == "dfs":
            return self.dfs(start=start)
        return self.bfs(start=start)

    def dfs(self, start: int = 0) -> List[int]:
        result = []
        stack = [start]
        visited = set()

        while stack:
            curr = stack.pop()
            if curr in visited:
                continue
            visited.add(curr)
            result.append(curr)
            for edge in self.adj_list[curr]:
                stack.append(edge[0])

        return result

    def bfs(self, start: int = 0) -> List[int]:
        result = []
        queue = deque()
        queue.append(start)
        visited = set()
        visited.add(start)

        while queue:
            curr = queue.popleft()
            result.append(curr)
            for edge in self.adj_list[curr]:
                if edge[0] in visited:
                    continue
                visited.add(edge[0])
                queue.append(edge[0])

        return result

    def __str__(self) -> str:
        adj_str = "[\n"
        for i, l in enumerate(self.adj_list):
            row_str = f" {i}: " + "".join([f" {val}, " for val in l])
            adj_str = adj_str + row_str + "\n"
        adj_str = adj_str + "]"
        return adj_str


class GraphMatrix:
    def __init__(self, size: int):
        self.size = size
        self.matrix = [[0 for _ in range(size)] for _ in range(size)]

    def add_edge(self, src: int, dst: int, weight: int):
        if not (0 <= src < self.size) or not (0 <= dst < self.size):
            raise Exception("Invalid key number for graph")

        self.matrix[src][dst] = weight

    def traverse(self, start: int = 0, type: str = "bfs") -> List[int]:
        if type == "dfs":
            return self.dfs(start=start)
        return self.bfs(start=start)

    def dfs(self, start: int = 0) -> List[int]:
        st = [start]
        visited = set()
        result = []
        while st:
            curr = st.pop()
            if curr in visited:
                continue
            visited.add(curr)
            result.append(curr)
            for i, w in enumerate(self.matrix[curr]):
                if w != 0:
                    st.append(i)
        return result

    def bfs(self, start: int = 0) -> List[int]:
        result = []
        q = deque()
        q.append(start)
        visited = set()
        visited.add(start)

        while q:
            curr = q.popleft()
            result.append(curr)
            for i, w in enumerate(self.matrix[curr]):
                if w == 0 or i in visited:
                    continue
                q.append(i)
                visited.add(i)

        return result

    def __str__(self):
        mat_str = "[\n"
        for row in self.matrix:
            row_str = "".join([f" {cell} " for cell in row])
            mat_str = mat_str + row_str + "\n"
        mat_str = mat_str + "]"
        return mat_str


if __name__ == "__main__":
    graph = GraphMatrix(8)
    graph.add_edge(0, 1, 4)
    graph.add_edge(0, 2, 3)
    graph.add_edge(1, 2, 2)
    graph.add_edge(2, 0, 3)
    graph.add_edge(2, 3, 6)
    graph.add_edge(3, 0, 8)
    graph.add_edge(3, 4, 1)
    graph.add_edge(4, 5, 3)
    graph.add_edge(5, 6, 2)
    graph.add_edge(6, 7, 1)
    graph.add_edge(7, 5, 2)

    # print(graph)
    print("DFS Adj Matrix: ", graph.traverse(type="dfs", start=3))
    print("BFS Adj Matrix: ", graph.traverse(start=3))
    graph_list = GraphList(8)
    graph_list.add_edge(0, 1, 4)
    graph_list.add_edge(0, 2, 3)
    graph_list.add_edge(1, 2, 2)
    graph_list.add_edge(2, 0, 3)
    graph_list.add_edge(2, 3, 6)
    graph_list.add_edge(3, 0, 8)
    graph_list.add_edge(3, 4, 1)
    graph_list.add_edge(4, 5, 3)
    graph_list.add_edge(5, 6, 2)
    graph_list.add_edge(6, 7, 1)
    graph_list.add_edge(7, 5, 2)

    # print(graph_list)
    print("DFS Adj List: ", graph_list.traverse(type="dfs", start=3))
    print("BFS Adj List: ", graph_list.traverse(start=3))
