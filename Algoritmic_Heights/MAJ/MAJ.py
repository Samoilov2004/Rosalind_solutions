file_path = './MAJ_input.txt'

with open(file_path, 'r') as f:
	a, b = list(map(int, f.readline().strip().split()))
	
	arrays = []
	for i in range(a):
		new_arr = list(map(int, f.readline().strip().split()))
		arrays.append(new_arr)

#realisation of Boyer–Moore string-search algorithm
def find_majority_element(arr):
    candidate = None
    count = 0

    for num in arr:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    count = 0
    for num in arr:
        if num == candidate:
            count += 1

    if count > len(arr) // 2:
        return candidate
    else:
        return -1
       
results = []
for i in arrays:
	results.append(find_majority_element(i))

print(*results)
with open('./MAJ_output.txt', 'w') as f:
	result_string = ' '.join(map(str, results))
	f.write(result_string)
		