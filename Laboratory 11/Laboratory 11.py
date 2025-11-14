from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, u, v):
        """Add an edge between u and v"""
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        
        self.graph[u].append(v)
        self.graph[v].append(u)  # For undirected graph
    
    def bfs(self, start):
        """Breadth-First Search traversal"""
        visited = set()
        queue = deque([start])
        result = []
        
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                # Add all unvisited neighbors
                for neighbor in self.graph.get(vertex, []):
                    if neighbor not in visited:
                        queue.append(neighbor)
        return result
    
    def dfs(self, start):
        """Depth-First Search traversal"""
        visited = set()
        result = []
        
        def dfs_util(vertex):
            visited.add(vertex)
            result.append(vertex)
            for neighbor in self.graph.get(vertex, []):
                if neighbor not in visited:
                    dfs_util(neighbor)
        
        dfs_util(start)
        return result
    
    def display(self):
        """Display the graph"""
        for vertex in self.graph:
            print(f"{vertex}: {self.graph[vertex]}")

# Example usage
if __name__ == "__main__":
    # Create a graph
    g = Graph()
    
    # Add edges
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    
    # Display the graph
    print("Graph structure:")
    g.display()
    
    # Traversal examples
    print(f"\nBFS starting from 0: {g.bfs(0)}")
    print(f"DFS starting from 0: {g.dfs(0)}")
    
    # Add more edges and show
    g.add_edge(4, 5)
    g.add_edge(1, 4)
    
    print(f"\nAfter adding more edges:")
    print(f"BFS starting from 0: {g.bfs(0)}")
    print(f"DFS starting from 0: {g.dfs(0)}")
