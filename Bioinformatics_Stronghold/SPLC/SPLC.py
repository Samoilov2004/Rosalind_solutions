from Bio import SeqIO
from Bio.Seq import Seq

file_path = 'SPLC_input.fasta'

sequences = []
for record in SeqIO.parse(file_path, "fasta"):
	sequences.append(str(record.seq))
	
dna_sequence = sequences[0]
introns = sequences[1:]


for i in introns:
    dna_sequence = dna_sequence.replace(i, '')

rna_sequence = dna_sequence.replace('T', 'U')

# Ensure the length of the RNA sequence is a multiple of three
rna_sequence = rna_sequence[:len(rna_sequence) - (len(rna_sequence) % 3)]

protein = str(Seq(rna_sequence).translate(to_stop=True))

print(protein)
with open('./SPLC_output.txt', 'w') as f:
	f.write(protein)