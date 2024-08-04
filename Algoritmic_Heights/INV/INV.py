input_file = './INV_input.txt'
output_file = './INV_output.txt'

with open(input_file, 'r') as f:
	array_len = int(f.readline().strip()) 
	array = list(map(int, f.readline().strip().split()))
		
def merge_sort_count(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, left_inv = merge_sort_count(arr[:mid])
    right, right_inv = merge_sort_count(arr[mid:])
    merged, split_inv = merge_count(left, right)

    total_inv = left_inv + right_inv + split_inv
    return merged, total_inv

def merge_count(left, right):
    sorted_array = []
    i = j = 0
    split_inv = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1
            split_inv += len(left) - i

    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])

    return sorted_array, split_inv

def count_inversions(arr):
    _, inversions = merge_sort_count(arr)
    return inversions

result = count_inversions(array)

print(result)
with open(output_file, 'w') as f:
	f.write(str(result))