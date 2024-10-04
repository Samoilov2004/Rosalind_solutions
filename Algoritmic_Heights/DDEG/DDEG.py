input_path = './DDEG_input.txt'
output_path = './DDEG_output.txt'


with open(input_path) as f:
	n_elements, m = list(map(int, f.readline().strip().split()))
		
	d = {}
	for i in range(1, n_elements+1):
		d[i] = []
		
	for i in range(m):
		a, b = list(map(int, f.readline().strip().split()))
		d[a].append(b)
		d[b].append(a)

help_dict = {}
for element in range(1, n_elements+1):
	help_dict[element] = [len(d[i]) for i in d[element]]
	
len_arr = [str(sum(help_dict[i])) for i in range(1, n_elements+1)]
result = ' '.join(len_arr)

print(result)
with open(output_path, 'w') as f:
    f.write(str(result))