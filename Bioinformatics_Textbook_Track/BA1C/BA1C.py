from Bio.Seq import Seq

input_file = './BA1C_input.txt'
output_file = './BA1C_output.txt'

with open(input_file, 'r') as f:
	sequence = Seq(f.readline().strip())

result = str(sequence.reverse_complement())

print(result)
with open(output_file, 'w') as f:
	f.write(result)