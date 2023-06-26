import sys
from collections import defaultdict
import time


class Graph:
    def __init__(self, dir_graph=False):
        self.graph = defaultdict(list)
        self.dir_graph = dir_graph

    def add_edge(self, frm, to, weight):
        self.graph[frm].append([to, weight])

        if self.dir_graph is False:
            self.graph[to].append([frm, weight])
        elif self.dir_graph is True:
            self.graph[to] = self.graph[to]

    def minimum_f(self, dis, visit):
        minimum = float('inf')
        index = -1
        for v in self.graph.keys():
            if visit[v] is False and dis[v] < minimum:
                minimum = dis[v]
                index = v

        return index

    def Dijkstras(self, source):
        visit = {i: False for i in self.graph}
        dis = {i: float('inf') for i in self.graph}
        P = {i: None for i in self.graph}

        dis[source] = 0

        # find shortest path for all vertices
        for i in range(len(self.graph) - 1):
            u = self.minimum_f(dis, visit)
            visit[u] = True
            for v, weight in self.graph[u]:

                if visit[v] is False and dis[u] + weight < dis[v]:
                    dis[v] = dis[u] + weight
                    P[v] = u
        return P, dis

    def print_path(self, path, v):
        if path[v] is None:
            return
        self.print_path(path, path[v])
        print(chr(v+65), end=" ")

    def print_solution(self, dis, P, source):
        print('{}\t\t{}\t{}'.format('Vertex', 'Distance', 'Path'))

        for i in self.graph.keys():
            if i == source:
                continue
            if dis[i] == float("inf"):
                continue
            print('{} -> {}\t\t{}\t\t{}'.format(chr(source+65),
                  chr(i+65), dis[i], chr(source+65)), end=' ')
            self.print_path(P, i)
            print()


#program for the input
j = 0
print("****************************************************************")
# graph=None
dir_graph = False
while(j < 4):
    input_file = open("input"+str(j)+".txt", "r")
    i = 0
    source = sys.maxsize
    print()
    print("For the given input file, the shortest paths are: ")
    print()

    for line in input_file.readlines():

        x_line = line.split()
        if i == 0:
            number_of_vertices = int(x_line[0])
            print('Number of Vertices in the graph=', number_of_vertices)
            print('Number of Edges in the graph=', int(x_line[1]))
            dir = x_line[2]
            if dir == "U":
                dir_graph = False
            else:
                dir_graph = True
            graph = Graph(dir_graph)

        elif len(x_line) == 1:
            source = ord(x_line[0])-65
        else:
            graph.add_edge(ord(x_line[0])-65, ord(x_line[1])-65, int(x_line[2]))
        i = i+1
    print("the Source is:", chr(source+65))
    if dir == "U":

        print("it's an UNDIRECTED_GRAPH")
    elif dir == "D":
        print("it is a DIRECTED_GRAPH")

    started_time = time.time()
    path, distance = graph.Dijkstras(source)
    graph.print_solution(distance, path, source)
    runtime = (time.time() - started_time)
    print()
    print('Time taken for Dijkstra\'s Algorithm in seconds:', runtime)
    print()
    j += 1
    print("================================================================")
    print('\t')
