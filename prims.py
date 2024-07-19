import heapq
def prims_algorithm(graph):
    mst = []
    visited = set()
    start_node = list(graph.keys())[0]  # Choose any starting node
    visited.add(start_node)
    edges = [(weight, start_node, neighbor) for neighbor, weight in graph[start_node]]
    heapq.heapify(edges)
    while len(visited) < len(graph):
        weight, source, destination = heapq.heappop(edges)
        if destination in visited:
            continue
        mst.append((source, destination, weight))
        visited.add(destination)
        for neighbor, weight in graph[destination]:
            if neighbor not in visited:
                heapq.heappush(edges, (weight, destination, neighbor))
    
    return mst
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 5), ('D', 7)],
    'C': [('A', 3), ('B', 5), ('D', 6)],
    'D': [('B', 7), ('C', 6)]
}
mst = prims_algorithm(graph)
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)
