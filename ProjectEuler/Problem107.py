#!/usr/bin/env python

# The following undirected network consists of seven vertices and twelve edges with a total weight of 243.
# <graphic>

# The same network can be represented by the matrix below.
#     	A	B	C	D	E	F	G
# A	-	16	12	21	-	-	-
# B	16	-	-	17	20	-	-
# C	12	-	-	28	-	31	-
# D	21	17	28	-	18	19	23
# E	-	20	-	18	-	-	11
# F	-	-	31	19	-	-	27
# G	-	-	-	23	11	27	-

# However, it is possible to optimise the network by removing some edges and still ensure that all points on the network remain connected. The network which achieves the maximum saving is shown below. It has a weight of 93, representing a saving of 243 − 93 = 150 from the original network.

# Using `network.txt` (right click and 'Save Link/Target As...'), a 6K text file containing a network with forty vertices, and given in matrix form, find the maximum saving which can be achieved by removing redundant edges whilst ensuring that the network remains connected.

parent = {}
rank = {}


def parse_matrix():
    matrix = []

    with open("Problem107.txt") as matrix_file:
        for line in matrix_file:
            tmp = line.strip().replace("-", "0").split(",")
            tmp = list(map(int, tmp))
            matrix.append(tmp)

    vertices = list(range(len(matrix)))

    edges = []
    for i in range(len(matrix)):
        for j in range(i):
            if matrix[i][j] > 0:
                edges.append((i, j, matrix[i][j]))

    return vertices, edges


def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]


def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1


def kruskal(vertices, edges):
    minimum_spanning_tree = set()
    edges.sort(key=lambda item: item[2])

    for vertice in vertices:
        parent[vertice] = vertice
        rank[vertice] = 0

    for edge in edges:
        vertice1, vertice2, weight = edge
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            minimum_spanning_tree.add(edge)

    return sorted(minimum_spanning_tree)


def main():
    vertices, edges = parse_matrix()

    solution = kruskal(vertices, edges)

    orig = sum([x[2] for x in edges])
    res = sum([x[2] for x in solution])

    print(orig - res)


if __name__ == "__main__":
    main()
