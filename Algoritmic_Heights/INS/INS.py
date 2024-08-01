file_path = './INS_input.txt'

with open(file_path, 'r') as f:
	a = int(f.readline().strip())
	arr = list(map(int, f.readline().strip().split()))
	
def insertion_sort_swaps(arr):
    n = len(arr)
    swap_count = 0

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            swap_count += 1
        arr[j + 1] = key

    return swap_count

result = insertion_sort_swaps(arr)
print(result)

with open('./INS_output.txt', 'w') as f:
	f.write(str(result))