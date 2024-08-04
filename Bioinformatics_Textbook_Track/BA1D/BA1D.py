input_file = './BA1D_input.txt'
output_file = './BA1D_output.txt'

with open(input_file, 'r') as f:
    pattern = f.readline().strip()
    genome = f.readline().strip()

def substring_index(pattern, genome):
    indices = []
    pattern_length = len(pattern)
    genome_length = len(genome)

    for i in range(genome_length - pattern_length + 1):
        if genome[i:i + pattern_length] == pattern:
            indices.append(i)

    return indices

result = ' '.join(map(str, substring_index(pattern, genome)))
print(result)

with open(output_file, 'w') as f:
    f.write(result)
