import pandas as pd
import networkx as nx
import time

# Load the data
file_path = 'datagram.xlsx'
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

# Define the DP function
def max_takjil(current_node, remaining_budget, visited, total_price, path):
    if (current_node, remaining_budget) in memo:
        return memo[(current_node, remaining_budget)]

    path = path + [current_node]
    self_loop_cost = G[current_node][current_node]['weight']
    
    if remaining_budget < self_loop_cost:
        memo[(current_node, remaining_budget)] = (len(visited), path, total_price)
        return len(visited), path, total_price
    
    total_price += self_loop_cost
    remaining_budget -= self_loop_cost
    
    max_nodes = len(visited) + 1
    best_path = path
    new_visited = visited | {current_node}
    
    for neighbor in G.neighbors(current_node):
        if neighbor not in new_visited:
            travel_cost = G[current_node][neighbor]['weight']
            if remaining_budget >= travel_cost + G[neighbor][neighbor]['weight']:
                nodes_visited, new_path, new_price = max_takjil(
                    neighbor, remaining_budget - travel_cost, new_visited, total_price, path
                )
                if nodes_visited > max_nodes:
                    max_nodes = nodes_visited
                    best_path = new_path
                    total_price = new_price
    
    memo[(current_node, remaining_budget)] = (max_nodes, best_path, total_price)
    return max_nodes, best_path, total_price

# Input starting node and budget
starting_node = input("Enter the starting node: ")
budget = int(input("Enter the budget limit: "))

# Validate starting node
if starting_node not in G.nodes:
    raise ValueError(f"Node '{starting_node}' is not in the graph.")

# Initialize memoization dictionary
memo = {}

# Measure running time of the DP function
start_time = time.time()

# Calculate result for the specified starting node
result = max_takjil(starting_node, budget, set(), 0, [])

# Measure end time
end_time = time.time()
running_time = end_time - start_time

# Adjust the path to ensure it stays within budget and is valid
max_nodes, path, total_price = result
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
print(f"Running Time of DP Function: {running_time:.4f} seconds")
