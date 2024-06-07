import pandas as pd
import networkx as nx
import time

# Load the data
file_path = 'datagram.xlsx'  # Replace with your file path
df = pd.read_excel(file_path)

# Initialize the graph
G = nx.DiGraph()

# Add edges to the graph based on the DataFrame
for index, row in df.iterrows():
    node1, node2 = row['path'].split(' - ')
    distance = row['distance']
    if row['path type'] == 'two way':
        G.add_edge(node1, node2, weight=distance)
        G.add_edge(node2, node1, weight=distance)
    else:
        G.add_edge(node1, node2, weight=distance)

# Add self-loops with given costs
self_loops = {
    'Es_cekek': 3000,
    'Cireng': 5000,
    'Es_teh': 5000,
    'Roti_bakar': 6000,
    'Kentang': 8000,
    'Batagor': 10000,
    'Dimsum': 12000
}
for node, price in self_loops.items():
    G.add_edge(node, node, weight=price)

# Define the greedy function
def greedy_takjil(start_node, budget):
    remaining_budget = budget
    path = []
    total_price = 0
    current_node = start_node

    while remaining_budget > 0:
        path.append(current_node)
        self_loop_cost = G[current_node][current_node]['weight']
        if remaining_budget < self_loop_cost:
            break
        remaining_budget -= self_loop_cost
        total_price += self_loop_cost

        # Find the next node with the lowest travel cost + self-loop cost within the remaining budget
        next_node = None
        min_cost = float('inf')
        for neighbor in G.neighbors(current_node):
            travel_cost = G[current_node][neighbor]['weight']
            neighbor_self_loop_cost = G[neighbor][neighbor]['weight']
            if neighbor not in path and remaining_budget >= travel_cost + neighbor_self_loop_cost:
                if travel_cost + neighbor_self_loop_cost < min_cost:
                    min_cost = travel_cost + neighbor_self_loop_cost
                    next_node = neighbor
        
        if next_node is None:
            break
        remaining_budget -= G[current_node][next_node]['weight']
        current_node = next_node

    return path, total_price

# Input starting node and budget
starting_node = input("Enter the starting node: ")
budget = int(input("Enter the budget limit: "))

# Validate starting node
if starting_node not in G.nodes:
    raise ValueError(f"Node '{starting_node}' is not in the graph.")

# Measure running time of the greedy function
start_time = time.time()

# Calculate result for the specified starting node
path, total_price = greedy_takjil(starting_node, budget)

# Measure end time
end_time = time.time()
running_time = end_time - start_time

# Adjust the path to ensure it stays within budget and is valid
adjusted_path = []
adjusted_price = 0
visited = set()
for p in path:
    if p not in visited:
        self_loop_cost = G[p][p]['weight']
        if adjusted_price + self_loop_cost <= budget:
            adjusted_path.append(p)
            adjusted_price += self_loop_cost
            visited.add(p)
        else:
            break

# Correct total price calculation for output
total_price_str = " + ".join([f"{G[n][n]['weight']} ({n})" for n in path])
adjusted_price_str = " + ".join([f"{G[n][n]['weight']} ({n})" for n in adjusted_path])
output_str = f"Starting Node: {starting_node}\n"
output_str += f"Adjusted Path: {adjusted_path}\n"
output_str += f"Adjusted Total Price: {adjusted_price_str} = {adjusted_price}\n"

# Print the result
print(output_str)
print(f"Running Time of Greedy Function: {running_time:.4f} seconds")
