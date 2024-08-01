from Bio.Seq import Seq
from Bio import SeqIO

file_path = './ORF_input.fasta'
	
for record in SeqIO.parse(file_path, "fasta"):
	dna_string = record.seq


def find_avaliable_proteins(dna_seq):
    # Function to translate a DNA sequence in all six reading frames
    def translate_frames(seq):
        translations = []
        for frame in range(3):
            # Ensure the sequence length is a multiple of three
            trimmed_seq = seq[frame:]
            trimmed_seq = trimmed_seq[:len(trimmed_seq) - (len(trimmed_seq) % 3)]
            translations.append(trimmed_seq.translate())
        return translations

    forward_translations = translate_frames(Seq(dna_seq))

    reverse_complement_seq = Seq(dna_seq).reverse_complement()
    reverse_translations = translate_frames(reverse_complement_seq)

    # Combine all translations
    all_translations = forward_translations + reverse_translations
    
    return all_translations

   
def find_orfs(proteins):
    orfs = []
    for protein in proteins:
        start_positions = [i for i, aa in enumerate(protein) if aa == 'M']
        for start in start_positions:
            orf = ''
            for i in range(start, len(protein)):
                if protein[i] == '*':
                    if '*' not in orf:
                        orfs.append(orf)
                    break
                orf += protein[i]
    return set(map(str, orfs))


proteins = find_avaliable_proteins(dna_string)
orfs = find_orfs(proteins)

print(*orfs, sep='\n')

with open('ORF_output.txt', 'w') as f:
	f.write('\n'.join(orfs))