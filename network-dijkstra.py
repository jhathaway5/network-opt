import heapq
import networkx as nx
import matplotlib.pyplot as plt

# Function to implement Dijkstra's algorithm
def dijkstra(graph, start_node):
    # Initialize distances from the start node to all other nodes as infinity
    distances = {node: float('infinity') for node in graph}
    # Distance from the start node to itself is zero
    distances[start_node] = 0

    # Priority queue to select the node with the smallest distance
    priority_queue = [(0, start_node)]

    # Dictionary to store the shortest path tree
    shortest_path_tree = {node: None for node in graph}

    while priority_queue:
        # Select the node with the smallest distance
        current_distance, current_node = heapq.heappop(priority_queue)

        # If the current distance is greater than the recorded distance, skip it
        if current_distance > distances[current_node]:
            continue

        # Explore neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # If a shorter path is found, update the distance and add it to the priority queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                shortest_path_tree[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, shortest_path_tree

# Define the graph as a dictionary
graph = {
    'A': {'B': 2, 'C': 4, 'D': 7},
    'B': {'E': 3, 'F': 8},
    'C': {'D': 1, 'G': 5},
    'D': {'H': 2},
    'E': {'F': 2, 'I': 6},
    'F': {'J': 3},
    'G': {'H': 3},
    'H': {'I': 1},
    'I': {'J': 4},
    'J': {}
}

# Run Dijkstra's algorithm from node 'A'
shortest_paths, shortest_path_tree = dijkstra(graph, 'A')

# Print the shortest paths from 'A' to all other nodes
for node, distance in shortest_paths.items():
    print(f"Shortest path from A to {node}: {distance}")

# Visualization
G = nx.DiGraph()

# Add edges to the graph
for node, neighbors in graph.items():
    for neighbor, weight in neighbors.items():
        G.add_edge(node, neighbor, weight=weight)

# Position nodes using the spring layout
pos = nx.spring_layout(G)

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_size=700, node_color='lightblue')

# Draw edges
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), arrowstyle='-|>', arrowsize=20)

# Draw node labels
nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')

# Draw edge labels
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Highlight the shortest path tree
path_edges = []
for node in shortest_path_tree:
    if shortest_path_tree[node]:
        path_edges.append((shortest_path_tree[node], node))

nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2, arrowstyle='-|>', arrowsize=25)

plt.title("Shortest Path Tree using Dijkstra's Algorithm")
plt.show()