input_file = './3SUM_input.txt'
output_file = './3SUM_output.txt'

with open(input_file, 'r') as f:
	a, b = list(map(int, f.readline().strip().split()))
	Data = []
	for _ in range(a):
		array = list(map(int, f.readline().strip().split()))
		Data.append(array)
		
def find_indices(array, array_len):
    def find_triplet(arr):
        n = array_len
        for i in range(n - 2):
            seen = {} # Initialize a dictionary to store encountered elements and their indices
            for j in range(i + 1, n):
                x = -(arr[i] + arr[j])
                if x in seen: # Check if the complement value is in the dictionary
                    return (seen[x] + 1, i + 1, j + 1)
                seen[arr[j]] = j
        return -1

    result = find_triplet(array)
    if result != -1:
        p, q, r = sorted(result)
        return [p, q, r]
    return -1

indices = [find_indices(i, b) for i in Data]
result = '\n'.join(' '.join(map(str, index)) if isinstance(index, list) else str(index) for index in indices)

print(result)
with open(output_file, 'w') as f:
	f.write(result)	