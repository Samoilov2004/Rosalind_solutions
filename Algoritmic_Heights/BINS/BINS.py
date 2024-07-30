file_path = './BINS_input.txt'

def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read().split()

    n = int(data[0])
    m = int(data[1])
    array = list(map(int, data[2:2+n]))
    numbers = list(map(int, data[2+n:2+n+m]))

    return n, m, array, numbers

n, m, array, numbers = read_data_from_file(file_path)

def binary_search(arr, key):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            return mid + 1  # Return 1-based index
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return -1

indexes = []
for i in numbers:
	result = binary_search(array, i)
	indexes.append(result)
	
print(*indexes)

with open('./BINS_output.txt', 'w') as output_file:
    output_file.write(" ".join(map(str, indexes)))
