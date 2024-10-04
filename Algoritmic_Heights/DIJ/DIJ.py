import heapq

input_path = '/Users/mihail/Downloads/rosalind_dij-2.txt'
output_path = './DIJ_output.txt'


def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances[end] if distances[end] != float('inf') else -1
   
   
def read_weight_graph(file_path):
	with open(file_path) as f:
		n_elements, m = list(map(int, f.readline().strip().split()))
		graph_dict = {}
		for i in range(1, n_elements+1):
			graph_dict[i] = {}
			
		for i in range(m):
			start, end, mass = list(map(int, f.readline().strip().split()))
			graph_dict[start][end] = mass
	return graph_dict
			

graph = read_weight_graph(input_path)
result_array = [str(dijkstra(graph, 1, i)) for i in range(1, max(graph)+1)]
result = ' '.join(result_array)

print(result)
with open(output_path, 'w') as f:
    f.write(result)