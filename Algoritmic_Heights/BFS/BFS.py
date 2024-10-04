from collections import deque

input_path = './BFS_input.txt'
output_path = './BFS_output.txt'


def read_graph(file_path):
	with open(input_path) as f:
		n_elements, m = list(map(int, f.readline().strip().split()))
		
		d = {}
		for i in range(1, n_elements+1):
			d[i] = []
		
		for i in range(m):
			a, b = list(map(int, f.readline().strip().split()))
			d[a].append(b)
	return d


def BFS(graph_dict, start, end):
    queue = deque([(start, 0)])

    visited = {start}

    while queue:
        node, distance = queue.popleft()

        if node == end:
            return distance

        for neighbor in graph_dict[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))

    return -1

graph = read_graph(input_path)
result_array = [str(BFS(graph, 1, i)) for i in range(1, max(graph)+1)]
result = ' '.join(result_array)

print(result)
with open(output_path, 'w') as f:
    f.write(result)