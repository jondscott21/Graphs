from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for i in range(len(ancestors)):
        graph.add_vertex(ancestors[i][0])
        graph.add_vertex(ancestors[i][1])
    for i in range(len(ancestors)):
        graph.add_edge(ancestors[i][1], ancestors[i][0])
    if len(graph.get_neighbors(starting_node)) == 0:
        return -1
    return graph.bft(starting_node)[-1]
# test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

# print(earliest_ancestor(test_ancestors, 2))