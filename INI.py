from Bio.Seq import Seq

file_path = './INI_input.txt'

with open(file_path, 'r') as file:
    data = file.read().split()

sequence = str(data[0])

numbers = []
for symbol in 'ACGT':
    my_seq = Seq(sequence)
    count = my_seq.count(symbol)
    numbers.append(count)

print(*numbers)

with open('./INI_output.txt', 'w') as output_file:
    output_file.write(" ".join(map(str, numbers)))