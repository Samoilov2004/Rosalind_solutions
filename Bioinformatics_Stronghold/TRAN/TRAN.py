from Bio import SeqIO

input_file = './TRAN_input.txt'
output_file = './TRAN_output.txt'

Sequences = []
for record in SeqIO.parse(input_file, "fasta"):
	Sequences.append(str(record.seq))

string1 = Sequences[0]
string2 = Sequences[1]

def calculate_ratio(s1, s2):
    transitions = 0
    transversions = 0

    transition_pairs = {('A', 'G'), ('G', 'A'), ('C', 'T'), ('T', 'C')}
    transversion_pairs = {('A', 'C'), ('C', 'A'), ('A', 'T'), ('T', 'A'),
                          ('G', 'C'), ('C', 'G'), ('G', 'T'), ('T', 'G')}

    for nucleotide1, nucleotide2 in zip(s1, s2):
        if nucleotide1 != nucleotide2:
            if (nucleotide1, nucleotide2) in transition_pairs:
                transitions += 1
            elif (nucleotide1, nucleotide2) in transversion_pairs:
                transversions += 1

    if transversions == 0:
        return transitions

    return transitions / transversions

result = calculate_ratio(string1, string2)

print(result)
with open(output_file, 'w') as f:
	f.write(str(result))