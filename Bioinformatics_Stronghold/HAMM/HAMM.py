file_path = './HAMM_input.txt'

with open(file_path, 'r') as f:
    first = f.readline().strip()
    second = f.readline().strip()
    a = len(first)

hamming_distance = sum(1 for i in range(a) if first[i] != second[i])
print(hamming_distance)

with open('./HAMM_output.txt', 'w') as f:
    f.write(str(hamming_distance))