import pulp
import networkx as nx

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

# Create a directed graph
G = nx.DiGraph()

# Add edges to the graph
for node, neighbors in graph.items():
    for neighbor, weight in neighbors.items():
        G.add_edge(node, neighbor, weight=weight)

# Define the source and destination nodes
source = 'A'
destination = 'J'

# Create a PuLP problem instance
prob = pulp.LpProblem("Shortest_Path_Problem", pulp.LpMinimize)

# Create binary variables for each edge
x = {}
for (i, j) in G.edges():
    x[(i, j)] = pulp.LpVariable(f"x_{i}_{j}", cat='Binary')

# Objective function: Minimize the total distance
prob += pulp.lpSum(G.edges[i, j]['weight'] * x[(i, j)] for (i, j) in G.edges())

# Constraints: Flow conservation
for node in G.nodes():
    if node == source:
        prob += pulp.lpSum(x[(i, j)] for (i, j) in G.out_edges(node)) - pulp.lpSum(x[(j, i)] for (j, i) in G.in_edges(node)) == 1
    elif node == destination:
        prob += pulp.lpSum(x[(i, j)] for (i, j) in G.out_edges(node)) - pulp.lpSum(x[(j, i)] for (j, i) in G.in_edges(node)) == -1
    else:
        prob += pulp.lpSum(x[(i, j)] for (i, j) in G.out_edges(node)) - pulp.lpSum(x[(j, i)] for (j, i) in G.in_edges(node)) == 0

# Solve the problem
prob.solve()

# Print the results
print(f"Status: {pulp.LpStatus[prob.status]}")

if pulp.LpStatus[prob.status] == 'Optimal':
    print("Shortest path from A to J:")
    for (i, j) in G.edges():
        if pulp.value(x[(i, j)]) == 1:
            print(f"Edge {i} -> {j} with weight {G.edges[i, j]['weight']}")