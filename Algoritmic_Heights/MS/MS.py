input_file = './MS_input.txt'
output_file = './MS_output.txt'

with open(input_file, 'r') as f:
	l = int(f.readline().strip())
	array = list(map(int, f.readline().strip().split()))

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

sorted_arr = merge_sort(array)
result = ' '.join(list(map(str, sorted_arr)))

print(result)
with open(output_file, 'w') as f:
	f.write(result)