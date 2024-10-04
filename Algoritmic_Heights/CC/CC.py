from collections import deque

input_path = '/Users/mihail/Downloads/rosalind_cc-3.txt'
output_path = './CC_output.txt'


def read_graph(file_path):
    with open(input_path) as f:
        n_elements, m = list(map(int, f.readline().strip().split()))
		
        d = {}
        for i in range(1, n_elements+1):
            d[i] = []
		
        for i in range(m):
            a, b = list(map(int, f.readline().strip().split()))
            d[a].append(b)
            d[b].append(a)
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
   
   
def CountComponents(graph):
    visited = set()
    count = 0

    for node in graph:
        if node not in visited:
            count += 1
            queue = deque([node])
            visited.add(node)

            while queue:
                current_node = queue.popleft()
                for neighbor in graph[current_node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

    return count


graph = read_graph(input_path)
result = str(CountComponents(graph))

print(result)
with open(output_path, 'w') as f:
    f.write(result)