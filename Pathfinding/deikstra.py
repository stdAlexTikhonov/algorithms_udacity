from collections import defaultdict
import sys

class Graph:
    def __init__(self):
        self.nodes = set()
        self.neibhours = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.neibhours[from_node].append(to_node)
        self.neibhours[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance

    def print_graph(self):
        print("Set of Nodes are: ", self.nodes)
        print("Neighbours are: ", self.neighbours)
        print("Distances are: ", self.distances)


testGraph = Graph()

for node in ['A', 'B', 'C', 'D', 'E']:
    testGraph.add_node(node)

testGraph.add_edge('A','B',3)
testGraph.add_edge('A','D',2)
testGraph.add_edge('B','D',4)
testGraph.add_edge('B','E',6)
testGraph.add_edge('B','C',1)
testGraph.add_edge('C','E',2)
testGraph.add_edge('E','D',1)


def deikstra(graph, source):
    result = {}
    result[source] = 0

    for node in graph.nodes:
        if node != source:
            result[node] = sys.maxsize

    unvisited = set(graph.nodes)

    path = {}

    while unvisited:
        min_node = None


        for node in unvisited:
            if node in result:
                if min_node is None:
                    min_node = node
                elif result[node] < result[min_node]:
                    min_node = node

        if min_node is None:
            break

        current_distance = result[min_node]


        for neibhour in graph.neibhours[min_node]:
            if neibhour in unvisited:
                distance = current_distance + graph.distances[(min_node, neibhour)]

                if (neibhour not in result) or (distance < result[neibhour]):
                    result[neibhour] = distance

                    path[neibhour] = min_node

        unvisited.remove(min_node)

    return result


print(deikstra(testGraph, 'A'))