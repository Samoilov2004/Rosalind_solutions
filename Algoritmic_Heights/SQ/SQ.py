input_path = './SQ_input.txt'
output_path = './SQ_output.txt'


def read_graph_array(file_path):
	array_of_dict = []
	with open(input_path) as f:
		num_of_graphs = int(f.readline().strip())
		f.readline()  # space line
		
		for graph_index in range(num_of_graphs):
			d = {}
			n_elements, n_lines = list(map(int, f.readline().strip().split()))
			
			for i in range(1, n_elements+1):
				d[i] = []
				
			for i in range(n_lines):
				start, end = list(map(int, f.readline().strip().split()))
				d[start].append(end)
				d[end].append(start)
			f.readline()  # space line
			array_of_dict.append(d)
	
	return array_of_dict
				
		
def has_cycle_of_size_4(graph):
    path = []
    visited = set()

    def dfs(node, length):
        if length == 4 and node == path[0]:
            return True
        if length > 4 or node in visited:
            return False
        visited.add(node)
        path.append(node)
        if node in graph:
            for neighbor in graph[node]:
                if dfs(neighbor, length + 1):
                    return True
        path.pop()
        visited.remove(node)
        return False

    for node in graph:
        if dfs(node, 0):
            return 1
    return -1


graphs_array = read_graph_array(input_path)
result_array = [str(has_cycle_of_size_4(i)) for i in graphs_array]
result = ' '.join(result_array)

print(result)
with open(output_path, 'w') as f:
    f.write(result)