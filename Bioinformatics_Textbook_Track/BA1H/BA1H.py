input_file = './BA1H_input.txt'
output_file = './BA1H_output.txt'

with open(input_file, 'r') as f:
    pattern = f.readline().strip()
    genome = f.readline().strip()
    max_errors = int(f.readline().strip())
    
hamming_distance = lambda s1, s2: sum(n1 != n2 for n1, n2 in zip(s1, s2))

def substring_index(pattern, genome):
    indices = []
    pattern_length = len(pattern)
    genome_length = len(genome)

    for i in range(genome_length - pattern_length + 1):
    	string = genome[i:i + pattern_length]
    	if hamming_distance(string, pattern) <= max_errors:
            indices.append(i)

    return indices

result = ' '.join(map(str, substring_index(pattern, genome)))
print(result)

with open(output_file, 'w') as f:
    f.write(result)