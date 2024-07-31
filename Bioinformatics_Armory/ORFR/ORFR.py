from Bio.Seq import Seq

file_path = './ORFR_input.txt'

with open(file_path, 'r') as f:
	dna_string = Seq(f.readline().strip())


def find_longest_orf(dna_seq):
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

    # Find the longest protein sequence
    #looking for a sequence that begins with 'M' and ends with '*'
    longest_protein = ""
    for translation in all_translations:
        pre_proteins = translation.split("*")
        for i in pre_proteins:
        	if 'M' in i:
        		ORF_protein = i[i.index('M'):]
        		if len(ORF_protein) > len(longest_protein):
        			longest_protein = ORF_protein

    return longest_protein


result = str(find_longest_orf(dna_string))
print(result)

with open('ORFR_output.txt', 'w') as f:
	f.write(result)