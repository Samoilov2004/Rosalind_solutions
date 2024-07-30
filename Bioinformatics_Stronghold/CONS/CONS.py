from Bio.Seq import Seq
from Bio import SeqIO

file_path = './CONS_input.fasta'

def generate_consensus_string(profile_matrix):
    consensus = []
    n = len(profile_matrix['A'])
    for i in range(n):
        counts = {
            'A': profile_matrix['A'][i],
            'C': profile_matrix['C'][i],
            'G': profile_matrix['G'][i],
            'T': profile_matrix['T'][i]
        }
        consensus.append(max(counts, key=counts.get))
    return ''.join(consensus)

arr = []
for record in SeqIO.parse(file_path, "fasta"):
	arr.append(str(record.seq))
	
l = len(arr[0])
profile_dict = {
	'A':[0 for i in range(l)],
	'C':[0 for i in range(l)],
	'G':[0 for i in range(l)],
	'T':[0 for i in range(l)]
	}

for i in arr:
	for q in range(l):
		profile_dict[i[q]][q] += 1
		
consensus = generate_consensus_string(profile_dict)

final_arr = []
for nucleotide in 'ACGT':
    final_arr.append(f"{nucleotide}: {' '.join(map(str, profile_dict[nucleotide]))}")
    
print(consensus)
for i in final_arr:
	print(i)

with open('./CONS_output.txt', 'w') as f:
    f.write(consensus)
    f.write('\n')
    for i in final_arr:
        f.write(i)
        f.write('\n')
