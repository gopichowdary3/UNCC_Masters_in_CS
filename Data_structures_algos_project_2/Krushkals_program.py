import time


class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def path_find(self, path, i):

        if path[i] == i:
            return i
        return self.path_find(path, path[i])

    def union_function(self, path, r, x, y):
        X = self.path_find(path, x)
        Y = self.path_find(path, y)

        if r[X] < r[Y]:
            path[X] = Y
        elif r[X] > r[Y]:
            path[Y] = X

        else:
            path[Y] = X
            r[X] += 1

    def Krushkal_function(self):

        result = []
        e = 0
        i = 0
        self.graph = sorted(self.graph, key=lambda item: item[2])

        P = []
        r = []

        for node in range(self.V):
            P.append(node)
            r.append(0)

        while e < self.V - 1:

            u, v, w = self.graph[i]

            i = i + 1
            x = self.path_find(P, u)
            y = self.path_find(P, v)

            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union_function(P, r, x, y)

        print('Edge Selected \t\t Weight')
        print()
        res = 0
        for u, v, weight in result:
            print(chr(u + 65), "-", chr(v + 65), "\t\t\t", weight)
            res += weight
        print('Minimum Spanning Tree\'s total cost =', res)


# program for the input
print("********************************************************************************")
j = 2
print()
while (j < 6):
    print("For the given graph, Minimum Spanning Tree using Kruskal's Algorithm:")
    print()
    input_file = open("input" + str(j) + ".txt", "r")

    i = 0
    for line in input_file.readlines():
        x = line.split()
        if i == 0:
            number_of_vertices = int(x[0])
            # print("number of vertices=",number_of_vertices)
            graph = Graph(number_of_vertices)
        elif len(x) == 1:
            pass
        else:
            graph.add_edge(ord(x[0]) - 65, ord(x[1]) - 65, int(x[2]))
        i = i + 1
    started_time = time.time()
    graph.Krushkal_function()
    time_taken = (time.time() - started_time)
    print('---------------------------------------------------------------------')
    print('Time taken for running Kruskal Algorithm in seconds=', time_taken)
    print()
    j += 1
    print("=====================================================================")
    print('\t')
