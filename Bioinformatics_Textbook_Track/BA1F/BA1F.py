input_file = './BA1F_input.txt'
output_file = './BA1F_output.txt'

with open(input_file, 'r') as f:
    string = f.readline().strip()

def minimum_skew(genome):
    skew = 0
    min_skew = 0
    positions = []

    for i in range(len(genome)):
        if genome[i] == 'C':
            skew -= 1
        elif genome[i] == 'G':
            skew += 1

        if skew < min_skew:
            min_skew = skew
            positions = [i + 1]
        elif skew == min_skew:
            positions.append(i + 1)

    return positions

result_arr = minimum_skew(string)
result = ' '.join(list(map(str, result_arr)))
print(result)

with open(output_file, 'w') as f:
    f.write(result)