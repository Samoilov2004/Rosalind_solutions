file_path = './MER_input.txt'

with open(file_path, 'r') as f:
	len_a = int(f.readline().strip())
	A = list(map(int, f.readline().strip().split()))
	len_b = int(f.readline().strip())
	B = list(map(int, f.readline().strip().split()))
	
def merge_arrays(A, B):
    final_array = []
    i = j = 0

    while i < len_a and j < len_b:
        if A[i] <= B[j]:
            final_array.append(A[i])
            i += 1
        else:
            final_array.append(B[j])
            j += 1

    while i < len_a:
        final_array.append(A[i])
        i += 1

    while j < len_b:
        final_array.append(B[j])
        j += 1

    return final_array


final_array = merge_arrays(A, B)
print(*final_array)

with open('./MER_output.txt', 'w') as f:
	f.write(' '.join(list(map(str, final_array))))
