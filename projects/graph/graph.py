"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist.")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue and enqueue the starting vertex ID
        # Create an empty set to store visited vertices
        # While the queue is not empty...
            # Dequeue the first vertex and store it as a variable
            # If that vertex has not been visited...
                # Mark it as visited
                # Then add all of its neighbors to the back of the queue
        queue = Queue()
        queue.enqueue(starting_vertex)
        visited = set()
        while queue.size() > 0:
            vertex = queue.dequeue()
            if vertex not in visited:
                print(vertex)
                visited.add(vertex)
                for neighbor in self.vertices[vertex]:
                    queue.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty stack and push the starting vertex ID
        # Create an empty set to store visited vertices
        # While the stack is not empty...
            # Pop the first vertex and store it as a variable
            # If that vertex has not been visited...
                # Mark it as visited
                # Then add all of its neighbors to the stack
        stack = Stack()
        stack.push(starting_vertex)
        visited = set()
        while stack.size() > 0:
            vertex = stack.pop()
            if not vertex in visited:
                print(vertex)
                visited.add(vertex)
                for neighbor in self.vertices[vertex]:
                    stack.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        visited.add(starting_vertex)
        print(starting_vertex)
        for neighbor in self.vertices[starting_vertex]:
            if not neighbor in visited:
                self.dft_recursive(neighbor)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Edge case for same vertices at start
        if starting_vertex == destination_vertex:
            return [starting_vertex]
        # Create an empty queue and enqueue the starting vertex ID
        queue = Queue()
        queue.enqueue(starting_vertex)
        # Create an empty set to store visited vertices
        visited = set()
        returned_list = list()
        # While the queue is not empty...
        while queue.size() > 0:
            # Dequeue the first vertex and store it as a variable
            vertex = queue.dequeue()
            # Check if destination is in neighbors
            if destination_vertex in self.vertices[vertex]:
                # Add it to list if it is and return list
                returned_list.append(destination_vertex)
                return returned_list
            # If that vertex has not been visited...
            if vertex not in visited:
                # Mark it as visited
                visited.add(vertex)
                returned_list.append(vertex)
                # add all of its neighbors to the back of the queue
                for neighbor in self.vertices[vertex]:
                    queue.enqueue(neighbor)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Edge case for same vertices at start
        if starting_vertex == destination_vertex:
            return [starting_vertex]
        # Create an empty stack and push the starting vertex ID
        stack = Stack()
        stack.push(starting_vertex)
        # Create an empty set to store visited vertices
        visited = set()
        # While the stack is not empty...
        while stack.size() > 0:
            # Pop the first vertex and store it as a variable
            vertex = stack.pop()
            # If that vertex has not been visited...
            if not vertex in visited:
                # Mark it as visited
                visited.add(vertex)
                # Add all of its neighbors to the stack
                for neighbor in self.vertices[vertex]:
                    stack.push(neighbor)
            # Check if destination is in neighbors
            if destination_vertex in self.vertices[vertex]:
                # Add it to list if it is and return list
                visited.add(destination_vertex)
                return list(visited)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if starting_vertex is destination_vertex:
            return list(starting_vertex)
        for neighbor in self.vertices[starting_vertex]:
            if destination_vertex is neighbor:
                visited.add(starting_vertex)        
                visited.add(destination_vertex)
                return list(visited)
            if destination_vertex in self.vertices[neighbor]:
                visited.add(starting_vertex)
                visited.add(neighbor)            
                visited.add(destination_vertex)
                return list(visited)
        for neighbor in self.vertices[starting_vertex]:
            if not neighbor in visited:
                visited.add(starting_vertex)
                self.dfs_recursive(neighbor, destination_vertex, visited)
        return list(visited)

        

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_vertex(8)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)
    graph.add_edge(6, 8)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    print('bft: ')
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print('dft: ')
    graph.dft(1)
    print('dft_recursive: ')
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print('bfs: ')
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print('dfs: ')
    print(graph.dfs(1, 6))
    print('dfs_recursive: ')
    print(graph.dfs_recursive(1, 8))
