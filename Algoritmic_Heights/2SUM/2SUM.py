input_file = './2SUM_input.txt'
output_file = './2SUM_output.txt'

with open(input_file, 'r') as f:
	a, b = list(map(int, f.readline().strip().split()))
	Data = []
	for _ in range(a):
		array = list(map(int, f.readline().strip().split()))
		Data.append(array)
		
def find_indices(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] == -arr[j]:
                return [i + 1, j + 1]
    return -1

indices = [find_indices(i) for i in Data]
result = '\n'.join(' '.join(map(str, index)) if isinstance(index, list) else str(index) for index in indices)

print(result)
with open(output_file, 'w') as f:
	f.write(result)	