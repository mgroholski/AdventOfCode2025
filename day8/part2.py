import bisect
import heapq
from typing import List


class Node:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class UnionFind:
    def __init__(self, nodeCnt):
        self.parent = [i for i in range(nodeCnt)]
        self.rank = [1 for _ in range(nodeCnt)]
        self.componentSize = {}

    def find(self, u):
        if self.parent[u] == u:
            return u

        self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = self.parent[root_v]
            elif self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = self.parent[root_u]
            else:
                self.parent[root_v] = self.parent[root_u]
                self.rank[root_u] += 1

    def connected(self, u, v):
        return self.find(u) == self.find(v)


def distance(a, b):
    return (a.x - b.x) ** 2 + (a.y - b.y) ** 2 + (a.z - b.z) ** 2


def main(inp: List[Node]):
    """
    We need to connect the closest 1000 pairs (we'll want to use the n^2 algorithm that computes this distance).
    Furthermore, we'll want to keep track of the largest three largest circuits. We can keep three variables that will track.
    """
    minHeap = []

    for i in range(len(inp)):
        for j in range(i + 1, len(inp)):
            heapq.heappush(minHeap, (distance(inp[i], inp[j]), i, j))

    unionFind = UnionFind(len(inp))
    res = 0
    while minHeap:
        _, i, j = heapq.heappop(minHeap)
        if not unionFind.connected(i, j):
            res = inp[i].x * inp[j].x
            unionFind.union(i, j)

    print(res)


if __name__ == "__main__":
    inp = []

    with open("inp.txt", "r") as file:
        for line in file:
            vals = line.strip().split(",")
            inp.append(Node(int(vals[0]), int(vals[1]), int(vals[2])))

    main(inp)
