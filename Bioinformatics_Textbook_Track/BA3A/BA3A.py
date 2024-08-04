input_file = './BA3A_input.txt'
output_file = './BA3A_output.txt'

with open(input_file, 'r') as f:
    pattern_size = int(f.readline().strip())
    genome = f.readline().strip()

def combinations(genome, pattern_length):
    genome_length = len(genome)
    DATA = []

    for i in range(genome_length - pattern_length + 1):
    	string = genome[i:i + pattern_length]
    	DATA.append(string)

    return DATA

DATA = combinations(genome, pattern_size)
result = '\n'.join(DATA)

print(result)
with open(output_file, 'w') as f:
    f.write(result)
