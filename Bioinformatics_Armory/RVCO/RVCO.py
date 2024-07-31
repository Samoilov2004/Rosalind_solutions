from Bio.Seq import Seq
from Bio import SeqIO

file_path = './RVCO_input.fasta'

def count_reverse_complement_matches(dna_strings):
    counts = 0
    for dna in dna_strings:
        reverse_complement = dna.reverse_complement()
        if dna == reverse_complement:
            counts += 1
    return counts

dna_strings = []
for record in SeqIO.parse(file_path, "fasta"):
	dna_strings.append(record.seq)

result = count_reverse_complement_matches(dna_strings)

print(result)
with open('./RVCO_output.txt', 'w') as f:
	f.write(str(result))