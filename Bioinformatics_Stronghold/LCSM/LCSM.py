from Bio.Seq import Seq
from Bio import SeqIO

input_path = './LCSM_input.fasta'
output_path = './LCSM_output.txt'


def read_fasta(path):
	sequences = []
	for record in SeqIO.parse(input_path, "fasta"):
		sequences.append(str(record.seq))
	
	return sequences


def is_common_substring(substring, sequences):
	for i in sequences:
		if substring not in i:
			return False
	return True
	

def find_longest_common_substring(sequences):
    shortest_sequence = min(sequences)
    n = len(shortest_sequence)

    for length in range(n + 1, 0, -1):
        for i in range(n - length + 1):
        	substring = shortest_sequence[i:i + length]
        	if is_common_substring(substring, sequences):
        		return substring

    return ''


sequences = read_fasta(input_path)
result = find_longest_common_substring(sequences)

print(result)
with open(output_path, 'w') as f:
    f.write(result)