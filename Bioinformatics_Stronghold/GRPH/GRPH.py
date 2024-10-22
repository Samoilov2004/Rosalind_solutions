from Bio.Seq import Seq
from Bio import SeqIO

input_path = './GRPH_input.fasta'
output_path = './GRPH_output.txt'


def read_fasta(path):
	sequences_dict = dict()
	for record in SeqIO.parse(input_path, "fasta"):
		sequences_dict[record.id] = str(record.seq)
	
	return sequences_dict
	
	
def is_edge(sequences_dict, name1, name2, k=3):
    if name1 == name2:
        return False

    seq1 = sequences_dict[name1]
    seq2 = sequences_dict[name2]

    if len(seq1) < k or len(seq2) < k:
        return False

    if seq1[-k:] == seq2[:k]:
        return True

    return False
   

def find_all_edges(sequences_dict):
	edges_list = []
	names_list = sequences_dict.keys()
	
	for name1 in names_list:
		for name2 in names_list:
			if is_edge(sequences_dict, name1, name2):
				edges_list.append([name1, name2])
	
	return edges_list


sequences_dict = read_fasta(input_path)
edges_list = find_all_edges(sequences_dict)

pre_result = []
for pair in edges_list:
    pre_result.append(' '.join(pair))

result = '\n'.join(pre_result)

print(result)
with open(output_path, 'w') as f:
    f.write(result)