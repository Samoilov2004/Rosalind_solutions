from Bio.Data import CodonTable

input_path = './MRNA_input.txt'
output_path = './MRNA_output.txt'

with open(input_path, 'r') as f:
	protein_string = f.readline().strip()
	
from Bio.Data import CodonTable

def count_rna_strings(protein_string):
    codon_table = CodonTable.unambiguous_dna_by_id[1]

    codon_counts = {}
    for codon in codon_table.forward_table:
        amino_acid = codon_table.forward_table[codon]
        if amino_acid in codon_counts:
            codon_counts[amino_acid] += 1
        else:
            codon_counts[amino_acid] = 1

    total_rna_strings = 1
    for amino_acid in protein_string:
        if amino_acid in codon_counts:
            total_rna_strings = (total_rna_strings * codon_counts[amino_acid]) % 1_000_000
        else:
            total_rna_strings = 0
            break

    stop_codons_count = len(codon_table.stop_codons)
    total_rna_strings = (total_rna_strings * stop_codons_count) % 1_000_000
    
    return total_rna_strings

result = count_rna_strings(protein_string)
print(result)
	
with open(output_path, 'w') as f:
	f.write(str(result))
