import pandas as pd
import networkx as nx
import streamlit as st
import time
import matplotlib.pyplot as plt

# Load the data
file_path = '/Users/hamdikr/Downloads/datagram.xlsx'  # Replace with your file path
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

# Function to visualize the path
def plot_path(G, path):
    pos = nx.spring_layout(G)
    plt.figure(figsize=(12, 8))
    
    # Draw the full graph
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=10, font_weight='bold')
    
    # Highlight the path
    path_edges = list(zip(path, path[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)
    
    # Highlight the nodes in the path
    nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='orange')
    
    # Highlight the self-loops
    self_loops = [(node, node) for node in path]
    nx.draw_networkx_edges(G, pos, edgelist=self_loops, edge_color='green', width=2, style='dashed')
    
    st.pyplot(plt)

# Streamlit App
st.title('Max Takjil Path Finder')

# Display the datagram table
st.subheader('Datagram Table')
st.dataframe(df)

# Input starting node and budget
starting_node = st.selectbox('Select the starting node:', G.nodes)
budget = st.number_input('Enter the budget limit:', min_value=0, value=50000, step=1000)
algorithm = st.selectbox('Select the algorithm:', ['Dynamic Programming', 'Greedy'])

# Initialize memoization dictionary for DP
memo = {}

if st.button('Find Max Takjil Path'):
    if algorithm == 'Dynamic Programming':
        # Measure running time of the DP function
        dp_start_time = time.time()
        dp_result = max_takjil(starting_node, budget, set(), 0, [])
        dp_end_time = time.time()
        dp_running_time = dp_end_time - dp_start_time
        
        # Process DP result
        dp_path, dp_total_price = dp_result[1], dp_result[2]
        dp_adjusted_path = []
        dp_adjusted_price = 0
        dp_visited = set()
        for p in dp_path:
            if p not in dp_visited:
                self_loop_cost = G[p][p]['weight']
                if dp_adjusted_price + self_loop_cost <= budget:
                    dp_adjusted_path.append(p)
                    dp_adjusted_price += self_loop_cost
                    dp_visited.add(p)
                else:
                    break

        # Correct total price calculation for DP output
        dp_total_price_str = " + ".join([f"{G[n][n]['weight']} ({n})" for n in dp_path])
        dp_adjusted_price_str = " + ".join([f"{G[n][n]['weight']} ({n})" for n in dp_adjusted_path])
        dp_output_str = f"Starting Node: {starting_node}\n"
        dp_output_str += f"Adjusted Path: {dp_adjusted_path}\n"
        dp_output_str += f"Adjusted Total Price: {dp_adjusted_price_str} = {dp_adjusted_price}\n"
        
        # Display the results
        st.subheader("Dynamic Programming Approach:")
        st.text(dp_output_str)
        st.text(f"Running Time of DP Function: {dp_running_time:.4f} seconds")
        plot_path(G, dp_adjusted_path)
    
    elif algorithm == 'Greedy':
        # Measure running time of the Greedy function
        greedy_start_time = time.time()
        greedy_path, greedy_total_price = greedy_takjil(starting_node, budget)
        greedy_end_time = time.time()
        greedy_running_time = greedy_end_time - greedy_start_time
        
        # Process Greedy result
        greedy_adjusted_path = []
        greedy_adjusted_price = 0
        greedy_visited = set()
        for p in greedy_path:
            if p not in greedy_visited:
                self_loop_cost = G[p][p]['weight']
                if greedy_adjusted_price + self_loop_cost <= budget:
                    greedy_adjusted_path.append(p)
                    greedy_adjusted_price += self_loop_cost
                    greedy_visited.add(p)
                else:
                    break

        # Correct total price calculation for Greedy output
        greedy_total_price_str = " + ".join([f"{G[n][n]['weight']} ({n})" for n in greedy_path])
        greedy_adjusted_price_str = " + ".join([f"{G[n][n]['weight']} ({n})" for n in greedy_adjusted_path])
        greedy_output_str = f"Starting Node: {starting_node}\n"
        greedy_output_str += f"Adjusted Path: {greedy_adjusted_path}\n"
        greedy_output_str += f"Adjusted Total Price: {greedy_adjusted_price_str} = {greedy_adjusted_price}\n"
        
        # Display the results
        st.subheader("Greedy Approach:")
        st.text(greedy_output_str)
        st.text(f"Running Time of Greedy Function: {greedy_running_time:.4f} seconds")
        plot_path(G, greedy_adjusted_path)
