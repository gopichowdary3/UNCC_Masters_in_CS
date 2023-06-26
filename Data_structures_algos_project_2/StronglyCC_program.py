from collections import defaultdict
from itertools import chain
import time


class Graph(object):
    def __init__(self, edges, vertices=()):
        self.edges = edges
        self.vertices = set(chain(*edges)).union(vertices)
        self.tails = defaultdict(list)
        for head, tail in self.edges:
            self.tails[head].append(tail)

    @classmethod
    def from_dict(cls, edge_dict):
        return cls((k, v) for k, vs in edge_dict.items() for v in vs)


class _StrongCC(object):
    def strong_connect(self, head):
        low_link, count, stack = self.low_link, self.count, self.stack
        low_link[head] = count[head] = self.counter = self.counter + 1
        stack.append(head)

        for tail in self.graph.tails[head]:
            if tail not in count:
                self.strong_connect(tail)
                low_link[head] = min(low_link[head], low_link[tail])
            elif count[tail] < count[head]:
                if tail in self.stack:
                    low_link[head] = min(low_link[head], count[tail])

        if low_link[head] == count[head]:
            component = []
            while stack and count[stack[-1]] >= count[head]:
                component.append(chr(stack.pop()+65))

            self.connected_components.append(component)

    def __call__(self, graph):
        self.graph = graph
        self.counter = 0
        self.count = dict()
        self.low_link = dict()
        self.stack = []
        self.connected_components = []

        for v in self.graph.vertices:
            if v not in self.count:
                self.strong_connect(v)

        return self.connected_components


strongly_connected_components = _StrongCC()

if __name__ == '__main__':

    count = 6
    print()
    while (count < 10):
        print("The Strongly Connected Components for the given graph is:")
        print()

        input_file = open("input" + str(count) + ".txt", "r")
        edges = []
        i = 0
        for line in input_file.readlines():
            l = line.split()
            if i == 0:
                no_of_vertices = int(l[0])
                # print("no_of_vertices", no_of_vertices)
            elif len(l) == 1:
                pass
            else:
                edges.append((ord(l[0]) - 65, ord(l[1]) - 65))

            i = i + 1
        start_time = time.time()
        print(strongly_connected_components(Graph(edges)))

        runtime = (time.time() - start_time)
        print('======================================================================')
        print('Time taken for running Strongly Connected Components Algorithm in seconds:', runtime)
        print()
        count += 1
        print("********************************************************************")
        print('\t')
