import sys

def get_user_input(message):
    """Gets user input as an integer."""
    while True:
        try:
            user_input = int(input(message))
            return user_input
        except ValueError:
            print("Invalid input. Please enter an integer.")

matrix = [
    [0, 5000, 0, 6000, 0, 0, 0],
    [3000, 0, 0, 0, 8000, 0, 0],
    [0, 0, 0, 0, 0, 10000, 12000],
    [3000, 0, 0, 0, 0, 0, 12000],
    [3000, 5000, 0, 0, 0, 0, 0],
    [3000, 0, 5000, 0, 0, 0, 0],
    [0, 0, 5000, 6000, 0, 0, 0],
]

data = [1, 2, 3, 4, 5, 6, 7]
n = len(data)
best_path = []
best_cost = float('inf')
most_nodes_visited = 0

def main():
    starting_point = get_user_input("Enter the starting point (integer between 1 and " + str(n) + "): ")
    if starting_point not in data:
        print("Invalid starting point. Please choose a number from the list:", data)
        return

    max_distance = get_user_input("Enter the maximum allowable distance: ")

    # Initialize global variables
    global best_path, best_cost, most_nodes_visited
    best_path = []
    best_cost = float('inf')
    most_nodes_visited = 0

    # Filter matrix based on maximum allowable distance
    filtered_matrix = [[(value if value <= max_distance else float('inf')) for value in row] for row in matrix]

    visited = [False] * n
    visited[starting_point - 1] = True

    find_best_path(starting_point, filtered_matrix, max_distance, current_cost=0, current_path=[starting_point], visited=visited, nodes_visited=1)

    if best_path:
        print('\n\nBest path found: {', ', '.join(map(str, best_path)), '} with total distance:', best_cost)
    else:
        print("No valid path found within the given distance constraint.")
    return

def find_best_path(current_node, matrix, max_distance, current_cost, current_path, visited, nodes_visited):
    global best_path, best_cost, most_nodes_visited

    # Update current cost with the value at the starting point
    current_cost += matrix[current_node - 1][current_path[0] - 1]

    # Explore all possible next nodes
    for next_node in range(n):
        if not visited[next_node] and matrix[current_node - 1][next_node] != 0 and current_cost + matrix[current_node - 1][next_node] <= max_distance:
            next_cost = current_cost + matrix[current_node - 1][next_node]
            next_path = current_path + [next_node + 1]

            visited[next_node] = True
            find_best_path(next_node + 1, matrix, max_distance, next_cost, next_path, visited, nodes_visited + 1)
            visited[next_node] = False

    # Check if the current path is better than the best found so far
    if nodes_visited > most_nodes_visited or (nodes_visited == most_nodes_visited and current_cost < best_cost):
        most_nodes_visited = nodes_visited
        best_cost = current_cost
        best_path = current_path[:]

if __name__ == '__main__':
    main()
    sys.exit(0)


