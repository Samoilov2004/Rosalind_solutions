from Bio.Seq import Seq
from Bio.Data import CodonTable

file_path = './PTRA_input.txt'

def find_genetic_code_index(dna_sequence, protein_sequence):
    rna_sequence = Seq(dna_sequence).transcribe()

	#i - index of different genetic codes
    for i in range(1, 34):
        try:
            translated_protein = rna_sequence.translate(table=i, to_stop=True)

            if translated_protein == protein_sequence:
                return i
        except Exception as e:
            continue
    return None

with open(file_path, 'r') as f:
	dna_sequence = f.readline().strip()
	protein_sequence = f.readline().strip()

result = find_genetic_code_index(dna_sequence, protein_sequence)

print(result)
with open('PTRA_output.txt', 'w') as f:
	f.write(str(result))